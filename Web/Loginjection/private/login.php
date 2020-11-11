<?php
session_start();
$db = mysqli_connect("db", "root", "bigmemes123", "loginjection");
if (mysqli_connect_errno()) {
	// If there is an error with the connection, stop the script and display the error.
	exit('Failed to connect to MySQL: ' . mysqli_connect_error());
}
if (!isset($_POST['username'], $_POST['password'])) {
    // Could not get the data that should have been sent.
    exit('Please fill both the username and password fields!');
}

$username = $_POST['username'];
$password = $_POST['password'];

$data = $db->query("SELECT * FROM `users` where username = '$username' and password = '$password'");
$login_success = $data->num_rows === 1;

if ($login_success) {
    session_regenerate_id();
    $_SESSION['loggedin'] = TRUE;
    header("Location: /flag.php");
    die();
} else {
    $encoded_message = urlencode('Invalid username and/or password!');
    header("Location: /?message=$encoded_message");
    die();
}
?>

