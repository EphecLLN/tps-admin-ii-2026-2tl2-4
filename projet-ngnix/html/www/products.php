<?php
// Connexion au container de la DB
$conn = new mysqli("db-server-tp5", "root", "mypass", "woodytoys");

if ($conn->connect_error) {
    die("Échec de la connexion : " . $conn->connect_error);
}

$result = $conn->query("SELECT * FROM products");

echo "<h1>Catalogue WoodyToys - Groupe L2-4</h1>";
echo "<table border='1'><tr><th>ID</th><th>Nom</th><th>Prix</th></tr>";

while($row = $result->fetch_assoc()) {
    echo "<tr><td>" . $row['id'] . "</td><td>" . $row['product_name'] . "</td><td>" . $row['product_price'] . "€</td></tr>";
}
echo "</table>";
?>
