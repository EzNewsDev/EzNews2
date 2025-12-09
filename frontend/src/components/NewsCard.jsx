import React from 'react';
import { Link } from 'react-router-dom';
import { formatDistanceToNow } from 'date-fns';
import { id as idLocale } from 'date-fns/locale/id';

const NewsCard = ({ article }) => {
    // Safety check for article object
    if (!article) {
        return null;
    }

    const { id: articleId, title, content, image_url, category, author_name, published_date } = article;

    // Extract first 150 characters as excerpt
    const excerpt = content ? content.substring(0, 150) + '...' : '';

    // Format date to relative time
    const timeAgo = published_date ? formatDistanceToNow(new Date(published_date), {
        addSuffix: true,
        locale: idLocale
    }) : 'Baru saja';

    return (
        <Link
            to={`/news/${articleId}`}
            className="group block bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden transform hover:-translate-y-1"
        >
            {/* Image */}
            <div className="relative h-48 overflow-hidden bg-gray-200 dark:bg-gray-700">
                {image_url ? (
                    <img
                        src={image_url}
                        alt={title}
                        className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
                        onError={(e) => {
                            e.target.style.display = 'none';
                        }}
                    />
                ) : (
                    <div className="w-full h-full flex items-center justify-center text-gray-400 dark:text-gray-500">
                        <svg className="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                        </svg>
                    </div>
                )}

                {/* Category Badge */}
                {category && (
                    <div className="absolute top-3 left-3">
                        <span className="px-3 py-1 bg-primary text-white text-xs font-semibold rounded-full shadow-md">
                            {category.name}
                        </span>
                    </div>
                )}
            </div>

            {/* Content */}
            <div className="p-5">
                {/* Title */}
                <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2 line-clamp-2 group-hover:text-primary-light transition-colors">
                    {title}
                </h3>

                {/* Excerpt */}
                <p className="text-gray-600 dark:text-gray-400 text-sm mb-4 line-clamp-3">
                    {excerpt}
                </p>

                {/* Meta Info */}
                <div className="flex items-center justify-between text-xs text-gray-500 dark:text-gray-500">
                    <div className="flex items-center space-x-2">
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                        </svg>
                        <span>{author_name}</span>
                    </div>
                    <div className="flex items-center space-x-2">
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span>{timeAgo}</span>
                    </div>
                </div>
            </div>
        </Link>
    );
};

export default NewsCard;
