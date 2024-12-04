# 📅 Backend - Emploi du temps universitaire - IUT de Laval

Ce dépôt contient le **backend** permettant de gérer l'emploi du temps universitaire. Il s'occupe de la collecte, de l'analyse et de la transformation des données XML en JSON, prêtes à être utilisées par un frontend ou toute autre application.

Accessible depuis [edt.gemino.dev](https://edt.gemino.dev)

---

## ⚙️ Fonctionnalités

- **Récupération des données** : Télécharge les données d'emploi du temps au format RSS/XML depuis une source externe.
- **Nettoyage et transformation** : Analyse et nettoie les données pour les formater en un fichier JSON exploitable. Cela inclut :
  - Extraction des informations clés (date, heures, groupe, professeur, salle, etc.).
  - Normalisation des textes pour corriger les encodages défectueux.
- **Flexibilité** :
  - Récupération uniquement (`fetch`).
  - Nettoyage uniquement (`clean`).
  - Fonctionnement complet (`fetch` + `clean`).
- **Tâche automatisée** : Conçu pour être exécuté régulièrement via une tâche cron, garantissant des données toujours à jour.

---

## 📥 Utilisation

### 1. **Cloner le dépôt**
```bash
git clone https://github.com/ruffaultravenelg/edt-back.git
cd edt-back
```

### 2. **Configurer la source de données**
Définissez le lien vers le flux RSS/XML dans le fichier `info.py` sous la variable `LINK` :
```python
# info.py
LINK = 'https://example.com/path-to-xml'
```

### 3. **Commandes disponibles**
- **Récupérer et nettoyer les données (mode complet)** :
  ```bash
  python3 main.py
  ```
- **Récupérer uniquement les données XML** :
  ```bash
  python3 main.py fetch
  ```
- **Nettoyer uniquement les données XML pour produire le JSON** :
  ```bash
  python3 main.py clean
  ```

### 4. **Automatisation**
Intégrez le script à une tâche cron pour l'exécuter régulièrement.

Exemple : mise à jour quotidienne à 6h du matin :
```bash
0 6 * * * /usr/bin/python3 /chemin/vers/ton/script/main.py
```

---

## 📂 Sorties

- **`data.xml`** : Contient les données brutes récupérées depuis le flux XML.
- **`data.json`** : Contient les données nettoyées et transformées en JSON.

---

## 📄 Licence

Ce projet est sous licence [GNU GPL v3.0](LICENSE). Contributions bienvenues via pull requests ou issues !
