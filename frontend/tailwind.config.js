/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#2E3B7D',
                    light: '#3B9DD9',
                    dark: '#1F2952'
                },
                secondary: {
                    DEFAULT: '#3B9DD9',
                    light: '#6BB8E8',
                    dark: '#2A7AB0'
                }
            },
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
            }
        },
    },
    plugins: [],
}
