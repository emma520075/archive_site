<?php
try {
    $pdo = new PDO('mysql:host=sql200.infinityfree.com;dbname=if0_40331579_5;charset=utf8', 'if0_40331579', 'Ieupnieupn55');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erreur de connexion à la base : " . $e->getMessage());
}
?>
