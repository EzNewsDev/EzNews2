// Create stub pages for the application
// These are functional placeholders that can be enhanced later

import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../utils/api';
import { toast } from 'react-toastify';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { format } from 'date-fns';

const Home = () => {
    const [articles, setArticles] = useState([]);
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchInitialData = async () => {
            try {
                const categoriesRes = await api.get('/categories');
                // Handle different category response structures
                const categoriesData = categoriesRes.data.categories || categoriesRes.data;
                setCategories(Array.isArray(categoriesData) ? categoriesData : []);
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        };
        fetchInitialData();
    }, []);

    useEffect(() => {
        const fetchArticles = async () => {
            setLoading(true);
            try {
                const params = {
                    page: 1,
                    page_size: 6,
                    ...(selectedCategory && { category_id: selectedCategory })
                };
                const response = await api.get('/articles', { params });
                setArticles(response.data.items);
            } catch (error) {
                console.error('Error fetching articles:', error);
                toast.error('Gagal memuat berita');
            } finally {
                setLoading(false);
            }
        };

        fetchArticles();
    }, [selectedCategory]);

    const handleCategoryClick = (categoryId) => {
        if (selectedCategory === categoryId) {
            setSelectedCategory(null); // Toggle off if already selected
        } else {
            setSelectedCategory(categoryId);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />

            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                {/* Hero */}
                <div className="text-center mb-12">
                    <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-4">
                        Selamat Datang di <span className="text-primary">EZ</span><span className="text-secondary">News</span>
                    </h1>
                    <p className="text-xl text-gray-600 dark:text-gray-400">
                        Portal Berita Terkini Indonesia
                    </p>
                </div>

                {/* Trending Topics */}
                <section className="mb-12">
                    <div className="flex items-center gap-2 mb-6">
                        <span className="text-2xl">🔥</span>
                        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                            Topik Trending
                        </h2>
                    </div>

                    <div className="flex flex-wrap gap-3">
                        <button
                            onClick={() => setSelectedCategory(null)}
                            className={`px-6 py-2 border rounded-full font-medium transition-all duration-200 shadow-sm hover:shadow-md ${selectedCategory === null
                                ? 'bg-primary text-white border-primary'
                                : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'
                                }`}
                        >
                            Semua
                        </button>
                        {categories.slice(0, 3).map((category) => (
                            <button
                                key={category.id}
                                onClick={() => handleCategoryClick(category.id)}
                                className={`px-6 py-2 border rounded-full font-medium transition-all duration-200 shadow-sm hover:shadow-md ${selectedCategory === category.id
                                    ? 'bg-primary text-white border-primary'
                                    : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700'
                                    }`}
                            >
                                {category.name}
                                {category.article_count !== undefined && (
                                    <span className="ml-2 text-xs opacity-75">({category.article_count})</span>
                                )}
                            </button>
                        ))}
                    </div>
                </section>

                {/* Top News */}
                <section>
                    <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-6">
                        {selectedCategory
                            ? `${categories.find(c => c.id === selectedCategory)?.name || 'Terbaru'}`
                            : 'Berita Terbaru'}
                    </h2>

                    {loading ? (
                        <div className="flex justify-center py-12">
                            <div className="spinner border-4 border-primary-light border-t-transparent rounded-full w-12 h-12"></div>
                        </div>
                    ) : (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {articles.length > 0 ? (
                                articles.map((article) => (
                                    <Link
                                        key={article.id}
                                        to={`/news/${article.id}`}
                                        className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:shadow-xl transition-shadow"
                                    >
                                        {article.image_url && (
                                            <img
                                                src={article.image_url}
                                                alt={article.title}
                                                className="w-full h-48 object-cover"
                                            />
                                        )}
                                        <div className="p-4">
                                            <div className="flex items-center gap-2 mb-2">
                                                <span className="text-xs bg-primary text-white px-2 py-1 rounded">
                                                    {article.category?.name}
                                                </span>
                                                <span className="text-xs text-gray-500 dark:text-gray-400">
                                                    {format(new Date(article.published_date), 'dd MMM yyyy')}
                                                </span>
                                            </div>
                                            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2 line-clamp-2">
                                                {article.title}
                                            </h3>
                                            <p className="text-sm text-gray-600 dark:text-gray-400">
                                                {article.author_name}
                                            </p>
                                        </div>
                                    </Link>
                                ))
                            ) : (
                                <div className="col-span-full text-center py-12 text-gray-500 dark:text-gray-400">
                                    Tidak ada berita ditemukan untuk kategori ini.
                                </div>
                            )}
                        </div>
                    )}

                    <div className="text-center mt-8">
                        <Link
                            to="/news"
                            className="inline-block px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary-dark transition-colors"
                        >
                            Lihat Semua Berita
                        </Link>
                    </div>
                </section>
            </main>

            <Footer />
        </div>
    );
};

export default Home;
