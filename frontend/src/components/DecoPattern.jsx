import React from 'react';
import batikKiri from '../assets/batik-kiri.png';
import batikKanan from '../assets/batik-kanan.png';

const DecoPattern = ({ position = 'left' }) => {
    const isLeft = position === 'left';
    const imageSrc = isLeft ? batikKiri : batikKanan;

    return (
        <div className={`absolute ${isLeft ? 'left-0' : 'right-0'} top-0 bottom-0 hidden lg:block overflow-hidden`}>
            <img 
                src={imageSrc} 
                alt={`${isLeft ? 'Left' : 'Right'} decoration`}
                className="w-full h-full object-cover"
            />
        </div>
    );
};

export default DecoPattern;
