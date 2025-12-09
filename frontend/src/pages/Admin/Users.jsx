import React, { useState, useEffect } from 'react';
import Navbar from '../../components/Navbar';
import LoadingSkeleton from '../../components/LoadingSkeleton';
import api from '../../utils/api';
import { toast } from 'react-toastify';
import { format } from 'date-fns';
import { id as idLocale } from 'date-fns/locale/id';

export const Users = () => {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        setLoading(true);
        try {
            const response = await api.get('/users');
            setUsers(response.data.users);
        } catch (error) {
            console.error('Error fetching users:', error);
            toast.error('Gagal memuat pengguna');
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (id) => {
        if (!window.confirm('Apakah Anda yakin ingin menghapus pengguna ini? Tindakan ini tidak dapat dibatalkan.')) return;

        try {
            await api.delete(`/users/${id}`);
            toast.success('Pengguna berhasil dihapus');
            fetchUsers();
        } catch (error) {
            console.error('Error deleting user:', error);
            const errorMsg = error.response?.data?.error || 'Gagal menghapus pengguna';
            toast.error(errorMsg);
        }
    };

    return (
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
            <Navbar />
            <div className="max-w-7xl mx-auto px-4 py-12">
                {/* Header */}
                <div className="flex justify-between items-center mb-8">
                    <div>
                        <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
                            Kelola Pengguna
                        </h1>
                        <p className="text-gray-600 dark:text-gray-400">
                            Daftar pengguna terdaftar
                        </p>
                    </div>
                </div>

                {/* Table */}
                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden">
                    {loading ? (
                        <div className="p-6">
                            <LoadingSkeleton type="text" count={5} />
                        </div>
                    ) : users.length > 0 ? (
                        <div className="overflow-x-auto">
                            <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                                <thead className="bg-gray-50 dark:bg-gray-900">
                                    <tr>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Nama</th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Email</th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Role</th>
                                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Bergabung</th>
                                        <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">Aksi</th>
                                    </tr>
                                </thead>
                                <tbody className="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
                                    {users.map((user) => (
                                        <tr key={user.id} className="hover:bg-gray-50 dark:hover:bg-gray-700">
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <div className="flex items-center">
                                                    <div className="h-8 w-8 rounded-full bg-primary text-white flex items-center justify-center text-sm font-bold mr-3">
                                                        {user.full_name.charAt(0).toUpperCase()}
                                                    </div>
                                                    <div className="text-sm font-medium text-gray-900 dark:text-white">
                                                        {user.full_name}
                                                    </div>
                                                </div>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                                                {user.email}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap">
                                                <span className={`px-2 py-1 text-xs font-semibold rounded-full ${user.role === 'admin'
                                                        ? 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200'
                                                        : 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                                                    }`}>
                                                    {user.role}
                                                </span>
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                                                {user.created_at
                                                    ? format(new Date(user.created_at), 'dd MMM yyyy', { locale: idLocale })
                                                    : '-'
                                                }
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                                <button
                                                    onClick={() => handleDelete(user.id)}
                                                    className="text-red-600 hover:text-red-900 dark:text-red-400 dark:hover:text-red-300"
                                                >
                                                    Hapus
                                                </button>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    ) : (
                        <div className="p-8 text-center text-gray-500 dark:text-gray-400">
                            Belum ada pengguna.
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};
