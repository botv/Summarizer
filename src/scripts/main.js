import 'bootstrap';
import $ from 'jquery';

$(() => {
	chrome.tabs.getSelected((tab) => {
		const currentURL = new URL(tab.url);

		console.log(currentURL)
	});
});