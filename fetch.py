import requests
import xml.etree.ElementTree as ET
import json
import re
import sys
from info import LINK

# Fetcher le contenu XML
response = requests.get(LINK)
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
        "professeur": professeur,
        "salle": salle
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