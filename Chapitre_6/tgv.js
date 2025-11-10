const url = "https://data.sncf.com/api/explore/v2.1/catalog/datasets/regularite-mensuelle-tgv-aqst/records?limit=25";

const container = document.getElementById("tableauTGV");
const filtreService = document.getElementById("filtreService");

let toutesDonnees = []; // on stocke toutes les données pour filtrer

function creerTableau(data) {
    if (!data || data.length === 0) {
        container.innerHTML = "<p>Aucune donnée disponible</p>";
        return;
    }

    const colonnes = ["date", "service", "gare_depart", "gare_arrivee", "duree_moyenne", "nb_train_prevu", "nb_annulation"];
    let html = "<table border='1' cellspacing='0' cellpadding='5'><tr>";

    colonnes.forEach(col => html += `<th>${col}</th>`);
    html += "</tr>";

    data.forEach(item => {
        html += "<tr>";
        colonnes.forEach(col => {
            html += `<td>${item[col] !== undefined ? item[col] : ""}</td>`;
        });
        html += "</tr>";
    });

    html += "</table>";
    container.innerHTML = html;
}

// Fonction pour filtrer les données
function filtrerDonnees() {
    const serviceSelectionne = filtreService.value;
    if (serviceSelectionne === "Tous") {
        creerTableau(toutesDonnees);
    } else {
        const filtre = toutesDonnees.filter(item => item.service === serviceSelectionne);
        creerTableau(filtre);
    }
}

// Écouteur sur le select
filtreService.addEventListener("change", filtrerDonnees);

// Récupération des données
fetch(url)
    .then(response => response.json())
    .then(data => {
        toutesDonnees = data.results; // on garde toutes les données
        creerTableau(toutesDonnees);
    })
    .catch(error => {
        container.innerHTML = "Erreur lors de la récupération des données : " + error;
        console.error(error);
    });
