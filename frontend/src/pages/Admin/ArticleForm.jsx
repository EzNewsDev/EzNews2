import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import Navbar from '../../components/Navbar';
import api from '../../utils/api';
import { toast } from 'react-toastify';

export const ArticleForm = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const isEditMode = !!id;

    const formatDateForInput = (date) => {
        if (!date) return '';
        const d = new Date(date);
        const offset = d.getTimezoneOffset() * 60000;
        const localDate = new Date(d.getTime() - offset);
        return localDate.toISOString().slice(0, 16);
    };

    const [formData, setFormData] = useState({
        title: '',
        content: '',
        category_id: '',
        image_url: '',
        author_name: '',
        published_date: formatDateForInput(new Date()), // Default to current local time
        tags: [] // Array of tag IDs
    });

    const [categories, setCategories] = useState([]);
    const [availableTags, setAvailableTags] = useState([]);
    const [loading, setLoading] = useState(false);
    const [initialLoading, setInitialLoading] = useState(true);

    useEffect(() => {
        fetchInitialData();
    }, [id]);

    const fetchInitialData = async () => {
        try {
            const [categoriesRes, tagsRes] = await Promise.all([
                api.get('/categories'),
                api.get('/tags')
            ]);

            setCategories(categoriesRes.data.categories || []);
            setAvailableTags(tagsRes.data.tags || []);

            if (isEditMode) {
                const articleRes = await api.get(`/articles/${id}`);
                const article = articleRes.data;

                setFormData({
                    title: article.title,
                    content: article.content,
                    category_id: article.category?.id || '',
                    image_url: article.image_url || '',
                    author_name: article.author_name,
                    published_date: article.published_date ? formatDateForInput(article.published_date) : '',
                    tags: article.tags ? article.tags.map(t => t.id) : []
                });
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            toast.error('Gagal memuat data');
        } finally {
            setInitialLoading(false);
        }
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleTagChange = (e) => {
        const selectedOptions = Array.from(e.target.selectedOptions, option => parseInt(option.value));
        setFormData(prev => ({
            ...prev,
            tags: selectedOptions
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const payload = {
                ...formData,
                category_id: parseInt(formData.category_id),
                published_date: new Date(formData.published_date).toISOString(),
                tag_ids: formData.tags // Backend expects tag_ids
            };

            if (isEditMode) {
                await api.put(`/articles/${id}`, payload);
                toast.success('Artikel berhasil diperbarui');
            } else {
                await api.post('/articles', payload);
                toast.success('Artikel berhasil dibuat');
            }
            navigate('/admin/articles');
        } catch (error) {
            console.error('Error saving article:', error);
            const errorMsg = error.response?.data?.errors?.join(', ') || error.response?.data?.error || 'Gagal menyimpan artikel';
            toast.error(errorMsg);
        } finally {
            setLoading(false);
        }
    };

    if (initialLoading) {
        return (
            <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
                <div className="spinner border-4 border-primary border-t-transparent rounded-full w-12 h-12 animate-spin"></div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />
            <div className="max-w-4xl mx-auto px-4 py-12">
                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-8">
                    <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
                        {isEditMode ? 'Edit Artikel' : 'Buat Artikel Baru'}
                    </h1>

                    <form onSubmit={handleSubmit} className="space-y-6">
                        {/* Title */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                Judul Artikel
                            </label>
                            <input
                                type="text"
                                name="title"
                                value={formData.title}
                                onChange={handleChange}
                                required
                                minLength={5}
                                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                                placeholder="Masukkan judul artikel (min. 5 karakter)"
                            />
                        </div>

                        {/* Author */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                Penulis
                            </label>
                            <input
                                type="text"
                                name="author_name"
                                value={formData.author_name}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                                placeholder="Nama penulis"
                            />
                        </div>

                        {/* Category */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                Kategori
                            </label>
                            <select
                                name="category_id"
                                value={formData.category_id}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                            >
                                <option value="">Pilih Kategori</option>
                                {categories.map(cat => (
                                    <option key={cat.id} value={cat.id}>
                                        {cat.name}
                                    </option>
                                ))}
                            </select>
                        </div>

                        {/* Tags */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                Tags (Tahan Ctrl/Cmd untuk memilih banyak)
                            </label>
                            <select
                                multiple
                                name="tags"
                                value={formData.tags}
                                onChange={handleTagChange}
                                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white h-32"
                            >
                                {availableTags.map(tag => (
                                    <option key={tag.id} value={tag.id}>
                                        {tag.name}
                                    </option>
                                ))}
                            </select>
                        </div>

                        {/* Image URL */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                URL Gambar
                            </label>
                            <input
                                type="url"
                                name="image_url"
                                value={formData.image_url}
                                onChange={handleChange}
                                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                                placeholder="https://example.com/image.jpg"
                            />
                            {formData.image_url && (
                                <div className="mt-2">
                                    <p className="text-xs text-gray-500 mb-1">Preview:</p>
                                    <img
                                        src={formData.image_url}
                                        alt="Preview"
                                        className="h-40 object-cover rounded-lg border border-gray-200 dark:border-gray-700"
                                        onError={(e) => e.target.style.display = 'none'}
                                    />
                                </div>
                            )}
                        </div>

                        {/* Published Date */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                Tanggal Publikasi
                            </label>
                            <input
                                type="datetime-local"
                                name="published_date"
                                value={formData.published_date}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                            />
                        </div>

                        {/* Content */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                Konten Artikel
                            </label>
                            <textarea
                                name="content"
                                value={formData.content}
                                onChange={handleChange}
                                required
                                minLength={50}
                                rows="15"
                                className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-white dark:bg-gray-700 text-gray-900 dark:text-white font-mono text-sm"
                                placeholder="Tulis konten artikel di sini... (min. 50 karakter)"
                            ></textarea>
                        </div>

                        {/* Actions */}
                        <div className="flex justify-end space-x-4 pt-4 border-t border-gray-200 dark:border-gray-700">
                            <button
                                type="button"
                                onClick={() => navigate('/admin/articles')}
                                className="px-6 py-2 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
                            >
                                Batal
                            </button>
                            <button
                                type="submit"
                                disabled={loading}
                                className="px-6 py-2 bg-primary text-white rounded-lg hover:bg-primary-light transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center"
                            >
                                {loading ? (
                                    <>
                                        <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                        </svg>
                                        Menyimpan...
                                    </>
                                ) : (
                                    'Simpan Artikel'
                                )}
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};
