{
  "patched_code": "
<?php
$mysqli = new mysqli('localhost', 'username', 'password', 'database');

if ($mysqli->connect_errno) {
    echo \"Failed to connect to MySQL: (\" . $mysqli->connect_errno . \") \" . $mysqli->connect_error;
}

$id = $_POST['id'];
$label = $_POST['label'];

$stmt = $mysqli->prepare(\"INSERT INTO test(id, label) VALUES (?, ?)\");
$stmt->bind_param(\"is\", $id, $label);
$stmt->execute();

$stmt->close();
$mysqli->close();
?>",
  "explanation": "The original code was vulnerable to SQL injection because it directly inserted user-provided data into a manually-constructed SQL string. This allowed an attacker to potentially inject malicious SQL code and steal or manipulate data from the database. The patched code fixes this vulnerability by using a prepared statement with parameterized queries. The `$mysqli->prepare()` function is used to prepare the SQL query, and the `$stmt->bind_param()` function is used to bind the user-provided data to the query parameters. This ensures that the user data is treated as literal input and not as part of the SQL code, preventing SQL injection attacks. The use of prepared statements also improves the security and performance of the code by reducing the risk of SQL injection and allowing the database to cache the query plan."
}