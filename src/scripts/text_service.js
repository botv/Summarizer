export default class TextService {
	static async analyze(url) {
		fetch(url).then((res) => {
			return res.text()
		}).then((res) => {
			console.log(res)
		});
	}
}