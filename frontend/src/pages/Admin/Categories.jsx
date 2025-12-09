import React, { useState, useEffect } from 'react';
import Navbar from '../../components/Navbar';
import LoadingSkeleton from '../../components/LoadingSkeleton';
import api from '../../utils/api';
import { toast } from 'react-toastify';

export const Categories = () => {
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [editingCategory, setEditingCategory] = useState(null);
    const [formData, setFormData] = useState({
        name: '',
        slug: ''
    });
    const [submitting, setSubmitting] = useState(false);

    useEffect(() => {
        fetchCategories();
    }, []);

    const fetchCategories = async () => {
        setLoading(true);
        try {
            const response = await api.get('/categories');
            setCategories(response.data.categories);
        } catch (error) {
            console.error('Error fetching categories:', error);
            toast.error('Gagal memuat kategori');
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => {
            const newData = { ...prev, [name]: value };
            // Auto-generate slug from name if slug is empty or was auto-generated
            if (name === 'name' && (!editingCategory || prev.slug === createSlug(prev.name))) {
                newData.slug = createSlug(value);
            }
            return newData;
        });
    };

    const createSlug = (text) => {
        return text
            .toLowerCase()
            .replace(/[^\w ]+/g, '')
            .replace(/ +/g, '-');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setSubmitting(true);
        try {
            if (editingCategory) {
                await api.put(`/categories/${editingCategory.id}`, formData);
                toast.success('Kategori berhasil diperbarui');
            } else {
                await api.post('/categories', formData);
                toast.success('Kategori berhasil dibuat');
            }
            closeModal();
            fetchCategories();
        } catch (error) {
            console.error('Error saving category:', error);
            const errorMsg = error.response?.data?.error || 'Gagal menyimpan kategori';
            toast.error(errorMsg);
        } finally {
            setSubmitting(false);
        }
    };

    const handleDelete = async (id) => {
        if (!window.confirm('Apakah Anda yakin ingin menghapus kategori ini?')) return;

        try {
            await api.delete(`/categories/${id}`);
            toast.success('Kategori berhasil dihapus');
            fetchCategories();
        } catch (error) {
            console.error('Error deleting category:', error);
            const errorMsg = error.response?.data?.error || 'Gagal menghapus kategori';
            toast.error(errorMsg);
        }
    };

    const openModal = (category = null) => {
        if (category) {
            setEditingCategory(category);
            setFormData({ name: category.name, slug: category.slug });
        } else {
            setEditingCategory(null);
            setFormData({ name: '', slug: '' });
        }
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
        setEditingCategory(null);
        setFormData({ name: '', slug: '' });
    };

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />
            <div className="max-w-7xl mx-auto px-4 py-12">
                {/* Header */}
                <div className="flex justify-between items-center mb-8">
                    <div>
                        <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
                            Kelola Kategori
                        </h1>
                        <p className="text-gray-600 dark:text-gray-400">
                            Daftar kategori berita
                        </p>
                    </div>
                    <button
                        onClick={() => openModal()}
                        className="px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary-light transition-colors flex items-center"
                    >
                        <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                        </svg>
                        Tambah Kategori
                    </button>
                </div>

                {/* Table */}
                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden">
                    {loading ? (
                        <div className="p-6">
                            <LoadingSkeleton type="text" count={5} />
                        </div>
                    ) : categories.length > 0 ? (
                        <div className="overflow-x-auto">
                            <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                                <thead className="bg-gray-50 dark:bg-gray-900">
                                    <tr>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Nama</th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Slug</th>
                                        <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Aksi</th>
                                    </tr>
                                </thead>
                                <tbody className="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
                                    {categories.map((category) => (
                                        <tr key={category.id} className="hover:bg-gray-50 dark:hover:bg-gray-700">
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="text-sm font-medium text-gray-900 dark:text-white">
                                                    {category.name}
                                                </div>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                                                {category.slug}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                                <button
                                                    onClick={() => openModal(category)}
                                                    className="text-primary hover:text-primary-light mr-4"
                                                >
                                                    Edit
                                                </button>
                                                <button
                                                    onClick={() => handleDelete(category.id)}
                                                    className="text-red-600 hover:text-red-900 dark:text-red-400 dark:hover:text-red-300"
                                                >
                                                    Hapus
                                                </button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    ) : (
                        <div className="p-8 text-center text-gray-500 dark:text-gray-400">
                            Belum ada kategori.
                        </div>
                    )}
                </div>
            </div>

            {/* Modal */}
            {isModalOpen && (
                <div className="fixed inset-0 z-50 overflow-y-auto">
                    <div className="flex items-center justify-center min-h-screen px-4 pt-4 pb-20 text-center sm:block sm:p-0">
                        <div className="fixed inset-0 transition-opacity" aria-hidden="true">
                            <div className="absolute inset-0 bg-gray-500 opacity-75" onClick={closeModal}></div>
                        </div>

                        <span className="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>

                        <div className="inline-block align-bottom bg-white dark:bg-gray-800 rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                            <form onSubmit={handleSubmit}>
                                <div className="bg-white dark:bg-gray-800 px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                                    <h3 className="text-lg leading-6 font-medium text-gray-900 dark:text-white mb-4">
                                        {editingCategory ? 'Edit Kategori' : 'Tambah Kategori'}
                                    </h3>
                                    <div className="space-y-4">
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                                Nama Kategori
                                            </label>
                                            <input
                                                type="text"
                                                name="name"
                                                value={formData.name}
                                                onChange={handleInputChange}
                                                required
                                                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-primary focus:border-primary bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                                                placeholder="Contoh: Teknologi"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                                                Slug
                                            </label>
                                            <input
                                                type="text"
                                                name="slug"
                                                value={formData.slug}
                                                onChange={handleInputChange}
                                                required
                                                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-primary focus:border-primary bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                                                placeholder="Contoh: teknologi"
                                            />
                                        </div>
                                    </div>
                                </div>
                                <div className="bg-gray-50 dark:bg-gray-700 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                                    <button
                                        type="submit"
                                        disabled={submitting}
                                        className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-primary text-base font-medium text-white hover:bg-primary-light focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary sm:ml-3 sm:w-auto sm:text-sm disabled:opacity-50"
                                    >
                                        {submitting ? 'Menyimpan...' : 'Simpan'}
                                    </button>
                                    <button
                                        type="button"
                                        onClick={closeModal}
                                        className="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 dark:border-gray-600 shadow-sm px-4 py-2 bg-white dark:bg-gray-800 text-base font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
                                    >
                                        Batal
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};
