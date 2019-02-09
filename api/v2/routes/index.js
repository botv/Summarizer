const express = require('express');
const AYLIENTextAPI = require('aylien_textapi');

const textAPI = new AYLIENTextAPI({
	application_id: process.env.AYLIEN_APP_ID,
	application_key: process.env.AYLIEN_APP_KEY
});

const router = express.Router();

router.get('/summarize', (req, res) => {
	textAPI.summarize({
		url: decodeURIComponent(req.query.url),
		sentences_number: 3
	}, (error, result) => {
		res.send(result)
	});
});

router.get('/sentiment', (req, res) => {
	textAPI.sentiment({
		url: decodeURIComponent(req.query.url)
	}, function(error, result) {
		res.send(result)
	});
});

module.exports = router;
