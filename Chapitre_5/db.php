<?php
/******************************************************************************
 * Nom        : db.php
 * Rôle       : Gérer la connexion MySQL via PDO pour le site web / formulaire
 * Auteur     : Emma BARETS
 * Version    : V0.1 du 25/10/2025
 * Licence    : Réalisé dans le cadre du cours d’Informatique Fondamentale
 * Dépendances : Nécessite une base MySQL fonctionnelle (InfinityFree ou locale)
 * Usage      : Inclus dans les fichiers PHP nécessitant un accès à la base
 ******************************************************************************/
 
try {
    $pdo = new PDO('mysql:host=sql200.infinityfree.com;dbname=if0_40331579_5;charset=utf8', 'if0_40331579', 'Ieupnieupn55');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erreur de connexion à la base : " . $e->getMessage());
}
?>
