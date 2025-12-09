import React from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import { AnimatePresence } from 'framer-motion';
import PageTransition from './PageTransition';
import { ProtectedRoute, AdminRoute } from './RouteGuards';

// Pages
import Login from '../pages/Auth/Login';
import Register from '../pages/Auth/Register';
import ForgotPassword from '../pages/Auth/ForgotPassword';
import ResetPassword from '../pages/Auth/ResetPassword';
import Home from '../pages/Home';
import NewsList from '../pages/NewsList';
import NewsDetail from '../pages/NewsDetail';
import Profile from '../pages/User/Profile';
import Bookmarks from '../pages/User/Bookmarks';
import AdminDashboard from '../pages/Admin/Dashboard';
import { ArticleList } from '../pages/Admin/ArticleList';
import { ArticleForm } from '../pages/Admin/ArticleForm';
import { Categories } from '../pages/Admin/Categories';
import { Tags } from '../pages/Admin/Tags';
import { Users } from '../pages/Admin/Users';

const AnimatedRoutes = () => {
    const location = useLocation();

    return (
        <AnimatePresence mode="wait">
            <Routes location={location} key={location.pathname}>
                {/* Public Routes */}
                <Route path="/" element={<PageTransition><Home /></PageTransition>} />
                <Route path="/news" element={<PageTransition><NewsList /></PageTransition>} />
                <Route path="/news/:id" element={<PageTransition><NewsDetail /></PageTransition>} />

                {/* Auth Routes */}
                <Route path="/login" element={<PageTransition><Login /></PageTransition>} />
                <Route path="/register" element={<PageTransition><Register /></PageTransition>} />
                <Route path="/forgot-password" element={<PageTransition><ForgotPassword /></PageTransition>} />
                <Route path="/reset-password" element={<PageTransition><ResetPassword /></PageTransition>} />

                {/* Protected User Routes */}
                <Route path="/profile" element={
                    <ProtectedRoute>
                        <PageTransition><Profile /></PageTransition>
                    </ProtectedRoute>
                } />
                <Route path="/bookmarks" element={
                    <ProtectedRoute>
                        <PageTransition><Bookmarks /></PageTransition>
                    </ProtectedRoute>
                } />

                {/* Admin Routes */}
                <Route path="/admin" element={
                    <AdminRoute>
                        <PageTransition><AdminDashboard /></PageTransition>
                    </AdminRoute>
                } />
                <Route path="/admin/articles" element={
                    <AdminRoute>
                        <PageTransition><ArticleList /></PageTransition>
                    </AdminRoute>
                } />
                <Route path="/admin/articles/new" element={
                    <AdminRoute>
                        <PageTransition><ArticleForm /></PageTransition>
                    </AdminRoute>
                } />
                <Route path="/admin/articles/edit/:id" element={
                    <AdminRoute>
                        <PageTransition><ArticleForm /></PageTransition>
                    </AdminRoute>
                } />
                <Route path="/admin/categories" element={
                    <AdminRoute>
                        <PageTransition><Categories /></PageTransition>
                    </AdminRoute>
                } />
                <Route path="/admin/tags" element={
                    <AdminRoute>
                        <PageTransition><Tags /></PageTransition>
                    </AdminRoute>
                } />
                <Route path="/admin/users" element={
                    <AdminRoute>
                        <PageTransition><Users /></PageTransition>
                    </AdminRoute>
                } />
            </Routes>
        </AnimatePresence>
    );
};

export default AnimatedRoutes;
