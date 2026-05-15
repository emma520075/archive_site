"""
****************************************************************************************
* Nom        : chatbot_version_final.py
* Rôle       : Chatbot éducatif pour le cours d’Informatique Fondamentale de l’IED Paris 8.
*             Permet de répondre aux questions sur le cours, les professeurs, les devoirs,
*             le campus, ainsi que l’heure et la date. Interface graphique développée avec Tkinter.
* Auteur     : Emma BARETS
<<<<<<< HEAD
* Version    : Version finale du 17/01/2026
=======
* Version    : Version finale du 17/02/2026
>>>>>>> 0ea5404255d1c2198d3bb81ebd09726a29caff16
* Licence    : Réalisé dans le cadre du cours d’Informatique Fondamentale
* Compilation: Exécuter via Python 3 (python chatbot_version_final.py)
* Usage      : Interface graphique pour poser des questions et obtenir des réponses instantanées.
* Modules    : 
*             - tkinter : interface graphique
*             - scrolledtext : zone de conversation défilante
*             - messagebox : affichage de pop-ups
*             - random : choix aléatoire des réponses
*             - PIL (Image, ImageTk) : gestion des images (logo)
*             - os : vérification de l’existence des fichiers
*             - datetime : récupération de la date et de l’heure
****************************************************************************************
"""

import tkinter as tk  # Importation de Tkinter pour créer l'interface graphique
from tkinter import scrolledtext, messagebox  # Importation pour les zones de texte défilantes et les pop-ups
import random  # Pour choisir aléatoirement des réponses
from PIL import Image, ImageTk  # Pour gérer les images dans Tkinter
import os  # Pour vérifier si les fichiers existent
import datetime  # Pour récupérer l'heure et la date

# --------------------------
# Fenêtre principale
# --------------------------
root = tk.Tk()  # Création de la fenêtre principale
root.title("Parle moi: Paris 8 ChatBot")  # Titre de la fenêtre
root.geometry("700x650")  # Taille de la fenêtre
root.config(bg="#f0f2f5")  # Couleur de fond

# --------------------------
# Header (en-tête)
# --------------------------
header = tk.Frame(root, bg="#004080", height=80)  # Frame qui contient le logo, titre et bouton
header.pack(fill=tk.X)  # S'étend sur toute la largeur

# --------------------------
# Fonction pour salutation (bonjour ou bonsoir)
# --------------------------
def salutations_heure():
    """Renvoie un message de salutation selon l'heure de la journée"""
    heure_actuelle = datetime.datetime.now().hour  # Récupère l'heure actuelle
    if 5 <= heure_actuelle < 12:
        return "Bonjour !"  # Matin
    elif 12 <= heure_actuelle < 18:
        return "Bon après-midi !"  # Après-midi
    else:
        return "Bonsoir !"  # Soir

# --------------------------
# Dictionnaire des réponses
# --------------------------
# Chaque catégorie contient des réponses possibles
Dictionnaire_mot_clé = {
    "salutation": [lambda: salutations_heure()],  # On utilise lambda ici pour mettre la fonction salutations_heure() dans le dictionnaire sans l’exécuter tout de suite, afin qu’elle soit appelée uniquement quand le chatbot doit répondre.
    "etat": [
        "Ça va très bien, merci ! Et toi ?",
        "Je vais bien, prêt à t'aider !",
        "Tout roule ! Et de ton côté ?"
    ],
    "organisation_cours": [
        "Le cours d'Informatique Fondamentale est structuré en deux parties :\n"
        "- Partie 1 : Système d’exploitation GNU/Linux et interactions locales \"utilisateur-système\" (par Larbi Boubchir)\n"
        "- Partie 2 : Internet et Web, interactions distantes \"utilisateur-serveur\" (par Philippe Kislin-Duval)"
    ],
    "professeurs": [
        "Partie 1 : Larbi Boubchir\nPartie 2 : Philippe Kislin-Duval"
    ],
    "devoirs_partie2": [
        "Vous pouvez envoyer vos devoirs pour la Partie 2 à partir du 26 mai 2026."
    ],
    "date_limite": [
        "La date limite d'envoi du PDF final avec tous les TP est fixée au 1er août 2026."
    ],
    "chapitre1": [
        "Chapitre 1 - Système d'exploitation : notions générales, introduction à GNU/Linux et installation d'Ubuntu."
    ],
    "chapitre2": [
        "Chapitre 2 - Interface système : terminal, Shell, commandes de base pour gérer fichiers et répertoires."
    ],
    "chapitre3": [
        "Chapitre 3 - Commandes avancées : gestion des droits, scripts Shell, commande écho ..."
    ],
    "exercices": [
        "Des exercices et PDFs sont disponibles pour chaque chapitre afin de pratiquer et valider vos connaissances."
    ],
    "inscriptions": [
        "Les inscriptions pour l'année 2025-2026 sont finis."
    ],
    "rappel": [
        "Important : envoyer un mail préalable entre le 11 et le 31 mai 2026 avant d’envoyer votre PDF final avec l’intégralité des TP regroupés."
    ],
    "heure": [
        lambda: f"Il est {datetime.datetime.now().strftime('%H:%M')}."  # Fonction lambda pour afficher l'heure
    ],
    "date_auj": [
        lambda: f"Aujourd'hui, nous sommes le {datetime.datetime.now().strftime('%A %d %B %Y')}."  # Fonction lambda pour afficher la date
    ],
    "paris8": [
        "L'IED Paris 8 est situé à Saint-Denis. Plus d'infos sur le site : https://www.univ-paris8.fr/ (pour Paris 8) et sur https://ied.univ-paris8.fr/ (pour l'IED Paris 8)"
    ],
    "merci": [
        "Avec plaisir 😄 !",
        "De rien, je suis là pour ça !",
        "Tout le plaisir est pour moi !"
    ],
}

