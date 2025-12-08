import React from 'react';

const LoadingSkeleton = ({ type = 'card', count = 1 }) => {
    const CardSkeleton = () => (
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden animate-pulse">
            <div className="h-48 bg-gray-300 dark:bg-gray-700"></div>
            <div className="p-5 space-y-3">
                <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-3/4"></div>
                <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded"></div>
                <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-5/6"></div>
            </div>
        </div>
    );

    const TableSkeleton = () => (
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden">
            <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                <thead className="bg-gray-50 dark:bg-gray-900">
                    <tr>
                        {[...Array(4)].map((_, i) => (
                            <th key={i} className="px-6 py-3">
                                <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded animate-pulse"></div>
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody className="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
                    {[...Array(count)].map((_, rowIndex) => (
                        <tr key={rowIndex}>
                            {[...Array(4)].map((_, colIndex) => (
                                <td key={colIndex} className="px-6 py-4">
                                    <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded animate-pulse"></div>
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );

    const FormSkeleton = () => (
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 animate-pulse">
            <div className="space-y-6">
                {[...Array(count)].map((_, index) => (
                    <div key={index}>
                        <div className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-1/4 mb-2"></div>
                        <div className="h-10 bg-gray-300 dark:bg-gray-700 rounded"></div>
                    </div>
                ))}
            </div>
        </div>
    );

    const TextSkeleton = () => (
        <div className="animate-pulse space-y-3">
            {[...Array(count)].map((_, index) => (
                <div key={index} className="h-4 bg-gray-300 dark:bg-gray-700 rounded w-full"></div>
            ))}
        </div>
    );

    const skeletonTypes = {
        card: CardSkeleton,
        table: TableSkeleton,
        form: FormSkeleton,
        text: TextSkeleton
    };

    const SkeletonComponent = skeletonTypes[type] || CardSkeleton;

    if (type === 'card') {
        return (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {[...Array(count)].map((_, index) => (
                    <SkeletonComponent key={index} />
                ))}
            </div>
        );
    }

    return <SkeletonComponent />;
};

export default LoadingSkeleton;
