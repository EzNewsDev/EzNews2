import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { toast } from 'react-toastify';
import api from '../../utils/api';
import DecoPattern from '../../components/DecoPattern';
import Logo from '../../components/Logo';

const ForgotPassword = () => {
    const [email, setEmail] = useState('');
    const [resetToken, setResetToken] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [step, setStep] = useState(1); // 1: email, 2: reset
    const [loading, setLoading] = useState(false);

    const handleRequestReset = async (e) => {
        e.preventDefault();

        if (!email) {
            toast.error('Email harus diisi');
            return;
        }

        setLoading(true);
        try {
            const response = await api.post('/auth/forgot-password', { email });
            toast.success('Token reset password telah dikirim!');
            // In development, show the token
            if (response.data.reset_token) {
                setResetToken(response.data.reset_token);
                toast.info(`Token Anda: ${response.data.reset_token}`, { autoClose: 10000 });
            }
            setStep(2);
        } catch (error) {
            toast.error(error.response?.data?.error || 'Gagal mengirim permintaan reset');
        } finally {
            setLoading(false);
        }
    };

    const handleResetPassword = async (e) => {
        e.preventDefault();

        if (!resetToken || !newPassword || !confirmPassword) {
            toast.error('Semua field harus diisi');
            return;
        }

        if (newPassword.length < 8) {
            toast.error('Password minimal 8 karakter');
            return;
        }

        if (newPassword !== confirmPassword) {
            toast.error('Password dan konfirmasi tidak cocok');
            return;
        }

        setLoading(true);
        try {
            await api.post('/auth/reset-password', {
                token: resetToken,
                new_password: newPassword,
                confirm_password: confirmPassword
            });
            toast.success('Password berhasil direset! Silakan login.');
            setTimeout(() => {
                window.location.href = '/login';
            }, 2000);
        } catch (error) {
            toast.error(error.response?.data?.error || 'Gagal mereset password');
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
            <div className="flex-1 flex items-center justify-center px-4 sm:px-6 lg:px-8 relative z-10">
                <div className="max-w-md w-full space-y-8">
                    {/* Logo */}
                    <div className="text-center">
                        <Logo />
                    </div>

                    {/* Title */}
                    <div className="text-center">
                        <h2 className="text-3xl font-bold text-gray-900 dark:text-white">
                            Forgot Password, Buddy?
                        </h2>
                        <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
                            Fill the forms below...
                        </p>
                    </div>

                    {/* Step 1: Request Reset */}
                    {step === 1 && (
                        <form className="mt-8 space-y-6" onSubmit={handleRequestReset}>
                            <div>
                                <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Email
                                </label>
                                <input
                                    id="email"
                                    name="email"
                                    type="email"
                                    required
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                    placeholder="johndoe@binus.ac.id"
                                />
                            </div>

                            <div>
                                <button
                                    type="submit"
                                    disabled={loading}
                                    className="w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-light disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                                >
                                    {loading ? 'Sending...' : 'Send Reset Token'}
                                </button>
                            </div>

                            <div className="text-center text-sm">
                                <Link to="/login" className="font-medium text-primary-light hover:text-primary">
                                    Back to Login
                                </Link>
                            </div>
                        </form>
                    )}

                    {/* Step 2: Reset Password */}
                    {step === 2 && (
                        <form className="mt-8 space-y-6" onSubmit={handleResetPassword}>
                            <div className="space-y-4">
                                <div>
                                    <label htmlFor="token" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                        Reset Token
                                    </label>
                                    <input
                                        id="token"
                                        name="token"
                                        type="text"
                                        required
                                        value={resetToken}
                                        onChange={(e) => setResetToken(e.target.value)}
                                        className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                        placeholder="Enter token from email"
                                    />
                                </div>

                                <div>
                                    <label htmlFor="newPassword" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                        New Password
                                    </label>
                                    <input
                                        id="newPassword"
                                        name="newPassword"
                                        type="password"
                                        required
                                        value={newPassword}
                                        onChange={(e) => setNewPassword(e.target.value)}
                                        className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                        placeholder="secretCode567"
                                    />
                                </div>

                                <div>
                                    <label htmlFor="confirmPassword" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                        Confirm New Password
                                    </label>
                                    <input
                                        id="confirmPassword"
                                        name="confirmPassword"
                                        type="password"
                                        required
                                        value={confirmPassword}
                                        onChange={(e) => setConfirmPassword(e.target.value)}
                                        className="appearance-none relative block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white bg-white dark:bg-gray-800 rounded focus:outline-none focus:ring-2 focus:ring-primary-light focus:border-transparent"
                                        placeholder="secretCode567"
                                    />
                                </div>
                            </div>

                            <div>
                                <button
                                    type="submit"
                                    disabled={loading}
                                    className="w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded text-white bg-primary hover:bg-primary-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-light disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                                >
                                    {loading ? 'Resetting...' : 'Reset Password'}
                                </button>
                            </div>

                            <div className="text-center text-sm">
                                <button
                                    type="button"
                                    onClick={() => setStep(1)}
                                    className="font-medium text-primary-light hover:text-primary"
                                >
                                    Request new token
                                </button>
                            </div>
                        </form>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ForgotPassword;
