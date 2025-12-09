import React, { useState, useEffect, useCallback } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import NewsCard from '../components/NewsCard';
import SearchBar from '../components/SearchBar';
import Pagination from '../components/Pagination';
import api from '../utils/api';
import { toast } from 'react-toastify';

const NewsList = () => {
    const [articles, setArticles] = useState([]);
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');
    const [selectedCategory, setSelectedCategory] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);
    const limit = 9; // Articles per page

    // Fetch categories on mount
    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const response = await api.get('/categories');
                const categoriesData = response.data.categories || response.data;
                setCategories(Array.isArray(categoriesData) ? categoriesData : []);
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        };
        fetchCategories();
    }, []);

    // Fetch articles with filters
    const fetchArticles = useCallback(async () => {
        setLoading(true);
        try {
            const params = {
                page: currentPage,
                limit,
                search: searchTerm,
                category_id: selectedCategory
            };

            const response = await api.get('/articles', { params });
            setArticles(response.data.items);
            setTotalPages(response.data.pages);
        } catch (error) {
            console.error('Error fetching articles:', error);
            toast.error('Gagal memuat berita. Silakan coba lagi.');
        } finally {
            setLoading(false);
        }
    }, [currentPage, searchTerm, selectedCategory]);

    // Fetch articles when filters change
    useEffect(() => {
        fetchArticles();
    }, [fetchArticles]);

    // Reset to page 1 when search/category changes
    useEffect(() => {
        if (currentPage !== 1) {
            setCurrentPage(1);
        }
    }, [searchTerm, selectedCategory]);

    const handleSearch = useCallback((term) => {
        setSearchTerm(term);
    }, []);

    const handleCategoryChange = useCallback((categoryId) => {
        setSelectedCategory(categoryId);
    }, []);

    const handlePageChange = (page) => {
        setCurrentPage(page);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />

            <div className="max-w-7xl mx-auto px-4 py-12">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-2">
                        Daftar Berita
                    </h1>
                    <p className="text-gray-600 dark:text-gray-400">
                        Temukan berita terkini dari berbagai kategori
                    </p>
                </div>

                {/* Search and Filter */}
                <SearchBar
                    onSearch={handleSearch}
                    onCategoryChange={handleCategoryChange}
                    categories={categories}
                    loading={loading}
                />



                {/* Loading State */}
                {loading ? (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {[...Array(6)].map((_, index) => (
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
                ) : articles.length > 0 ? (
                    <>
                        {/* Articles Grid */}
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {articles.map((article) => (
                                <NewsCard key={article.id} article={article} />
                            ))}
                        </div>

                        {/* Pagination */}
                        <Pagination
                            currentPage={currentPage}
                            totalPages={totalPages}
                            onPageChange={handlePageChange}
                        />
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
                                d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"
                            />
                        </svg>
                        <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                            Tidak ada berita ditemukan
                        </h3>
                        <p className="text-gray-600 dark:text-gray-400">
                            Coba ubah kata kunci pencarian atau filter kategori
                        </p>
                    </div>
                )}
            </div>
            <Footer />
        </div>
    );
};

export default NewsList;
