<?php
// --- CONFIGURATION DE LA CONNEXION (SÉCURISÉE TP6) ---
// On récupère les variables définies dans le fichier db.env via Docker
$dbhost = "db";     // Récupère "mariadb"
$dbname = "woodytoys"; // Récupère "woodytoys"
$dbuser = "root";     // Récupère "woodytoys"
$dbpass = "mypass"; // Récupère ton mot de passe secret

// Tentative de connexion
$connect = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname) 
    or die("Erreur : Impossible de joindre la base de données sur l'hôte '$dbhost'");

// Requête SQL
$result = mysqli_query($connect, "SELECT id, product_name, product_price FROM products");
?>

<!DOCTYPE html>
<html>
<head>
    <title>Catalogue WoodyToys</title>
    <style>
        /* Design : Fond bleu ciel et centrage */
        body {
            background-color: #87CEEB; /* SkyBlue */
            font-family: 'Segoe UI', Tahoma, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 50px;
        }
        h1 { color: #333; text-shadow: 1px 1px 2px white; }

        /* Style du tableau */
        table {
            background-color: white;
            border-collapse: collapse;
            width: 70%;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        }
        th, td { padding: 15px; border: 1px solid #ddd; text-align: center; }
        th { background-color: #2c3e50; color: white; }
        tr:nth-child(even) { background-color: #f9f9f9; }
    </style>
</head>
<body>
    <h1>Catalogue WoodyToys - Groupe L2-4</h1>

    <table>
        <tr>
            <th>ID</th>
            <th>Désignation du produit</th>
            <th>Prix</th>
        </tr>

        <?php
        // Boucle d'affichage des résultats
        while ($row = mysqli_fetch_array($result)) {
            printf("<tr><td>%s</td> <td>%s</td> <td>%s €</td></tr>",
                $row[0], $row[1], $row[2]);
        }
        
        // Fermeture de la connexion
        mysqli_close($connect);
        ?>
    </table>
</body>
</html>
