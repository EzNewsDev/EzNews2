import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import { toast } from 'react-toastify';
import DecoPattern from '../../components/DecoPattern';
import logo from '../../assets/logo_EzNews_new.png';

const Register = () => {
    const navigate = useNavigate();
    const { register } = useAuth();
    const [formData, setFormData] = useState({
        full_name: '',
        email: '',
        password: '',
        confirm_password: '',
    });
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setFormData(prev => ({
            ...prev,
            [e.target.name]: e.target.value
        }));
    };

    const validateForm = () => {
        if (!formData.full_name || formData.full_name.length < 2) {
            toast.error('Nama lengkap minimal 2 karakter');
            return false;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(formData.email)) {
            toast.error('Format email tidak valid');
            return false;
        }

        if (formData.password.length < 8) {
            toast.error('Password minimal 8 karakter');
            return false;
        }
        if (!/(?=.*[a-z])/.test(formData.password)) {
            toast.error('Password harus mengandung huruf kecil');
            return false;
        }
        if (!/(?=.*[A-Z])/.test(formData.password)) {
            toast.error('Password harus mengandung huruf besar');
            return false;
        }
        if (!/(?=.*\d)/.test(formData.password)) {
            toast.error('Password harus mengandung angka');
            return false;
        }
        if (!/(?=.*[@$!%*?&])/.test(formData.password)) {
            toast.error('Password harus mengandung karakter spesial (@$!%*?&)');
            return false;
        }

        if (formData.password !== formData.confirm_password) {
            toast.error('Password dan konfirmasi password tidak cocok');
            return false;
        }

        return true;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!validateForm()) return;

        setLoading(true);
        try {
            await register(formData);
            toast.success('Registrasi berhasil! Selamat datang di EzNews!');
            navigate('/');
        } catch (error) {
            const errorMsg = error.response?.data?.errors?.join(', ') || error.response?.data?.error || 'Registrasi gagal';
            toast.error(errorMsg);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-white dark:bg-gray-900 flex relative overflow-hidden">
            {/* Left Pattern */}
            <DecoPattern position="left" />

            {/* Right Pattern */}
            <DecoPattern position="right" />

            {/* Main Content */}
            <div className="flex-1 flex items-center justify-center px-4 sm:px-6 lg:px-8 relative z-10 py-12">
                <div className="max-w-md w-full space-y-8">
                    {/* Logo */}
                    <div className="text-center">
                        <img src={logo} alt="EzNews Logo" className="h-32 w-auto mx-auto" />
                    </div>

                    {/* Title */}
                    <div className="text-center">
                        <h2 className="text-3xl font-bold text-gray-900 dark:text-white">
                            Hi, New Guy!
                        </h2>
                    </div>

                    {/* Form */}
                    <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                        <div className="space-y-4">
                            {/* Full Name */}
                            <div>
                                <label htmlFor="full_name" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Full Name
                                </label>
                                <input
                                    id="full_name"
                                    name="full_name"
                                    type="text"
                                    required
                                    value={formData.full_name}
                                    onChange={handleChange}
                                    className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                    placeholder="John Doe"
                                />
                            </div>

                            {/* Email */}
                            <div>
                                <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Email
                                </label>
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    autoComplete="email"
                                    required
                                    value={formData.email}
                                    onChange={handleChange}
                                    className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                    placeholder="johndoe@binus.ac.id"
                                />
                            </div>

                            {/* Password */}
                            <div>
                                <label htmlFor="password" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Password
                                </label>
                                <input
                                    id="password"
                                    name="password"
                                    type="password"
                                    required
                                    value={formData.password}
                                    onChange={handleChange}
                                    className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                    placeholder="secretCode567"
                                />
                                <p className="mt-1 text-xs text-gray-500 dark:text-gray-400">
                                    Min. 8 karakter, 1 huruf besar, 1 huruf kecil, 1 angka, 1 karakter spesial (@$!%*?&)
                                </p>
                            </div>

                            {/* Confirm Password */}
                            <div>
                                <label htmlFor="confirm_password" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Confirm Password
                                </label>
                                <input
                                    id="confirm_password"
                                    name="confirm_password"
                                    type="password"
                                    required
                                    value={formData.confirm_password}
                                    onChange={handleChange}
                                    className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                    placeholder="secretCode567"
                                />
                            </div>
                        </div>

                        {/* Submit Button */}
                        <div>
                            <button
                                type="submit"
                                disabled={loading}
                                className="w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-light disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            >
                                {loading ? 'Creating Account...' : 'Create Account'}
                            </button>
                        </div>

                        {/* Divider */}
                        <div className="relative">
                            <div className="absolute inset-0 flex items-center">
                                <div className="w-full border-t border-gray-300 dark:border-gray-600"></div>
                            </div>
                            <div className="relative flex justify-center text-sm">
                                <span className="px-2 bg-white dark:bg-gray-900 text-gray-500">Or sign up with</span>
                            </div>
                        </div>

                        {/* Social Login */}
                        <div className="grid grid-cols-2 gap-3">
                            <button
                                type="button"
                                className="flex items-center justify-center gap-2 py-2 px-4 border border-gray-300 dark:border-gray-600 rounded shadow-sm bg-white dark:bg-gray-800 text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
                            >
                                <img src="https://www.google.com/favicon.ico" alt="Google" className="w-5 h-5" />
                                Google
                            </button>
                            <button
                                type="button"
                                className="flex items-center justify-center gap-2 py-2 px-4 border border-gray-300 dark:border-gray-600 rounded shadow-sm bg-white dark:bg-gray-800 text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
                            >
                                <img src="https://www.facebook.com/favicon.ico" alt="Facebook" className="w-5 h-5" />
                                Facebook
                            </button>
                        </div>

                        {/* Login Link */}
                        <div className="text-center text-sm">
                            <span className="text-gray-600 dark:text-gray-400">Already have an account? </span>
                            <Link to="/login" className="font-medium text-primary-light hover:text-primary">
                                Login here!
                            </Link>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Register;
