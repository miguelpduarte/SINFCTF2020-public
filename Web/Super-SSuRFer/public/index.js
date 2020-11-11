'use strict';

const express = require('express');
const fetch = require('node-fetch');
const morgan = require('morgan');

const verifyToken = require('./token_verifier');
const flag = require("./flag");

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express();

app.set('query parser', (queryString) => new URLSearchParams(queryString));
// Express setup
app.set('view engine', 'ejs');
app.use(express.urlencoded());
app.use(morgan('short'));
app.use('/static', express.static(__dirname + '/static'));


app.get('/', (req, res) => {
    return res.render('index');
});

app.post('/login', async (req, res) => {
    const { username, password, token } = req.body;

    const private_key = "REDACTED_PRODUCTION_KEY";
    // The username and password are static, but it's okay since we still have the very secure token!
    if (username === "b4ckdo0r" && password == "p0rtad0sFund0s!!") {
	// Verify the token
	const resp = await fetch(`http://127.0.0.1:${PORT}/verify?token=${token}&private_key=${private_key}`);
	const data = await resp.text();

	let message = "";
	if (data === "yes") {
	    message = flag;
	} else {
	    message = "Login failed!";
	}
	return res.render('index', {message});
    } else {
	return res.render('index', {message: "Login failed!"});
    }
});

app.get('/verify', (req, res) => {
    if (req.connection.remoteAddress !== '127.0.0.1') {
	return res.send("only local access");
    }
    
    const token = req.query.get('token');
    const private_key = req.query.get('private_key');

    // TODO: Don't forget to remove the debug private key: E1C9C68AAB24055C218B8B319D368BBD from the stage 2 token verifier
    if (verifyToken(token, private_key)) {
	return res.send("yes");
    } else {
	return res.send("no");
    }
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
