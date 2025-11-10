// On attend que le DOM soit complètement chargé avant de manipuler les éléments
document.addEventListener("DOMContentLoaded", function() {

    // On récupère l'élément où l'utilisateur va entrer son nombre
    var zoneDeSaisie = document.querySelector('#zoneDeSaisie');

    // On récupère le bouton "Valider" pour écouter le clic de l'utilisateur
    var valider = document.querySelector('#valider');

    // On récupère le bouton "Rejouer" pour recommencer le jeu
    var rejouer = document.querySelector('#rejouer');

    // On récupère la div (de HTML) où on affichera le résultat du jeu
    var resultat = document.querySelector('#resultat');
	
	// Pour l'affichage
	var compteurAff = document.getElementById('compteur');
	var historiqueAff = document.getElementById('historique');
	
    // On génère un nombre aléatoire entre 1 et 100 inclus
    var nombreMystere = Math.floor(Math.random() * 100) + 1;
	
	// Variables pour le compteur et l'historique
	var essais = 0;
	var historique = [];
	
    // Quand l'utilisateur clique sur "Valider"
    valider.addEventListener('click', function() {
        
        // On récupère la valeur saisie par l'utilisateur et on la transforme en entier
        var devinette = parseInt(zoneDeSaisie.value);
		
		essais++; // On incrémente le compteur
		historique.push(devinette); // On ajoute le nombre à l'historique
    
		// Mise à jour de l'affichage
		compteurAff.textContent = "Nombre d'essais : " + essais;
		historiqueAff.textContent = "Historique : " + historique.join(", ");
		
		// Calcul de la distance
		var distance = Math.abs(devinette - nombreMystere);
		
		// On change la couleur selon la proximité
		if (distance === 0) {
			resultat.textContent = `Bravo! Vous avez trouvé le nombre mystère`;
			resultat.style.color = 'green';
			zoneDeSaisie.disabled = true;
			valider.disabled = true;
		} else if (distance <= 5) {
			resultat.textContent = "Très proche !";
			resultat.style.color = 'red';
		} else if (distance <= 15) {
			resultat.textContent = "Proche !";
			resultat.style.color = 'orange';
		} else if (distance <= 30) {
			resultat.textContent = "Pas mal, mais encore loin !";
			resultat.style.color = 'yellow';
		} else {
			resultat.textContent = "Très loin du nombre mystère !";
			resultat.style.color = 'blue';
		}

        // Si le champ est vide ou invalide
        if (isNaN(devinette)) {
            resultat.textContent = "Veuillez entrer un nombre valide !";
            return; // On sort de la fonction
        }

        // Comparaison avec le nombre mystère
        if (devinette < nombreMystere) {
            resultat.textContent = "Trop petit !"; // Message si le nombre est trop petit
        } 
        else if (devinette > nombreMystere) {
            resultat.textContent = "Trop grand !"; // Message si le nombre est trop grand
        } 
        else {
            resultat.textContent = `Bravo ! Vous avez trouvé le nombre mystère !`; // Message si gagné
            zoneDeSaisie.disabled = true; // On désactive le champ pour empêcher d'autres saisies
            valider.disabled = true; // On désactive le bouton pour empêcher d'autres clics
        }
    });

    // Quand l'utilisateur clique sur "Rejouer"
    rejouer.addEventListener('click', function() {
        // On génère un nouveau nombre aléatoire
        nombreMystere = Math.floor(Math.random() * 100) + 1;

        // On vide le champ de saisie et réactive le champ et le bouton
        zoneDeSaisie.value = '';
        zoneDeSaisie.disabled = false;
        valider.disabled = false;

        // On vide le message de résultat
        resultat.textContent = '';
		
		essais = 0; // Reset compteur
		historique = []; // Reset historique
		compteurAff.textContent = "Nombre d'essais : 0";
		historiqueAff.textContent = "Historique : ";
    });
	
	// On récupère l'image par son ID
    var shadokImg = document.getElementById("shadokImage");
    
    // On définit les deux images
    var image1 = "sha1.jpg";
    var image2 = "sha2.jpg";
    
    // On garde en mémoire quelle image est affichée
    var imageActuelle = 1;
    
    // Quand on clique sur l’image
    shadokImg.addEventListener("click", function() {
        if (imageActuelle === 1) {
            shadokImg.src = image2;   // On change vers la 2
            imageActuelle = 2;
        } else {
            shadokImg.src = image1;   // On revient à la 1
            imageActuelle = 1;
        }
	});
	
	const bouton = document.getElementById('boutonFuyant');
	const body = document.body;

	bouton.addEventListener('mouseover', function() {
		// Récupère la largeur et hauteur de la fenêtre
		const largeur = window.innerWidth - bouton.offsetWidth;
		const hauteur = window.innerHeight - bouton.offsetHeight;

    // Choisis une nouvelle position aléatoire
    const newX = Math.floor(Math.random() * largeur);
    const newY = Math.floor(Math.random() * hauteur);

    // Applique la nouvelle position
    bouton.style.left = newX + "px";
    bouton.style.top = newY + "px";
});

});