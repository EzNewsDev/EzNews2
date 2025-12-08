import React from 'react';

const EmptyState = ({
    icon,
    title,
    message,
    actionLabel,
    onAction
}) => {
    const defaultIcon = (
        <svg
            className="mx-auto h-24 w-24 text-gray-400 dark:text-gray-600"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
        >
            <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
            />
        </svg>
    );

    return (
        <div className="text-center py-16 px-4">
            {icon || defaultIcon}

            <h3 className="mt-4 text-xl font-semibold text-gray-900 dark:text-white">
                {title}
            </h3>

            <p className="mt-2 text-gray-600 dark:text-gray-400 max-w-md mx-auto">
                {message}
            </p>

            {actionLabel && onAction && (
                <button
                    onClick={onAction}
                    className="mt-6 inline-flex items-center px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary-light transition-colors"
                >
                    {actionLabel}
                </button>
            )}
        </div>
    );
};

export default EmptyState;
