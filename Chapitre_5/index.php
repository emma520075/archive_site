<form action="process.php" method="POST">
    Nom : <input type="text" name="nom" required><br>
    Email : <input type="email" name="email" required><br>
    Date : <input type="date" name="date_post" required><br>
    Note (1-5) : <input type="number" name="note" min="1" max="5" required><br>
    Message : <textarea name="message" required></textarea><br>
    <button type="submit">Envoyer</button>
</form>

<?php
require 'db.php';

$sql = "SELECT * FROM messages ORDER BY date_post DESC";
$stmt = $pdo->query($sql);

while ($row = $stmt->fetch()) {
    echo "<div>";
    echo "<strong>Nom :</strong> " . htmlspecialchars($row['nom']) . "<br>";
    echo "<strong>Email :</strong> " . htmlspecialchars($row['email']) . "<br>";
    echo "<strong>Date :</strong> " . htmlspecialchars($row['date_post']) . "<br>";
    echo "<strong>Note :</strong> " . intval($row['note']) . "<br>";
    echo "<strong>Message :</strong> " . nl2br(htmlspecialchars($row['message'])) . "<br>";
    echo "</div><hr>";
}
?>
