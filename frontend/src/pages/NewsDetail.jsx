import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import api from '../utils/api';
import { toast } from 'react-toastify';
import { format } from 'date-fns';
import { id as idLocale } from 'date-fns/locale/id';
import { useAuth } from '../contexts/AuthContext';

const NewsDetail = () => {
    const { id: articleId } = useParams();
    const navigate = useNavigate();
    const { isAuthenticated } = useAuth();

    const [article, setArticle] = useState(null);
    const [loading, setLoading] = useState(true);
    const [isBookmarked, setIsBookmarked] = useState(false);
    const [bookmarkId, setBookmarkId] = useState(null);

    // AI Summary state
    const [showSummaryPanel, setShowSummaryPanel] = useState(true);
    const [summaryFilters, setSummaryFilters] = useState({
        who: false,
        when: false,
        where: false,
        what: false,
        why: false,
        how: false
    });
    const [summary, setSummary] = useState('');
    const [summaryLoading, setSummaryLoading] = useState(false);

    // Fetch article
    useEffect(() => {
        const fetchArticle = async () => {
            try {
                const response = await api.get(`/articles/${articleId}`);
                setArticle(response.data);
                console.log('Article data:', response.data);
                console.log('Tags:', response.data.tags);

                // Check if bookmarked (if API provides this info)
                if (response.data.is_bookmarked) {
                    setIsBookmarked(true);
                    setBookmarkId(response.data.bookmark_id);
                }
            } catch (error) {
                console.error('Error fetching article:', error);
                toast.error('Gagal memuat artikel');
                navigate('/news');
            } finally {
                setLoading(false);
            }
        };

        fetchArticle();
    }, [articleId, isAuthenticated, navigate]);

    // Handle bookmark toggle
    const handleBookmark = async () => {
        if (!isAuthenticated) {
            toast.warning('Silakan login terlebih dahulu');
            navigate('/login');
            return;
        }

        try {
            if (isBookmarked) {
                // Remove bookmark
                await api.delete(`/bookmarks/${articleId}`);
                setIsBookmarked(false);
                setBookmarkId(null);
                toast.success('Bookmark dihapus');
            } else {
                // Add bookmark
                const response = await api.post('/bookmarks', { article_id: parseInt(articleId) });

                // Backend might return different formats
                const newBookmarkId = response.data.bookmark?.id || response.data.id || null;

                setIsBookmarked(true);
                setBookmarkId(newBookmarkId);
                toast.success('Artikel disimpan ke bookmark');
            }
        } catch (error) {
            console.error('Error toggling bookmark:', error);
            toast.error('Gagal mengubah status bookmark');
        }
    };

    // Handle filter toggle
    const handleFilterToggle = (filter) => {
        setSummaryFilters(prev => ({ ...prev, [filter]: !prev[filter] }));
    };

    // Generate AI Summary
    const handleGenerateSummary = async () => {
        const selectedFilters = Object.keys(summaryFilters).filter(key => summaryFilters[key]);

        if (selectedFilters.length === 0) {
            toast.warning('Pilih minimal satu filter');
            return;
        }

        setSummaryLoading(true);
        try {
            const response = await api.post('/summarize', {
                article_id: parseInt(articleId),
                filters: selectedFilters
            });
            // Backend returns the summary object directly
            setSummary(response.data);
        } catch (error) {
            console.error('Error generating summary:', error);
            toast.error('Gagal generate ringkasan');
        } finally {
            setSummaryLoading(false);
        }
    };

    // Handle export
    const handleExport = async (format) => {
        try {
            const response = await api.get(`/articles/${articleId}/export`, {
                params: { format },
                responseType: 'blob'
            });

            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', `${article.title}.${format}`);
            document.body.appendChild(link);
            link.click();
            link.remove();

            toast.success(`Artikel di-download sebagai ${format.toUpperCase()}`);
        } catch (error) {
            console.error('Error exporting article:', error);
            toast.error('Gagal download artikel');
        }
    };

    if (loading) {
        return (
            <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
                <Navbar />
                <div className="max-w-7xl mx-auto px-4 py-12">
                    <div className="animate-pulse">
                        <div className="h-8 bg-gray-300 dark:bg-gray-700 rounded w-3/4 mb-4"></div>
                        <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-1/2 mb-8"></div>
                        <div className="h-96 bg-gray-300 dark:bg-gray-700 rounded mb-8"></div>
                        <div className="space-y-3">
                            <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded"></div>
                            <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded"></div>
                            <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-5/6"></div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    if (!article) return null;

    const filterLabels = {
        who: 'Siapa',
        when: 'Kapan',
        where: 'Dimana',
        what: 'Apa',
        why: 'Mengapa',
        how: 'Bagaimana'
    };

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />

            <div className="max-w-7xl mx-auto px-4 py-8">
                {/* Breadcrumb */}
                <nav className="mb-6 text-sm">
                    <ol className="flex items-center space-x-2 text-gray-600 dark:text-gray-400">
                        <li><Link to="/" className="hover:text-primary">Home</Link></li>
                        <li>/</li>
                        <li><Link to="/news" className="hover:text-primary">Berita</Link></li>
                        <li>/</li>
                        <li className="text-gray-900 dark:text-white truncate">{article.category?.name}</li>
                    </ol>
                </nav>

                <div className="flex flex-col lg:flex-row gap-8">
                    {/* Main Content */}
                    <div className="flex-1">
                        {/* Article Header */}
                        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-8 mb-6">
                            <div className="mb-4">
                                <span className="px-3 py-1 bg-primary text-white text-sm font-semibold rounded-full">
                                    {article.category?.name}
                                </span>
                            </div>

                            <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
                                {article.title}
                            </h1>

                            <div className="flex items-center justify-between text-gray-600 dark:text-gray-400 text-sm mb-6">
                                <div className="flex items-center space-x-4">
                                    <div className="flex items-center space-x-2">
                                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                                        </svg>
                                        <span>{article.author_name}</span>
                                    </div>
                                    <div className="flex items-center space-x-2">
                                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                        </svg>
                                        <span>
                                            {article.published_date
                                                ? format(new Date(article.published_date), 'dd MMMM yyyy', { locale: idLocale })
                                                : 'Tanggal tidak tersedia'
                                            }
                                        </span>
                                    </div>
                                </div>

                                <div className="flex items-center space-x-2">
                                    {/* Bookmark Button */}
                                    <button
                                        onClick={handleBookmark}
                                        className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all duration-200 transform hover:scale-105 active:scale-95 shadow-sm hover:shadow-md ${isBookmarked
                                            ? 'bg-primary text-white hover:bg-primary-dark'
                                            : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-primary hover:text-white'
                                            }`}
                                    >
                                        <svg className="w-5 h-5" fill={isBookmarked ? 'currentColor' : 'none'} stroke="currentColor" viewBox="0 0 24 24">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
                                        </svg>
                                        <span className="hidden sm:inline">{isBookmarked ? 'Tersimpan' : 'Simpan'}</span>
                                    </button>

                                    {/* Export Buttons */}
                                    <div className="relative group">
                                        <button className="flex items-center space-x-2 px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-primary hover:text-white transition-all duration-200 transform hover:scale-105 active:scale-95 shadow-sm hover:shadow-md">
                                            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                            </svg>
                                            <span className="hidden sm:inline">Export</span>
                                        </button>
                                        <div className="hidden group-hover:block absolute right-0 top-full pt-2 w-32 z-10">
                                            <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg py-2">
                                                <button
                                                    onClick={() => handleExport('pdf')}
                                                    className="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                                                >
                                                    PDF
                                                </button>
                                                <button
                                                    onClick={() => handleExport('txt')}
                                                    className="block w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                                                >
                                                    TXT
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            {/* Article Image */}
                            {article.image_url && (
                                <img
                                    src={article.image_url}
                                    alt={article.title}
                                    className="w-full h-96 object-cover rounded-lg mb-6"
                                    onError={(e) => {
                                        e.target.style.display = 'none';
                                    }}
                                />
                            )}

                            {/* Article Content */}
                            <div className="prose dark:prose-invert max-w-none mb-8 text-gray-800 dark:text-gray-200 leading-relaxed whitespace-pre-line">
                                {article.content}
                            </div>

                            {/* Tags */}
                            {article.tags && article.tags.length > 0 && (
                                <div className="flex flex-wrap gap-2 mb-8">
                                    {article.tags.map(tag => (
                                        <span
                                            key={tag.id}
                                            className="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 text-sm rounded-full hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors cursor-default"
                                        >
                                            #{tag.name}
                                        </span>
                                    ))}
                                </div>
                            )}

                            <h3 className="text-xl font-bold text-gray-900 dark:text-white mt-8 mb-4 flex items-center justify-between">
                                AI Summary
                                <button
                                    onClick={() => setShowSummaryPanel(!showSummaryPanel)}
                                    className="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300"
                                >
                                    <svg className={`w-5 h-5 transition-transform ${showSummaryPanel ? 'transform rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                                    </svg>
                                </button>
                            </h3>
                        </div>

                        {showSummaryPanel && (
                            <>
                                <p className="text-sm text-gray-600 dark:text-gray-400 mb-4">
                                    Pilih filter untuk mendapatkan ringkasan AI yang disesuaikan:
                                </p>

                                {/* Filter Buttons */}
                                <div className="grid grid-cols-2 gap-2 mb-4">
                                    {Object.keys(filterLabels).map((filter) => (
                                        <button
                                            key={filter}
                                            onClick={() => handleFilterToggle(filter)}
                                            className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${summaryFilters[filter]
                                                ? 'bg-primary text-white'
                                                : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
                                                }`}
                                        >
                                            {filterLabels[filter]}
                                        </button>
                                    ))}
                                </div>

                                {/* Generate Button */}
                                <button
                                    onClick={handleGenerateSummary}
                                    disabled={summaryLoading}
                                    className="w-full bg-primary-light text-white px-4 py-3 rounded-lg font-medium hover:bg-primary transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
                                >
                                    {summaryLoading ? (
                                        <>
                                            <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                            </svg>
                                            Generating...
                                        </>
                                    ) : (
                                        <>
                                            <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                                            </svg>
                                            Generate Ringkasan
                                        </>
                                    )}
                                </button>

                                {/* Summary Display */}
                                {summary && (
                                    <div className="mt-4 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-800">
                                        <h4 className="font-semibold text-gray-900 dark:text-white mb-3">Ringkasan AI:</h4>
                                        <div className="space-y-3">
                                            {typeof summary === 'object' ? (
                                                Object.entries(summary).map(([key, value]) => (
                                                    <div key={key}>
                                                        <span className="font-bold text-primary capitalize">{filterLabels[key] || key}: </span>
                                                        <span className="text-sm text-gray-700 dark:text-gray-300 leading-relaxed">
                                                            {value}
                                                        </span>
                                                    </div>
                                                ))
                                            ) : (
                                                <p className="text-sm text-gray-700 dark:text-gray-300 leading-relaxed whitespace-pre-line">
                                                    {summary}
                                                </p>
                                            )}
                                        </div>
                                    </div>
                                )}
                            </>
                        )}
                    </div>
                </div>
            </div>
            <Footer />
        </div >

    );
};

export default NewsDetail;
