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
<?php if (md5($_POST['password']) === 'ad42f6697b035b7580e4fef93be20b4d') { ?>
<h1>Hello admin!</h1>
<h2>Your flag:</h2>
<pre><code><?= file_get_contents('/etc/flag'); ?></code></pre>
<?php } else { ?>
<h1>Hmmm it seems like you got the wrong password...</h1>
<?php } ?>
</body>
</html>
