const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
	mode: 'production',
	performance: {hints: false},
	entry: './src/scripts/main.js',
	output: {
		filename: 'scripts/main.js',
		path: path.resolve(__dirname, 'dist')
	},
	plugins: [
		new CopyWebpackPlugin([
			{from: 'src/styles/', to: 'styles/'},
			{from: 'src/images/', to: 'images/'},
			{from: 'node_modules/bootstrap/dist/css/bootstrap.css', to: 'styles/'},
			'src/manifest.json'
		]),
		new HtmlWebpackPlugin({
			filename: 'index.html',
			template: 'src/index.html'
		})
	]
};