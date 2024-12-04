# clean.py
import xml.etree.ElementTree as ET
import json
import re

# Fonction pour formater correctement le nom du professeur
def format_professeur_name(name):
    if name is None:
        return None
    return name.lower().title()

# Fonction pour formater correctement le nom de la salle
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
    match_date_time = re.search(r"(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - (\d{2}:\d{2})", description)
    jour = match_date_time.group(1) if match_date_time else None
    heure_debut = match_date_time.group(2) if match_date_time else None
    heure_fin = match_date_time.group(3) if match_date_time else None

    match_groupe = re.search(r"Resources</b><br />([^<]+)", description)
    groupe = match_groupe.group(1) if match_groupe else None

    match_professeur = re.search(r"<br/>([^<]+)<br/>", description)
    professeur = match_professeur.group(1) if match_professeur else None

    match_salle = re.search(r"<br/>([^<]+)<br/><p><b>Comment", description)
    salle = match_salle.group(1) if match_salle else None

    return jour, heure_debut, heure_fin, groupe, professeur, salle

def clean_data():
    try:
        # Lire et parser le fichier XML
        tree = ET.parse('data.xml')
        root = tree.getroot()

        # Initialiser une liste pour stocker les événements
        events = []

        # Extraire les items du flux RSS
        for item in root.find("channel").findall("item"):
            description = item.find("description").text
            jour, heure_debut, heure_fin, groupe, professeur, salle = parse_description(description)

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

            events.append(event_data)

        # Enregistrer les données nettoyées dans un fichier JSON
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(events, f, indent=4)
        print("Données nettoyées avec succès et enregistrées dans data.json")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    clean_data()