# --------------------------
# Synonymes pour détecter différentes formulations
# --------------------------
# Permet au bot de comprendre différentes manières de poser la même question
synonymes = {
    "salutation": ["bonjour", "bonsoir", "salut", "bjr", "hello", "slt"],
    "etat": ["ça va", "cv", "comment ça va", "comment vas tu"],
    "organisation_cours": ["organisation du cours", "cours", "informatique fondamentale", "IF"],
    "professeurs": ["professeurs", "enseignants", "qui enseigne", "profs", "profs"],
    "devoirs_partie2": ["devoirs partie 2", "envoyer devoirs", "quand envoyer devoirs", "quand peut-on envoyer nos devoirs"],
    "date_limite": ["date limite", "fin devoir", "fin du devoir", "deadline", "rendu cours"],
    "chapitre1": ["chapitre 1", "système d'exploitation", "linux", "ubuntu"],
    "chapitre2": ["chapitre 2", "interface système", "shell", "terminal"],
    "chapitre3": ["chapitre 3", "commandes avancées", "scripts", "redirection", "processus"],
    "exercices": ["exercices", "tp", "pdf", "pratique"],
    "inscriptions": ["inscriptions", "année 2025", "2025-2026"],
    "rappel": ["rappel", "mail", "consignes"],
    "heure": ["quelle heure", "heure"],
    "date_auj": ["quelle date", "jour", "date aujourd'hui", "aujourd'hui"],
    "paris8": ["paris 8", "ied paris 8", "campus paris 8"],
    "merci": ["merci", "thanks"],
    "je_ne_sais_pas": ["je ne sais pas", "je sais pas", "je comprend pas"]
}

# --------------------------
# Fonction de réponse
# --------------------------
def Reponse_utilisateur(user_input):
    """
    Analyse la phrase de l'utilisateur et renvoie une ou plusieurs réponses.
    - Convertit en minuscules pour uniformiser
    - Cherche les mots-clés ou synonymes
    - Choisit une réponse aléatoire parmi celles disponibles
    """
    user_input = user_input.lower()
    mots_prioritaires = []

    # Créer une liste triée par longueur des mots pour détecter d'abord les plus précis
    for key, mots in synonymes.items():
        for mot in mots:
            mots_prioritaires.append((key, mot))
    mots_prioritaires.sort(key=lambda x: -len(x[1]))

    réponses = []
    for key, mot in mots_prioritaires:
        if mot in user_input:  # Si le mot-clé est présent dans la phrase
            response = random.choice(Dictionnaire_mot_clé[key])
            if callable(response):  # Vérifie si c'est une fonction (lambda)
                response = response()
            if response not in réponses:  # Évite les doublons
                réponses.append(response)

    # Si aucune réponse trouvée
    if réponses:
        return "\n".join(réponses)
    else:
        return "Désolé, je n'ai pas l'info… Je suis encore en train d'apprendre sur ce sujet !"

