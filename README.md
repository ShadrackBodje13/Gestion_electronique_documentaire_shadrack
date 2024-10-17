# Gestion_electronique_documentaire_shadrack
J'ai utilisé un cas d'usage, et j'ai essayé de proposer une solution pour la gestion electronique de donnée. 

Voici les étapes de traitement que je me suis mis. 
1-Initialisation des dossiers : Le script récupère les fichiers à traiter dans un dossier d’entrée.
2- OCR et Classification : Chaque fichier est analysé, l’OCR extrait le texte, puis le modèle de machine learning détermine de quel type de document il s'agit (facture, RIB, pièce d’identité).
3- Stockage des fichiers : Les fichiers sont automatiquement déplacés dans des sous-dossiers du dossier de sortie en fonction de leur classification.
4- Notification : Une fois le processus terminé, un email est envoyé pour informer que les fichiers ont été classés avec succès.


Pour configurer votre mot de passe de votre adresse email, il faut une variable d'envrionnement. 
Pour windows il faut le faire dvia panneau de configuration ou set EMAIL_PASSWORD=votre_mot_de_passe
Pour linux ou macOS : export EMAIL_PASSWORD="votre_mot_de_passe_ici"


## 1 installation des bibliothèques

> pip install pytesseract opencv-python scikit-learn pandas nltk python-docx imaplib smtplib pdfplumber Pillow watchdog

pytesseract : Pour faire de l’OCR sur les documents scannés.
opencv-python : Pour la manipulation des images si besoin.
scikit-learn : Pour le modèle de classification.
pandas : Pour manipuler les données.
nltk : Pour traiter le texte.
python-docx : Pour générer des faux documents.
smtplib : Pour l’envoi d’emails.

Telecharger Pytesseract : https://github.com/UB-Mannheim/tesseract/wiki
sinon sur linux : sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-[lang] 

(Remplacer lang par fra pour francais et eng opur anglais)

Maintenant installer le > pip install pytesseract

