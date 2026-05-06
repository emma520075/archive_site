<?php
/****************************************************************************************
 * Nom        : traitement.php
 * Rôle       : Traitement des données envoyées par le formulaire HTML et insertion 
 * Auteur     : Emma BARETS
 * Version    : V0.1 du 26/11/2025
 * Licence    : Réalisé dans le cadre du cours d’Informatique Fondamentale
 * Compilation: Fichier PHP à exécuter via un serveur web avec PHP et accès à la base MySQL
 * Usage      : Inclusion du formulaire HTML via action="traitement.php" pour enregistrer les données
 ****************************************************************************************/

require_once 'db.php'; // connexion à la base (à créer, voir étape suivante)

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nom = htmlspecialchars($_POST['nom']);
    $email = htmlspecialchars($_POST['email']);
    $date_post = $_POST['date_post']; // la date sous format YYYY-MM-DD
    $note = (int)$_POST['note'];
    $message = htmlspecialchars($_POST['message']);

    // Préparation et exécution de l'insertion en base
    $stmt = $pdo->prepare("INSERT INTO utilisateurs (nom, email, date_inscription, note, message) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute([$nom, $email, $date_post, $note, $message]);

    echo "Merci, $nom, votre message a bien été enregistré.";
} else {
    echo "Accès interdit.";
}
?>
