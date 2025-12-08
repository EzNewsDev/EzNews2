import React from 'react';

const DecoPattern = ({ position = 'left' }) => {
    const isLeft = position === 'left';

    return (
        <div className={`absolute ${isLeft ? 'left-0' : 'right-0'} top-0 bottom-0 w-48 hidden lg:block overflow-hidden`}>
            {/* Pattern circles */}
            <div className="h-full flex flex-col justify-center">
                {Array.from({ length: 8 }).map((_, i) => (
                    <div key={i} className="relative w-full h-32">
                        {/* Large circle */}
                        <div
                            className={`absolute ${isLeft ? 'left-0' : 'right-0'} w-24 h-24 rounded-full`}
                            style={{
                                background: `radial-gradient(circle at center, ${i % 2 === 0 ? '#3B9DD9' : '#2E3B7D'} 0%, ${i % 2 === 0 ? '#2E3B7D' : '#3B9DD9'} 100%)`,
                                opacity: 0.7,
                                clipPath: isLeft
                                    ? `circle(50% at ${-25 + (i % 3) * 10}% 50%)`
                                    : `circle(50% at ${125 - (i % 3) * 10}% 50%)`
                            }}
                        />
                        {/* Small circles */}
                        <div
                            className={`absolute ${isLeft ? 'left-12' : 'right-12'} top-2 w-12 h-12 rounded-full`}
                            style={{
                                background: `radial-gradient(circle at center, ${i % 2 === 0 ? '#2E3B7D' : '#3B9DD9'} 0%, ${i % 2 === 0 ? '#3B9DD9' : '#2E3B7D'} 100%)`,
                                opacity: 0.5
                            }}
                        />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default DecoPattern;
