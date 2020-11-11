<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
	<meta charset="utf-8">
	<title>Login</title>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css">
	<link href="styles.css" rel="stylesheet" type="text/css">
    </head>
    <body>
	<nav>
	    <ul>
		<li><a href="/">Login</a></li>
		<li><a href="/flag.php">Flag</a></li>
		<li class="align-end"><a href="/logout.php">Log out</a></li>
	    </ul>
	</nav>
	<div class="flag">
	    <h1>Flag</h1>
	    <div class="content">
	    <?php if ($_SESSION['loggedin']) { ?>
		<p>Here you go dear Admin:</p>
		<pre><code><?=file_get_contents('/etc/flag');?></pre></code>
	    <?php } else { ?>
		<p>The flag is only available to logged in admins!</p>
		<p>Please <a href="/">login</a> as admin to get the flag.</p>
	    <?php } ?>
	    </div>
	</div>
    </body>
</html>
