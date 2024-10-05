# 📅 Backend - Emploi du temps universitaire - IUT de Laval

Ce dépôt contient le **backend** responsable de la collecte, de l'analyse et de la transformation des données de l'emploi du temps universitaire. Le backend récupère quotidiennement les informations depuis une source au format XML et les convertit en un fichier JSON exploitable par le frontend (<https://github.com/ruffaultravenelg/edt-front.git>).

Accessible depuis [edt.gemino.dev](https://edt.gemino.dev)

## ⚙️ Fonctionnalités

- **Récupération des données** : Le backend récupère les données de l'emploi du temps sous forme de flux RSS/XML depuis une source externe.
- **Analyse des informations** : Les informations importantes (date, heures, groupe, professeur, salle, etc.) sont extraites à partir du contenu XML..
- **Transformation en JSON** : Une fois les données extraites, elles sont formatées et enregistrées dans un fichier JSON.
- **Tâche automatisée** : Le script est prévu pour être exécuté automatiquement chaque jour via une tâche cron, garantissant des informations toujours à jour.

## 📥 Utilisation

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/ruffaultravenelg/edt-back.git
   cd edt-back
   ```

2. **Configurer la source de données** :

   Le lien vers le flux XML doit être défini dans le fichier `info.py` sous la variable `LINK`.

   Exemple :

   ```python
   # info.py
   LINK = 'https://example.com/path-to-xml'
   ```

3. **Exécuter le script** :

   Par défaut, le fichier JSON sera sauvegardé sous le nom `data.json`. Il est possible de spécifier un autre nom pour le fichier en le passent un argument au script :

   ```bash
   python3 fetcher.py mon_fichier.json
   ```

4. **Automatisation** :

   Le script peut être intégré à une tâche cron sur un serveur afin de s'exécuter automatiquement chaque jour. Cela garantit une mise à jour régulière des données de l'emploi du temps.

   Exemple de configuration cron pour une exécution quotidienne à 6h du matin :

   ```bash
   0 6 * * * /usr/bin/python3 /chemin/vers/ton/script/fetcher.py /chemin/vers/ton/fichier/data.json
   ```

## 📄 Licence

Ce projet est sous licence [GNU GPL v3.0](LICENSE).
