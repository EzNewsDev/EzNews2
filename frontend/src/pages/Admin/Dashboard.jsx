import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../../components/Navbar';
import LoadingSkeleton from '../../components/LoadingSkeleton';
import api from '../../utils/api';
import { toast } from 'react-toastify';
import { format } from 'date-fns';
import { id as idLocale } from 'date-fns/locale/id';

const AdminDashboard = () => {
    const [stats, setStats] = useState({
        totalArticles: 0,
        totalCategories: 0,
        totalTags: 0,
        totalUsers: 0
    });
    const [recentArticles, setRecentArticles] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchDashboardData();
    }, []);

    const fetchDashboardData = async () => {
        try {
            // Fetch statistics
            const [articlesRes, categoriesRes, tagsRes, usersRes] = await Promise.all([
                api.get('/articles?limit=1'),
                api.get('/categories'),
                api.get('/tags'),
                api.get('/users')
            ]);

            setStats({
                totalArticles: articlesRes.data.total || 0,
                totalCategories: (categoriesRes.data.categories || categoriesRes.data)?.length || 0,
                totalTags: (tagsRes.data.tags || tagsRes.data)?.length || 0,
                totalUsers: (usersRes.data.users || usersRes.data)?.length || 0
            });

            // Fetch recent articles (last 5)
            const recentRes = await api.get('/articles?limit=5&page=1');
            setRecentArticles(recentRes.data.items || []);
        } catch (error) {
            console.error('Error fetching dashboard data:', error);
            toast.error('Gagal memuat data dashboard');
        } finally {
            setLoading(false);
        }
    };

    const handleDeleteArticle = async (articleId) => {
        if (!window.confirm('Apakah Anda yakin ingin menghapus artikel ini?')) return;

        try {
            await api.delete(`/articles/${articleId}`);
            setRecentArticles(recentArticles.filter(a => a.id !== articleId));
            setStats({ ...stats, totalArticles: stats.totalArticles - 1 });
            toast.success('Artikel berhasil dihapus');
        } catch (error) {
            console.error('Error deleting article:', error);
            toast.error('Gagal menghapus artikel');
        }
    };

    if (loading) {
        return (
            <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
                <Navbar />
                <div className="max-w-7xl mx-auto px-4 py-12">
                    <LoadingSkeleton type="card" count={4} />
                </div>
            </div>
        );
    }

    const statCards = [
        {
            title: 'Total Artikel',
            value: stats.totalArticles,
            icon: (
                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z" />
                </svg>
            ),
            color: 'bg-blue-500',
            link: '/admin/articles'
        },
        {
            title: 'Kategori',
            value: stats.totalCategories,
            icon: (
                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                </svg>
            ),
            color: 'bg-green-500',
            link: '/admin/categories'
        },
        {
            title: 'Tags',
            value: stats.totalTags,
            icon: (
                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                </svg>
            ),
            color: 'bg-purple-500',
            link: '/admin/tags'
        },
        {
            title: 'Pengguna',
            value: stats.totalUsers,
            icon: (
                <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
            ),
            color: 'bg-orange-500',
            link: '/admin/users'
        }
    ];

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />

            <div className="max-w-7xl mx-auto px-4 py-12">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-2">
                        Dashboard Admin
                    </h1>
                    <p className="text-gray-600 dark:text-gray-400">
                        Kelola konten dan pengguna EzNews
                    </p>
                </div>

                {/* Statistics Cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                    {statCards.map((card, index) => (
                        <Link
                            key={index}
                            to={card.link}
                            className="group bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1"
                        >
                            <div className="flex items-center justify-between mb-4">
                                <div className={`${card.color} text-white p-3 rounded-lg group-hover:scale-110 transition-transform`}>
                                    {card.icon}
                                </div>
                            </div>
                            <h3 className="text-gray-600 dark:text-gray-400 text-sm font-medium mb-1">
                                {card.title}
                            </h3>
                            <p className="text-3xl font-bold text-gray-900 dark:text-white">
                                {card.value}
                            </p>
                        </Link>
                    ))}
                </div>

                {/* Quick Actions */}
                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-8">
                    <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                        Aksi Cepat
                    </h2>
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <Link
                            to="/admin/articles/new"
                            className="flex items-center justify-center px-4 py-3 bg-primary text-white rounded-lg hover:bg-primary-light transition-colors"
                        >
                            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                            </svg>
                            Buat Artikel Baru
                        </Link>
                        <Link
                            to="/admin/categories"
                            className="flex items-center justify-center px-4 py-3 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
                        >
                            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                            </svg>
                            Kelola Kategori
                        </Link>
                        <Link
                            to="/admin/tags"
                            className="flex items-center justify-center px-4 py-3 bg-purple-500 text-white rounded-lg hover:bg-purple-600 transition-colors"
                        >
                            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                            </svg>
                            Kelola Tags
                        </Link>
                        <Link
                            to="/admin/articles"
                            className="flex items-center justify-center px-4 py-3 bg-orange-500 text-white rounded-lg hover:bg-orange-600 transition-colors"
                        >
                            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 10h16M4 14h16M4 18h16" />
                            </svg>
                            Lihat Semua Artikel
                        </Link>
                    </div>
                </div>

                {/* Recent Articles */}
                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden">
                    <div className="p-6 border-b border-gray-200 dark:border-gray-700">
                        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                            Artikel Terbaru
                        </h2>
                    </div>

                    {recentArticles.length > 0 ? (
                        <div className="overflow-x-auto">
                            <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                                <thead className="bg-gray-50 dark:bg-gray-900">
                                    <tr>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                            Judul
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                            Kategori
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                            Penulis
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                            Tanggal
                                        </th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                                            Aksi
                                        </th>
                                    </tr>
                                </thead>
                                <tbody className="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
                                    {recentArticles.map((article) => (
                                        <tr key={article.id} className="hover:bg-gray-50 dark:hover:bg-gray-700">
                                            <td className="px-6 py-4">
                                                <div className="text-sm font-medium text-gray-900 dark:text-white">
                                                    {article.title}
                                                </div>
                                            </td>
                                            <td className="px-6 py-4">
                                                <span className="px-2 py-1 text-xs font-semibold rounded-full bg-primary text-white">
                                                    {article.category?.name}
                                                </span>
                                            </td>
                                            <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                                                {article.author_name}
                                            </td>
                                            <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                                                {article.published_date
                                                    ? format(new Date(article.published_date), 'dd MMM yyyy', { locale: idLocale })
                                                    : 'Tanggal tidak tersedia'
                                                }
                                            </td>
                                            <td className="px-6 py-4 text-sm">
                                                <div className="flex items-center space-x-2">
                                                    <Link
                                                        to={`/admin/articles/edit/${article.id}`}
                                                        className="text-primary hover:text-primary-light"
                                                    >
                                                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                                                        </svg>
                                                    </Link>
                                                    <button
                                                        onClick={() => handleDeleteArticle(article.id)}
                                                        className="text-red-500 hover:text-red-700"
                                                    >
                                                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                                                        </svg>
                                                    </button>
                                                </div>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    ) : (
                        <div className="p-8 text-center text-gray-500 dark:text-gray-400">
                            Belum ada artikel
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default AdminDashboard;
