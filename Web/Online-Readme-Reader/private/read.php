<?php
$UPLOADS_DIR = 'uploadzzz/';
$msg = '';
$error = false;
$filename = basename($_FILES['zipfile']['name']);
$filetype = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
$destination_dir = $UPLOADS_DIR . basename(md5($filename));
$readme_location = $destination_dir . '/README.txt';

if ($_FILES['zipfile']['size'] > 1000) {
    $error = true;
    $msg = 'File too large!';
}

if ($filetype !== 'zip') {
    $error = true;
    $msg = 'Only zip files allowed!';
}

if (!$error) {
    // Create destination dir
    mkdir($destination_dir);
    // Unzip file to destination_dir
    $escaped_zip_name = escapeshellarg($_FILES['zipfile']['tmp_name']);
    $escaped_destination_dir = escapeshellarg($destination_dir);
    // $retVal = 0;
    exec("unzip $escaped_zip_name -d $escaped_destination_dir ", $_irrelevant, $retval);
    
    if ($retval === 0) {
	if (file_exists($readme_location)) {
	    $msg = file_get_contents($readme_location);
	} else {
	    $error = true;
	    $msg = 'README.txt not found in zip file!';
	}
    } else {
	$error = true;
	$msg = 'Error opening zip file. Is it a valid zip?';
    }
    // This is easier than PHP version and probably works just as well
    shell_exec("rm -rf $escaped_destination_dir");
}
?>

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
    <h1>Online README.txt Reader - OR^2</h1>
    <?php if ($error) { ?>
    <h3 style="color:red;">Error!</h3>
    <p>Process unsuccessful! Reason:</p>
    <p><?=$msg?></p>
    <?php } else { ?>
    <h3 style="color:green;">Success!</h3>
    <p>Your file info:</p>
    <p><?=$msg?></p>
    <?php } ?>
</body>
</html>
