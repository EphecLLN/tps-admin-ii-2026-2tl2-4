<html>
<head>
    <title>Catalogue WoodyToys</title>
    <style>
        /* Fond bleu ciel sur toute la page */
        body {
            background-color: #87CEEB; /* SkyBlue */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center; /* Centre tout horizontalement */
            padding-top: 50px;
        }

        h1 {
            color: #333;
            text-shadow: 1px 1px 2px white;
        }

        /* Style du tableau et centrage */
        table {
            background-color: white; /* Fond blanc pour que ce soit lisible */
            border-collapse: collapse;
            width: 60%;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.2); /* Petite ombre pour le style */
        }

        th, td {
            padding: 15px;
            border: 1px solid #ddd;
            text-align: center;
        }

        th {
            background-color: #2c3e50;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        tr:hover {
            background-color: #f1f1f1; /* Effet au survol */
        }
    </style>
<head>
<title>Catalogue WoodyToys</title>
</head>

<body>
<h1>Catalogue WoodyToys</h1>

<?php
$dbname = 'woodytoys';
$dbuser = 'root';
$dbpass = 'mypass';
$dbhost = 'db-server-tp5';
$connect = mysqli_connect($dbhost, $dbuser, $dbpass) or die("Unable to connect to '$dbhost'");
mysqli_select_db($connect,$dbname) or die("Could not open the database '$dbname'");
$result = mysqli_query($connect,"SELECT id, product_name, product_price FROM products");
?>

<table>
  <tr> <th>Numéro</th>
    <th>Descriptif</th>
    <th>Prix</th>
  </tr>

<?php
  while ($row = mysqli_fetch_array($result)) {
      // On utilise <td> pour les données et on ajoute le symbole €
      printf("<tr><td>%s</td> <td>%s</td> <td>%s €</td></tr>", $row[0], $row[1], $row[2]);
  }
  ?>
</table>
</body>
</html>
