import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
    const currentYear = new Date().getFullYear();
    // Force 2025 as requested, or use dynamic if they want "2025" specifically. 
    // The user asked for "tahunnya 2025", so I will hardcode or ensure it shows 2025.
    // Let's use 2025 explicitly as requested.
    const displayYear = '2025';

    return (
        <footer className="bg-white dark:bg-gray-800 border-t dark:border-gray-700 mt-auto">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {/* Brand Section */}
                    <div className="col-span-1 md:col-span-1">
                        <Link to="/" className="flex items-center gap-2 mb-4">
                            <span className="text-2xl font-bold text-primary">EZ</span>
                            <span className="text-2xl font-bold text-secondary">News</span>
                        </Link>
                        <p className="text-gray-600 dark:text-gray-400 text-sm leading-relaxed">
                            Portal berita terkini dan terpercaya di Indonesia. Menyajikan informasi aktual, tajam, dan berimbang untuk Anda.
                        </p>
                    </div>

                    {/* Quick Links */}
                    <div>
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Menu</h3>
                        <ul className="space-y-2">
                            <li>
                                <Link to="/" className="text-gray-600 dark:text-gray-400 hover:text-primary dark:hover:text-primary transition-colors text-sm">
                                    Home
                                </Link>
                            </li>
                            <li>
                                <Link to="/news" className="text-gray-600 dark:text-gray-400 hover:text-primary dark:hover:text-primary transition-colors text-sm">
                                    Berita
                                </Link>
                            </li>
                            <li>
                                <Link to="/bookmarks" className="text-gray-600 dark:text-gray-400 hover:text-primary dark:hover:text-primary transition-colors text-sm">
                                    Bookmark
                                </Link>
                            </li>
                        </ul>
                    </div>

                    {/* Contact / Social */}
                    <div>
                        <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">Hubungi Kami</h3>
                        <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
                            <li className="flex items-center gap-2">
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                                </svg>
                                support@eznews.com
                            </li>
                            <li className="flex items-center gap-2">
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                </svg>
                                Jakarta, Indonesia
                            </li>
                        </ul>
                    </div>
                </div>

                <div className="border-t border-gray-200 dark:border-gray-700 mt-12 pt-8">
                    <p className="text-center text-gray-500 dark:text-gray-400 text-sm">
                        &copy; {displayYear} EzNews. All rights reserved.
                    </p>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
