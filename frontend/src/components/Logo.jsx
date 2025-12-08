import React from 'react';
import logo from '../assets/logo_EzNews_new.png';

const Logo = () => {
    return (
        <div className="flex justify-center">
            <img src={logo} alt="EzNews Logo" className="h-12 w-auto" />
        </div>
    );
};

export default Logo;