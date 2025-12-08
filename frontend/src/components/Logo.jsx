import React from 'react';

const Logo = () => {
    return (
        <div className="flex items-center justify-center">
            <div className="text-center">
                {/* Logo SVG - EZN with plane */}
                <svg width="120" height="80" viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg" className="mx-auto">
                    {/* Plane icon */}
                    <path d="M85 25L95 35L85 40L75 35L85 25Z" fill="#3B9DD9" />
                    <path d="M75 35L70 37L72 40L77 38L75 35Z" fill="#3B9DD9" />
                    <path d="M95 35L100 37L98 40L93 38L95 35Z" fill="#3B9DD9" />

                    {/* Text EZN */}
                    <text x="20" y="55" fontFamily="Inter, sans-serif" fontSize="32" fontWeight="800" fill="#2E3B7D">
                        EZ
                    </text>
                    <text x="72" y="55" fontFamily="Inter, sans-serif" fontSize="32" fontWeight="800" fill="#3B9DD9">
                        N
                    </text>
                </svg>
            </div>
        </div>
    );
};

export default Logo;
