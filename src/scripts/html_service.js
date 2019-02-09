import $ from 'jquery';

export default class HTMLService {
	static displaySummary(data) {
		const summarySentences = data.sentences;
		const summaryContainer = $('#summaryContainer');
		summaryContainer.text('');

		if (summarySentences.length === 0) {
			summaryContainer.append($('<p></p>').text('No summary could be found for this page.'));
			return
		}

		for (let sentence of summarySentences) {
			summaryContainer.append($('<p></p>').text(sentence))
		}
	}
}