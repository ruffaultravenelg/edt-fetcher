# fetch.py
import requests
from info import LINK

# Ajouter un User-Agent pour imiter un navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

def fetch_data():
    try:
        # Fetcher le contenu XML
        response = requests.get(LINK, headers=headers)
        if not response.ok:
            print("Erreur lors de la récupération des données:")
            print(response.text)
            return False

        # Sauvegarder les données dans un fichier data.xml
        with open('data.xml', 'w', encoding='utf-8') as file:
            file.write(response.text)
        print("Données récupérées avec succès et enregistrées dans data.xml")
        return True
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False

if __name__ == "__main__":
    fetch_data()

