import 'bootstrap';
import $ from 'jquery';
import TextService from './text_service';

$(() => {
	chrome.tabs.getSelected((tab) => {
		const currentURL = new URL(tab.url);

		console.log(currentURL);
	});

	TextService.analyze('https://www.google.com')
});