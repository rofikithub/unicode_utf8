 <?php
header('Content-Type: application/json');

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "facebook";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}


$sql = "SELECT * FROM competency";
$result = $conn->query($sql);


$json = array();



if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    array_push($json, $row);
  }

  echo json_encode($json);
}

$conn->close();
?> 
