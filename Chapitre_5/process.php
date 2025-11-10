<?php
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
