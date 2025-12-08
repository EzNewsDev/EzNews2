// Create stub pages for the application
// These are functional placeholders that can be enhanced later

import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../utils/api';
import { toast } from 'react-toastify';
import Navbar from '../components/Navbar';
import { format } from 'date-fns';

const Home = () => {
    const [articles, setArticles] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchArticles();
    }, []);

    const fetchArticles = async () => {
        try {
            const response = await api.get('/articles?page=1&page_size=6');
            setArticles(response.data.items);
        } catch (error) {
            toast.error('Gagal memuat berita');
        } finally {
            setLoading(false);
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

                {/* Top News */}
                <section>
                    <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-6">
                        Berita Terbaru
                    </h2>

                    {loading ? (
                        <div className="flex justify-center py-12">
                            <div className="spinner border-4 border-primary-light border-t-transparent rounded-full w-12 h-12"></div>
                        </div>
                    ) : (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {articles.map((article) => (
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
                            ))}
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

            <footer className="bg-white dark:bg-gray-800 border-t dark:border-gray-700 mt-12">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
                    <p className="text-center text-gray-600 dark:text-gray-400">
                        © 2024 EzNews. All rights reserved.
                    </p>
                </div>
            </footer>
        </div>
    );
};

export default Home;
