export default class APIService {
	static summarize(url, callback) {
		fetch('https://summarizer-api.herokuapp.com/?url=' + encodeURIComponent(url)).then((res) => {
			return res.text();
		}).then((text) => {
			callback(JSON.parse(text))
		});
	}
}