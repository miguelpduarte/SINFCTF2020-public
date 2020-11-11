<!DOCTYPE html>
<html>
    <head>
	<link href="https://fonts.googleapis.com/css?family=Waiting+for+the+Sunrise" rel="stylesheet" type="text/css"/>
    <style>
	body {
	  font-family: 'Waiting for the Sunrise', cursive;
	  font-size:30px;
	  margin: 10px 50px;
	  letter-spacing: 6px;
	  font-weight: bold;
	}
    </style>
</head>
<body>
<?php if (hash('tiger160,3', $_POST['password']) == '0e123123123438638639052845934576') { ?>
<h1>Hello admin!</h1>
<h2>Your flag:</h2>
<pre><code><?= file_get_contents('/etc/flag'); ?></code></pre>
<?php } else { ?>
<h1>Hmmm it seems like you got the wrong password...</h1>
<h2>Or possibly you are a hacker that was foiled! Hehe</h2>
<?php } ?>
</body>
</html>
