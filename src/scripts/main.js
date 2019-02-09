import 'bootstrap';
import $ from 'jquery';
import APIService from './api_service';
import HTMLService from './html_service'

$(() => {
	chrome.tabs.getSelected((tab) => {
		const currentURL = new URL(tab.url);

		console.log(currentURL);

		APIService.summarize(currentURL.href, (result) => {
			HTMLService.displaySummary(result)
		});
	});
});