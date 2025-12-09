import React, { useState, useEffect } from 'react';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import api from '../../utils/api';
import { toast } from 'react-toastify';
import { useAuth } from '../../contexts/AuthContext';

const Profile = () => {
    const { user, updateUser } = useAuth();
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);

    // Profile Form State
    const [profileData, setProfileData] = useState({
        full_name: '',
        email: ''
    });

    // Password Form State
    const [passwordData, setPasswordData] = useState({
        current_password: '',
        new_password: '',
        confirm_password: ''
    });
    const [passwordErrors, setPasswordErrors] = useState({});

    useEffect(() => {
        fetchProfile();
    }, []);

    const fetchProfile = async () => {
        try {
            const response = await api.get('/users/profile');
            setProfileData({
                full_name: response.data.full_name || '',
                email: response.data.email || ''
            });
        } catch (error) {
            console.error('Error fetching profile:', error);
            toast.error('Gagal memuat profil');
        } finally {
            setLoading(false);
        }
    };

    const handleProfileChange = (e) => {
        setProfileData({
            ...profileData,
            [e.target.name]: e.target.value
        });
    };

    const handleProfileSubmit = async (e) => {
        e.preventDefault();
        setSaving(true);

        try {
            const response = await api.put('/users/profile', {
                full_name: profileData.full_name
            });

            // Update user in auth context
            updateUser({ full_name: profileData.full_name });

            toast.success('Profil berhasil diperbarui');
        } catch (error) {
            console.error('Error updating profile:', error);
            toast.error(error.response?.data?.message || 'Gagal memperbarui profil');
        } finally {
            setSaving(false);
        }
    };

    const handlePasswordChange = (e) => {
        setPasswordData({
            ...passwordData,
            [e.target.name]: e.target.value
        });

        // Clear errors for this field
        if (passwordErrors[e.target.name]) {
            setPasswordErrors({
                ...passwordErrors,
                [e.target.name]: ''
            });
        }
    };

    const validatePassword = () => {
        const errors = {};

        if (!passwordData.current_password) {
            errors.current_password = 'Password saat ini harus diisi';
        }

        if (!passwordData.new_password) {
            errors.new_password = 'Password baru harus diisi';
        } else if (passwordData.new_password.length < 8) {
            errors.new_password = 'Password minimal 8 karakter';
        } else if (!/(?=.*[a-z])/.test(passwordData.new_password)) {
            errors.new_password = 'Password harus mengandung huruf kecil';
        } else if (!/(?=.*[A-Z])/.test(passwordData.new_password)) {
            errors.new_password = 'Password harus mengandung huruf besar';
        } else if (!/(?=.*\d)/.test(passwordData.new_password)) {
            errors.new_password = 'Password harus mengandung angka';
        } else if (!/(?=.*[@$!%*?&])/.test(passwordData.new_password)) {
            errors.new_password = 'Password harus mengandung karakter spesial (@$!%*?&)';
        }

        if (!passwordData.confirm_password) {
            errors.confirm_password = 'Konfirmasi password harus diisi';
        } else if (passwordData.new_password !== passwordData.confirm_password) {
            errors.confirm_password = 'Password tidak cocok';
        }

        return errors;
    };

    const handlePasswordSubmit = async (e) => {
        e.preventDefault();

        const errors = validatePassword();
        if (Object.keys(errors).length > 0) {
            setPasswordErrors(errors);
            return;
        }

        setSaving(true);
        try {
            const payload = {
                old_password: passwordData.current_password,
                new_password: passwordData.new_password,
                confirm_new_password: passwordData.confirm_password
            };
            console.log('Sending payload:', payload);

            await api.put('/users/change-password', payload);

            // Clear form
            setPasswordData({
                current_password: '',
                new_password: '',
                confirm_password: ''
            });
            setPasswordErrors({});

            toast.success('Password berhasil diubah');
        } catch (error) {
            console.error('Error changing password:', error);
            toast.error(error.response?.data?.message || 'Gagal mengubah password');
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return (
            <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
                <Navbar />
                <div className="max-w-4xl mx-auto px-4 py-12">
                    <div className="animate-pulse">
                        <div className="h-8 bg-gray-300 dark:bg-gray-700 rounded w-1/3 mb-8"></div>
                        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 mb-6">
                            <div className="h-6 bg-gray-300 dark:bg-gray-700 rounded w-1/4 mb-4"></div>
                            <div className="space-y-4">
                                <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-full"></div>
                                <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-full"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />

            <div className="max-w-4xl mx-auto px-4 py-12">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-2">
                        Profil Saya
                    </h1>
                    <p className="text-gray-600 dark:text-gray-400">
                        Kelola informasi profil dan keamanan akun Anda
                    </p>
                </div>

                {/* Profile Information Section */}
                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 mb-6">
                    <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
                        Informasi Profil
                    </h2>

                    <form onSubmit={handleProfileSubmit}>
                        <div className="space-y-4">
                            {/* Name */}
                            <div>
                                <label htmlFor="name" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Nama Lengkap
                                </label>
                                <input
                                    type="text"
                                    id="name"
                                    name="full_name"
                                    value={profileData.full_name}
                                    onChange={handleProfileChange}
                                    className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
                                    required
                                />
                            </div>

                            {/* Email (Read-only) */}
                            <div>
                                <label htmlFor="email" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Email
                                </label>
                                <input
                                    type="email"
                                    id="email"
                                    value={profileData.email}
                                    className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-100 dark:bg-gray-900 text-gray-600 dark:text-gray-400 cursor-not-allowed"
                                    disabled
                                />
                                <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
                                    Email tidak dapat diubah
                                </p>
                            </div>

                            {/* Submit Button */}
                            <div className="flex justify-end">
                                <button
                                    type="submit"
                                    disabled={saving}
                                    className="px-6 py-2 bg-primary text-white rounded-lg hover:bg-primary-light transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                                >
                                    {saving ? 'Menyimpan...' : 'Simpan Perubahan'}
                                </button>
                            </div>
                        </div>
                    </form>
                </div>

                {/* Change Password Section */}
                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
                    <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
                        Ubah Password
                    </h2>

                    <form onSubmit={handlePasswordSubmit}>
                        <div className="space-y-4">
                            {/* Current Password */}
                            <div>
                                <label htmlFor="current_password" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Password Saat Ini
                                </label>
                                <input
                                    type="password"
                                    id="current_password"
                                    name="current_password"
                                    value={passwordData.current_password}
                                    onChange={handlePasswordChange}
                                    className={`w-full px-4 py-2 border ${passwordErrors.current_password
                                        ? 'border-red-500'
                                        : 'border-gray-300 dark:border-gray-600'
                                        } rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent`}
                                />
                                {passwordErrors.current_password && (
                                    <p className="mt-1 text-sm text-red-500">{passwordErrors.current_password}</p>
                                )}
                            </div>

                            {/* New Password */}
                            <div>
                                <label htmlFor="new_password" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Password Baru
                                </label>
                                <input
                                    type="password"
                                    id="new_password"
                                    name="new_password"
                                    value={passwordData.new_password}
                                    onChange={handlePasswordChange}
                                    className={`w-full px-4 py-2 border ${passwordErrors.new_password
                                        ? 'border-red-500'
                                        : 'border-gray-300 dark:border-gray-600'
                                        } rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent`}
                                />
                                {passwordErrors.new_password && (
                                    <p className="mt-1 text-sm text-red-500">{passwordErrors.new_password}</p>
                                )}
                                <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
                                    Min. 8 karakter, 1 huruf besar, 1 huruf kecil, 1 angka, 1 karakter spesial
                                </p>
                            </div>

                            {/* Confirm Password */}
                            <div>
                                <label htmlFor="confirm_password" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                                    Konfirmasi Password Baru
                                </label>
                                <input
                                    type="password"
                                    id="confirm_password"
                                    name="confirm_password"
                                    value={passwordData.confirm_password}
                                    onChange={handlePasswordChange}
                                    className={`w-full px-4 py-2 border ${passwordErrors.confirm_password
                                        ? 'border-red-500'
                                        : 'border-gray-300 dark:border-gray-600'
                                        } rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent`}
                                />
                                {passwordErrors.confirm_password && (
                                    <p className="mt-1 text-sm text-red-500">{passwordErrors.confirm_password}</p>
                                )}
                            </div>

                            {/* Submit Button */}
                            <div className="flex justify-end">
                                <button
                                    type="submit"
                                    disabled={saving}
                                    className="px-6 py-2 bg-primary text-white rounded-lg hover:bg-primary-light transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                                >
                                    {saving ? 'Menyimpan...' : 'Ubah Password'}
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <Footer />
        </div>
    );
};

export default Profile;
