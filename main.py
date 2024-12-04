# main.py
import sys
from fetch import fetch_data
from clean import clean_data

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Si aucun argument n'est donné, fetch et clean
        if fetch_data():
            clean_data()
    elif len(sys.argv) == 2:
        # Si un argument est donné
        if sys.argv[1] == "fetch":
            fetch_data()
        elif sys.argv[1] == "clean":
            clean_data()
        else:
            print("Commande invalide. Utilisez 'fetch', 'clean', ou aucune commande.")
    else:
        print("Usage : python3 main.py [fetch|clean]")

