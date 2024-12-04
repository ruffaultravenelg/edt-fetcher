# 📅 Fetcher d'emploi du temps - Université

Ce dépôt contient un **script Python** permettant de gérer les emplois du temps universitaires. Le script télécharge les fichiers `.ics` pour une classe spécifique, les analyse et les convertit en un fichier JSON exploitable par un frontend ou d'autres applications.

Mon frontend peut être accessible a l'adresse suivante : [edt.gemino.dev](https://edt.gemino.dev)

---

## ⚙️ Fonctionnalités

- **Téléchargement des données** : Récupère les emplois du temps au format `.ics` depuis une URL spécifiée.
- **Analyse et transformation** : Convertit les données en JSON exploitable. Cela inclut :
  - Extraction des informations clés (date, heures, groupe, professeur, salle, etc.).
  - Normalisation des textes pour corriger les problèmes d'encodage.
  - Détection du type d'événement (ex. : cours magistral, travaux dirigés, travaux pratiques).
- **Flexibilité** : Permet de traiter les emplois du temps d'une classe donnée en ligne de commande.
- **Intégration facile** : Peut être exécuté manuellement ou automatiquement via une tâche cron.

---

## 📥 Utilisation

### 1. **Cloner le dépôt**
```bash
git clone https://github.com/ruffaultravenelg/edt-fetcher.git
cd edt-fetcher
```

### 2. **Configurer les liens des classes**
Définissez les URLs des emplois du temps dans un fichier `links.json`. Exemple :
```json
[
    {
        "classe": "21B",
        "url": "http://example.com/chemin-vers-ics-classe"
    },
    {
        "classe": "32D",
        "url": "http://example.com/chemin-vers-ics-classe"
    }
]
```

### 3. **Exécuter le script**
- **Télécharger et analyser l'emploi du temps d'une classe** :
  ```bash
  python3 main.py <nom_classe>
  ```
  Remplacez `<nom_classe>` par le nom de la classe, par exemple `21B`.

### 4. **Automatiser le script**
Intégrez le script dans une tâche cron pour maintenir les données à jour.

Exemple : Exécution quotidienne à 6h du matin :
```bash
0 6 * * * /usr/bin/python3 /chemin/vers/votre/script/main.py <nom_classe>
```

---

## 📂 Sortie

- **`data.json`** : Contient les données nettoyées et formatées au format JSON, prêtes à être utilisées.

---

## 🛠 Prérequis

- Python 3.x
- Dépendances :
  ```bash
  pip install requests icalendar
  ```

---

## 📄 Licence

Ce projet est sous licence [GNU GPL v3.0](LICENSE). Les contributions sont les bienvenues via des pull requests ou des issues !
