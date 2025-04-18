<?php
<<<<<<< HEAD
<<<<<<< HEAD
// Récupérer la requête SQL envoyée depuis le client
$sqlQuery = $_POST['sqlQuery'];

// Exécuter la requête SQL et récupérer les résultats
// Remplacez cette partie par votre propre logique pour exécuter la requête SQL
// et récupérer les résultats depuis votre base de données

// Exemple de connexion à une base de données MySQL
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "facebook_infos";

// Créer une connexion
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifier la connexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Exécuter la requête SQL
$result = $conn->query($sqlQuery);

// Récupérer les résultats et les stocker dans un tableau
$results = array();
if ($result && $result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $results[] = $row;
    }
}

// Fermer la connexion à la base de données
$conn->close();

// Retourner les résultats au format JSON
header('Content-Type: application/json');
echo json_encode($results);
?>
=======

=======

>>>>>>> main

if (isset($_POST['fieldSelect'])) {
    $fieldSelect = $_POST['fieldSelect'];
    $sqlQuery = "";
    switch ($fieldSelect) {
        case 'date':
            $startDate = @$_POST['startDate'];
            $endDate = @$_POST['endDate'];
            if ($startDate != null && $endDate != null) {
                $sqlQuery = "SELECT * FROM `facebook_infos.users` WHERE `date` BETWEEN '$startDate' AND '$endDate'";
            }
            break;
        default:
            $conditionValue = @$_POST['conditionValue'];
            if ($conditionValue != null) {
                $sqlQuery = "SELECT * FROM `facebook_infos.users` WHERE `$fieldSelect` = '$conditionValue'";
            }
            break;
    }

    if ($sqlQuery != '') {
        $serverName = "localhost";
        $username = "root";
        $password = "";
        $dbname = "facebook_infos";

        // Mieux vaut PDO et les requêtes préparées  que mysqli...
        try {
            $conn = new mysqli($serverName, $username, $password, $dbname);
            $result = $conn->query($sqlQuery);
<<<<<<< HEAD

=======
            var_dump($result);
>>>>>>> main
            echo json_encode($result->fetch_all());
            $conn->close();
        } catch (\Exception $e) {
            http_response_code(500);
            echo json_encode($e->getMessage());
        }

        exit;
    }
}

http_response_code(400);
echo json_encode("Requête incomplete");
<<<<<<< HEAD
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)
=======
>>>>>>> main