# --------------------------
# Fonction pour envoyer la question
# --------------------------
def Question_utilisateur(event=None):
    """
    Récupère la question de l'utilisateur et affiche la réponse du bot.
    """
    user_input = entry.get().strip()  # Récupère le texte saisi
    if not user_input:
        return  # Ne rien faire si l'entrée est vide
    chat_window.config(state="normal")  # Active la zone pour écrire
    chat_window.insert(tk.END, f"👩‍🎓 Vous : {user_input}\n", "user_tag")
    response = Reponse_utilisateur(user_input)  # Obtenir la réponse
    chat_window.insert(tk.END, f"🤖 Paris8_ChatBot : {response}\n\n", "bot_tag")
    chat_window.config(state='disabled')  # Désactive pour éviter la saisie directe
    entry.delete(0, tk.END)  # Efface la zone de saisie
    chat_window.see(tk.END)  # Défiler vers le bas

# --------------------------
# Fenêtre de présentation
# --------------------------
def show_presentation():
    """Affiche une fenêtre popup présentant le chatbot et ses fonctionnalités"""
    messagebox.showinfo(
        "Présentation du Chatbot:",
        "🤖 Bienvenue dans ASK ME: Paris8 ChatBot !\n\n"
        "✨ Fonctionnalités principales :\n"
        "• Je répond aux questions sur le cours Informatique Fondamentale.\n"
        "• Je fournis les infos sur le campus Paris 8 et les professeurs.\n"
        "• Je donne les dates limites et consignes pour les devoirs.\n"
        "• Je peux combiner plusieurs réponses dans la même phrase !\n\n"
        "🎓 Amuse-toi bien à l'IED Paris 8 !"
    )

# --------------------------
# Logo IED Paris 8
# --------------------------
if os.path.exists("paris8.jpg"):  # Vérifie que l'image existe
    campus_img = Image.open("paris8.jpg").resize((60, 60), Image.LANCZOS)  # Redimensionner l'image
    campus_logo = ImageTk.PhotoImage(campus_img)  # Convertir pour Tkinter
    campus_label = tk.Label(header, image=campus_logo, bg="#004080")  # Label pour afficher l'image
    campus_label.pack(side=tk.LEFT, padx=15)
else:
    print("⚠️ Image 'paris8.jpg' introuvable. Vérifiez le nom et le dossier.")

# --------------------------
# Titre au centre
# --------------------------
title_label = tk.Label(header, text="Parle moi: Paris 8 ChatBot",
    font=("Helvetica", 18, "bold"), bg="#004080", fg="white")
title_label.pack(side=tk.LEFT, expand=True)

# --------------------------
# Bouton présentation
# --------------------------
presentation_button = tk.Button(header, text="📖 Présentation", command=show_presentation,
    font=("Arial", 11, "bold"), bg="white", fg="#004080",
    relief="flat", padx=10, pady=5)
presentation_button.pack(side=tk.RIGHT, padx=10)

# --------------------------
# Zone de conversation
# --------------------------
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled",
    font=("Arial", 12), bg="white", fg="black")
chat_window.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
chat_window.tag_configure("user_tag", foreground="#1a73e8", font=("Arial", 11, "bold"))  # Style utilisateur
chat_window.tag_configure("bot_tag", foreground="#0b8043", font=("Arial", 11, "bold"))  # Style bot

# --------------------------
# Zone de saisie et bouton d'envoi
# --------------------------
input_frame = tk.Frame(root, bg="#f0f2f5")  # Conteneur pour l'entrée et bouton
input_frame.pack(pady=10, fill=tk.X)
entry = tk.Entry(input_frame, width=45, font=("Arial", 12), relief="flat",
    bg="#ffffff", fg="black", highlightbackground="#004080", highlightthickness=1)
entry.pack(side=tk.LEFT, padx=10, ipady=6)
send_button = tk.Button(input_frame, text="➡ Envoyer", command=Question_utilisateur,
    font=("Arial", 12, "bold"), bg="#004080", fg="white",
    activebackground="#0066cc", activeforeground="white",
    relief="flat", padx=15, pady=5)
root.bind("<Return>", Question_utilisateur)  # Permet d'envoyer avec la touche Entrée
send_button.pack(side=tk.LEFT, padx=5)

# --------------------------
# Boucle principale
# --------------------------
root.mainloop()  # Démarre l'application et attend les interactions de l'utilisateur

