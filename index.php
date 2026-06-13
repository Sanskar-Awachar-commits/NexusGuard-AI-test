<?php
$username = $_POST['user'];
$password = $_POST['pass'];
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($conn, $query);

$search_term = $_GET['search'];
echo "<h2>Results for your search: " . $search_term . "</h2>";

$target_ip = $_GET['ip'];
echo "<pre>";
system("ping -c 4 " . $target_ip);
echo "</pre>";

$page = $_GET['page'];
include($page . ".php");
?>