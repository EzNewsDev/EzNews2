import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useAuth } from './contexts/AuthContext';

// Pages
import Login from './pages/Auth/Login';
import Register from './pages/Auth/Register';
import ForgotPassword from './pages/Auth/ForgotPassword';
import ResetPassword from './pages/Auth/ResetPassword';
import Home from './pages/Home';
import NewsList from './pages/NewsList';
import NewsDetail from './pages/NewsDetail';
import Profile from './pages/User/Profile';
import Bookmarks from './pages/User/Bookmarks';
import AdminDashboard from './pages/Admin/Dashboard';
import ArticleList from './pages/Admin/ArticleList';
import ArticleForm from './pages/Admin/ArticleForm';
import Categories from './pages/Admin/Categories';
import Tags from './pages/Admin/Tags';
import Users from './pages/Admin/Users';

// Protected Route Components
const ProtectedRoute = ({ children }) => {
    const { isAuthenticated, loading } = useAuth();

    if (loading) {
        return <div className="min-h-screen flex items-center justify-center"><div className="spinner border-4 border-primary-light border-t-transparent rounded-full w-12 h-12"></div></div>;
    }

    return isAuthenticated ? children : <Navigate to="/login" />;
};

const AdminRoute = ({ children }) => {
    const { isAdmin, loading } = useAuth();

    if (loading) {
        return <div className="min-h-screen flex items-center justify-center"><div className="spinner border-4 border-primary-light border-t-transparent rounded-full w-12 h-12"></div></div>;
    }

    return isAdmin ? children : <Navigate to="/" />;
};

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    {/* Public Routes */}
                    <Route path="/" element={<Home />} />
                    <Route path="/news" element={<NewsList />} />
                    <Route path="/news/:id" element={<NewsDetail />} />

                    {/* Auth Routes */}
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/forgot-password" element={<ForgotPassword />} />
                    <Route path="/reset-password" element={<ResetPassword />} />

                    {/* Protected User Routes */}
                    <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
                    <Route path="/bookmarks" element={<ProtectedRoute><Bookmarks /></ProtectedRoute>} />

                    {/* Admin Routes */}
                    <Route path="/admin" element={<AdminRoute><AdminDashboard /></AdminRoute>} />
                    <Route path="/admin/articles" element={<AdminRoute><ArticleList /></AdminRoute>} />
                    <Route path="/admin/articles/new" element={<AdminRoute><ArticleForm /></AdminRoute>} />
                    <Route path="/admin/articles/edit/:id" element={<AdminRoute><ArticleForm /></AdminRoute>} />
                    <Route path="/admin/categories" element={<AdminRoute><Categories /></AdminRoute>} />
                    <Route path="/admin/tags" element={<AdminRoute><Tags /></AdminRoute>} />
                    <Route path="/admin/users" element={<AdminRoute><Users /></AdminRoute>} />
                </Routes>

                <ToastContainer
                    position="top-right"
                    autoClose={3000}
                    hideProgressBar={false}
                    newestOnTop
                    closeOnClick
                    pauseOnFocusLoss
                    draggable
                    pauseOnHover
                />
            </div>
        </Router>
    );
}

export default App;
