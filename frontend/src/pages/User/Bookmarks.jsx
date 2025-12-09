import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../../components/Navbar';
import NewsCard from '../../components/NewsCard';
import api from '../../utils/api';
import { toast } from 'react-toastify';

const Bookmarks = () => {
    const [bookmarks, setBookmarks] = useState([]);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
        fetchBookmarks();
    }, []);

    const fetchBookmarks = async () => {
        setLoading(true);
        try {
            const response = await api.get('/bookmarks');
            // Backend returns {bookmarks: [...]} not direct array
            const bookmarksData = response.data.bookmarks || [];
            setBookmarks(bookmarksData);
        } catch (error) {
            console.error('Error fetching bookmarks:', error);
            if (error.response?.status === 401) {
                toast.error('Silakan login terlebih dahulu');
                navigate('/login');
            } else {
                toast.error('Gagal memuat bookmark');
            }
        } finally {
            setLoading(false);
        }
    };

    const handleRemoveBookmark = async (bookmark) => {
        console.log('[DELETE] Starting delete for bookmark:', bookmark);
        console.log('[DELETE] Article ID:', bookmark.article?.id);
        console.log('[DELETE] Bookmark ID:', bookmark.id);

        try {
            console.log('[DELETE] Calling API DELETE /bookmarks/' + bookmark.article.id);
            const response = await api.delete(`/bookmarks/${bookmark.article.id}`);
            console.log('[DELETE] API Response:', response);

            console.log('[DELETE] Filtering bookmarks - Before:', bookmarks.length);
            const newBookmarks = bookmarks.filter(b => b.id !== bookmark.id);
            console.log('[DELETE] Filtering bookmarks - After:', newBookmarks.length);

            setBookmarks(newBookmarks);
            toast.success('Bookmark dihapus');
        } catch (error) {
            console.error('[DELETE] Error removing bookmark:', error);
            console.error('[DELETE] Error response:', error.response);
            toast.error('Gagal menghapus bookmark');
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />

            <div className="max-w-7xl mx-auto px-4 py-12">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-2">
                        Bookmark Saya
                    </h1>
                    <p className="text-gray-600 dark:text-gray-400">
                        Artikel yang telah Anda simpan untuk dibaca nanti
                    </p>
                </div>

                {/* Loading State */}
                {loading ? (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {[...Array(3)].map((_, index) => (
                            <div key={index} className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden animate-pulse">
                                <div className="h-48 bg-gray-300 dark:bg-gray-700"></div>
                                <div className="p-5 space-y-3">
                                    <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-3/4"></div>
                                    <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded"></div>
                                    <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-5/6"></div>
                                </div>
                            </div>
                        ))}
                    </div>
                ) : bookmarks.length > 0 ? (
                    <>
                        {/* Bookmarks Grid */}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {bookmarks.map((bookmark) => (
                                <div key={bookmark.id} className="relative">
                                    <NewsCard article={bookmark.article} />

                                    {/* Remove Button Overlay */}
                                    <button
                                        onClick={() => handleRemoveBookmark(bookmark)}
                                        className="absolute top-3 right-3 bg-red-500 hover:bg-red-600 text-white p-2 rounded-full shadow-lg transition-colors z-10"
                                        title="Hapus Bookmark"
                                    >
                                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                                        </svg>
                                    </button>
                                </div>
                            ))}
                        </div>

                        {/* Summary */}
                        <div className="mt-8 text-center text-gray-600 dark:text-gray-400">
                            Total {bookmarks.length} artikel tersimpan
                        </div>
                    </>
                ) : (
                    /* Empty State */
                    <div className="text-center py-16">
                        <svg
                            className="mx-auto h-24 w-24 text-gray-400 dark:text-gray-600 mb-4"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth={1.5}
                                d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"
                            />
                        </svg>
                        <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                            Belum ada bookmark
                        </h3>
                        <p className="text-gray-600 dark:text-gray-400 mb-6">
                            Mulai bookmark artikel favorit Anda untuk dibaca nanti
                        </p>
                        <button
                            onClick={() => navigate('/news')}
                            className="inline-flex items-center px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary-light transition-colors"
                        >
                            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                            Jelajahi Berita
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Bookmarks;
