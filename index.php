$mysqli = new mysqli('localhost', 'username', 'password', 'database');
$label = $_POST['label'];
$stmt = $mysqli->prepare("INSERT INTO test(id, label) VALUES (?, ?)");
$stmt->bind_param("is", $id, $label);
$id = 1;
$stmt->execute();
$stmt->close();
$mysqli->close();