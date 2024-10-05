import requests
import xml.etree.ElementTree as ET
import json
import re
import sys
from info import LINK

# Ajouter un User-Agent pour imiter un navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# Fetcher le contenu XML
response = requests.get(LINK, headers=headers)
rss_content = response.text

#Check response
if not response.ok:
    print("ERROR")
    print(response.text)
    exit()

# Parser le contenu XML
root = ET.fromstring(rss_content)

# Initialiser une liste pour stocker les événements
events = []

# Fonction pour formater correctement le nom
def format_professeur_name(name):
    if name is None:
        return None
    return name.lower().title()

# Fonction pour formater correctement la salle
def format_salle_name(name):
    if name is None:
        return None
    known_rooms = ["TP1", "TP2", "TP3", "TP4", "TD1", "TD2", "TDm1", "TDm2", "TDm3", "TDm4", "Amphi 2", "Amphi 1", "Amphi 3", "Amphi Le Balle"]
    for room in known_rooms:
        if room in name:
            return room
    return name

# Fonction pour extraire les informations de la description
def parse_description(description):
    # Extraire le jour et les heures
    match_date_time = re.search(r"(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - (\d{2}:\d{2})", description)
    jour = match_date_time.group(1) if match_date_time else None
    heure_debut = match_date_time.group(2) if match_date_time else None
    heure_fin = match_date_time.group(3) if match_date_time else None
    
    # Extraire le groupe, professeur, et salle
    match_groupe = re.search(r"Resources</b><br />([^<]+)", description)
    groupe = match_groupe.group(1) if match_groupe else None

    match_professeur = re.search(r"<br/>([^<]+)<br/>", description)
    professeur = match_professeur.group(1) if match_professeur else None

    match_salle = re.search(r"<br/>([^<]+)<br/><p><b>Comment", description)
    salle = match_salle.group(1) if match_salle else None

    return jour, heure_debut, heure_fin, groupe, professeur, salle

# Extraire les items du flux RSS
for item in root.find("channel").findall("item"):
    description = item.find("description").text
    
    # Extraire les informations depuis la description
    jour, heure_debut, heure_fin, groupe, professeur, salle = parse_description(description)
    
    # Créer un dictionnaire pour cet événement
    event_data = {
        "guid": item.find("guid").text,
        "titre": item.find("title").text,
        "jour": jour,
        "heure_debut": heure_debut,
        "heure_fin": heure_fin,
        "groupe": groupe,
        "professeur": format_professeur_name(professeur),
        "salle": format_salle_name(salle)
    }

    # Ajouter cet événement à la liste des événements
    events.append(event_data)

# Enregistre le JSON final
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'data.json'  # Valeur par défaut si aucun argument n'est fourni

with open(filename, 'w') as f:
    json.dump(events, f, indent=4)