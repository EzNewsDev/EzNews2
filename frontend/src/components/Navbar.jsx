import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { useTheme } from '../contexts/ThemeContext';
import { FaSun, FaMoon, FaBars, FaTimes } from 'react-icons/fa';
import Logo from './Logo';

const Navbar = () => {
    const { user, logout, isAuthenticated, isAdmin } = useAuth();
    const { theme, toggleTheme } = useTheme();
    const [mobileMenuOpen, setMobileMenuOpen] = React.useState(false);

    return (
        <nav className="bg-white dark:bg-gray-900 shadow-md sticky top-0 z-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                    <div className="flex items-center">
                        <Link to="/" className="flex items-center">
                            <Logo />
                        </Link>
                    </div>

                    {/* Desktop Menu */}
                    <div className="hidden md:flex items-center space-x-6">
                        <Link to="/" className="text-gray-700 dark:text-gray-300 hover:text-primary dark:hover:text-primary-light">
                            Home
                        </Link>
                        <Link to="/news" className="text-gray-700 dark:text-gray-300 hover:text-primary dark:hover:text-primary-light">
                            Berita
                        </Link>
                        {isAuthenticated && (
                            <Link to="/bookmarks" className="text-gray-700 dark:text-gray-300 hover:text-primary dark:hover:text-primary-light">
                                Bookmark
                            </Link>
                        )}
                        {isAdmin && (
                            <Link to="/admin" className="text-gray-700 dark:text-gray-300 hover:text-primary dark:hover:text-primary-light">
                                Admin
                            </Link>
                        )}

                        <button onClick={toggleTheme} className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800">
                            {theme === 'light' ? <FaMoon className="text-gray-600" /> : <FaSun className="text-yellow-400" />}
                        </button>

                        {isAuthenticated ? (
                            <div className="flex items-center space-x-4">
                                <Link to="/profile" className="text-gray-700 dark:text-gray-300 hover:text-primary dark:hover:text-primary-light">
                                    {user?.full_name}
                                </Link>
                                <button
                                    onClick={logout}
                                    className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
                                >
                                    Logout
                                </button>
                            </div>
                        ) : (
                            <div className="flex items-center space-x-4">
                                <Link to="/login" className="text-gray-700 dark:text-gray-300 hover:text-primary dark:hover:text-primary-light">
                                    Login
                                </Link>
                                <Link to="/register" className="px-4 py-2 bg-primary text-white rounded hover:bg-primary-dark">
                                    Register
                                </Link>
                            </div>
                        )}
                    </div>

                    {/* Mobile menu button */}
                    <div className="md:hidden flex items-center">
                        <button onClick={() => setMobileMenuOpen(!mobileMenuOpen)} className="p-2">
                            {mobileMenuOpen ? <FaTimes className="text-2xl" /> : <FaBars className="text-2xl" />}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            {mobileMenuOpen && (
                <div className="md:hidden bg-white dark:bg-gray-900 border-t dark:border-gray-700 px-4 py-4 space-y-3">
                    <Link to="/" className="block text-gray-700 dark:text-gray-300 hover:text-primary">Home</Link>
                    <Link to="/news" className="block text-gray-700 dark:text-gray-300 hover:text-primary">Berita</Link>
                    {isAuthenticated && <Link to="/bookmarks" className="block text-gray-700 dark:text-gray-300 hover:text-primary">Bookmark</Link>}
                    {isAdmin && <Link to="/admin" className="block text-gray-700 dark:text-gray-300 hover:text-primary">Admin</Link>}
                    {isAuthenticated ? (
                        <>
                            <Link to="/profile" className="block text-gray-700 dark:text-gray-300 hover:text-primary">{user?.full_name}</Link>
                            <button onClick={logout} className="w-full text-left text-red-600 hover:text-red-700">Logout</button>
                        </>
                    ) : (
                        <>
                            <Link to="/login" className="block text-gray-700 dark:text-gray-300 hover:text-primary">Login</Link>
                            <Link to="/register" className="block text-primary hover:text-primary-dark">Register</Link>
                        </>
                    )}
                </div>
            )}
        </nav>
    );
};

export default Navbar;
