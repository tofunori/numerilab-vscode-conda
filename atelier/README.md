# Matériel d'atelier - VSCode & Conda pour la géomatique

Ce dossier contient tous les fichiers nécessaires pour participer à l'atelier Numérilab sur VSCode et Conda.

## 📋 Contenu du dossier

### 1. Document de formation complet

- **[formation-vscode-conda.md](formation-vscode-conda.md)** - Document principal de l'atelier (90 minutes)
  - Couvre l'installation et la configuration de Conda
  - Guide d'utilisation de VSCode pour la géomatique
  - Intégration de Git et GitHub dans votre workflow

### 2. Notebooks Jupyter interactifs

Les notebooks suivants sont à exécuter dans l'ordre recommandé :

- **[notebooks/01a-validation-rapide.ipynb](notebooks/01a-validation-rapide.ipynb)** (2-3 min)
  - Vérifiez que votre environnement est correctement configuré
  - Test rapide des librairies géospatiales essentielles

- **[notebooks/01b-exemple-sentinel2-avance.ipynb](notebooks/01b-exemple-sentinel2-avance.ipynb)** (10-15 min)
  - Analyse d'images satellites Sentinel-2
  - Calcul d'indices de végétation (NDVI)
  - Manipulation de données raster

### 3. Exercices pratiques

- **[exercices/02-pratique-projet-complet.md](exercices/02-pratique-projet-complet.md)** (45 min)
  - Projet complet intégrant Conda, VSCode et Git
  - Création d'un workflow reproductible
  - Mise en pratique de toutes les notions

## 🚀 Avant de commencer

### Prérequis

Assurez-vous d'avoir installé :

1. **Conda** (Miniforge recommandé)
   - Téléchargement : https://github.com/conda-forge/miniforge

2. **VSCode**
   - Téléchargement : https://code.visualstudio.com/

3. **Git**
   - Téléchargement : https://git-scm.com/download

### Configuration de l'environnement

Créez un environnement conda avec les librairies géospatiales :

```bash
# Naviguez vers le dossier resources à la racine du projet
cd ../resources

# Créez l'environnement à partir du fichier environment.yml
conda env create -f environment.yml

# Activez l'environnement
conda activate geo-env
```

### Lancer les notebooks

Une fois l'environnement activé :

```bash
# Installez JupyterLab si ce n'est pas déjà fait
conda install -c conda-forge jupyterlab

# Lancez JupyterLab depuis le dossier notebooks
cd notebooks
jupyter lab
```

## 📖 Ordre recommandé

Pour tirer le meilleur parti de l'atelier, suivez cet ordre :

1. Lisez **formation-vscode-conda.md** pour comprendre les concepts
2. Exécutez **01a-validation-rapide.ipynb** pour valider votre installation
3. Pratiquez avec **01b-exemple-sentinel2-avance.ipynb** pour manipuler des données réelles
4. Complétez **02-pratique-projet-complet.md** pour intégrer tous les outils

## 💡 Ressources supplémentaires

- **Fichiers de configuration** : Voir le dossier `../resources/`
  - `environment.yml` : Définition complète de l'environnement conda
  - `settings.json` : Configuration VSCode optimale
  - `extensions-recommandees.md` : Liste des extensions VSCode utiles

- **Site web de formation** : https://tofunori.github.io/numerilab-vscode-conda/
  - Versions en ligne de tous les contenus
  - Navigation interactive par sections
  - Exemples et exercices

## ❓ Besoin d'aide ?

- Consultez la section troubleshooting dans `formation-vscode-conda.md`
- Visitez le site web pour les FAQ : https://tofunori.github.io/numerilab-vscode-conda/
- Ouvrez une issue sur GitHub : https://github.com/tofunori/numerilab-vscode-conda/issues

---

**Bon atelier!** 🎓
