import React from 'react';
import { Link } from 'react-router-dom';

const ResetPassword = () => {
    return (
        <div className="min-h-screen flex items-center justify-center">
            <div className="text-center">
                <h1 className="text-2xl font-bold mb-4">Reset Password</h1>
                <p className="mb-4">Please use the Forgot Password page instead.</p>
                <Link to="/forgot-password" className="text-primary-light hover:text-primary">
                    Go to Forgot Password
                </Link>
            </div>
        </div>
    );
};

export default ResetPassword;
