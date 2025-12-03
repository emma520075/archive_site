<?php
/******************************************************************************
 * Nom        : process.php
 * Rôle       : Traite les données envoyées par le formulaire HTML (SQL)
 * Auteur     : Emma BARETS
 * Version    : V0.1 du 26/10/2025
 * Licence    : Réalisé dans le cadre du cours d’Informatique Fondamentale
 * Compilation : Interprété côté serveur via PHP
 * Dépendances : Nécessite db.php et une base MySQL fonctionnelle
 * Usage      : Enregistrement des messages dans la base de données SQL
 ******************************************************************************/

require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nom = htmlspecialchars($_POST['nom']);
    $email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
    $date_post = $_POST['date_post'];
    $note = intval($_POST['note']);
    $message = htmlspecialchars($_POST['message']);

    if (!$email) {
        die("Email invalide");
    }

    $sql = "INSERT INTO messages (nom, email, date_post, note, message) VALUES (?, ?, ?, ?, ?)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$nom, $email, $date_post, $note, $message]);

    header("Location: index.php");
    exit();
}
?>
