/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode:'class',
  
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        body: ['Poppins', 'sans-serif'],
      },
      screens: {
        print: {raw: 'print'},
        screen: {raw: 'screen'},
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
