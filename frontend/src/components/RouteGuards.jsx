import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

export const ProtectedRoute = ({ children }) => {
    const { isAuthenticated, loading } = useAuth();

    if (loading) {
        return <div className="min-h-screen flex items-center justify-center"><div className="spinner border-4 border-primary-light border-t-transparent rounded-full w-12 h-12"></div></div>;
    }

    return isAuthenticated ? children : <Navigate to="/login" />;
};

export const AdminRoute = ({ children }) => {
    const { isAdmin, loading } = useAuth();

    if (loading) {
        return <div className="min-h-screen flex items-center justify-center"><div className="spinner border-4 border-primary-light border-t-transparent rounded-full w-12 h-12"></div></div>;
    }

    return isAdmin ? children : <Navigate to="/" />;
};
