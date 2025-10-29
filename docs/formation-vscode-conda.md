# Introduction à VSCode et Conda pour la géomatique

**Durée** : 90 minutes
**Niveau** : Intermédiaire
**Formateur** : Numérilab UQTR
**Date** : Octobre 2025

---

## 📑 Table des matières

- [1. Introduction](#1-introduction)
- [2. Conda - Gestion des environnements (40 min)](#2-conda---gestion-des-environnements-40-min)
  - [2.1 Théorie et contexte](#21-théorie-et-contexte)
  - [2.2 Installation guidée](#22-installation-guidée)
  - [2.3 Création d'environnements](#23-création-denvironnements)
  - [2.4 Stack géospatial essentiels](#24-stack-géospatial-essentiels)
- [3. VSCode - Éditeur pour géomatique (45 min)](#3-vscode---éditeur-pour-géomatique-45-min)
  - [3.1 Prise en main de l'interface](#31-prise-en-main-de-linterface)
  - [3.2 Extensions essentielles](#32-extensions-essentielles)
  - [3.3 Terminal intégré et Conda](#33-terminal-intégré-et-conda)
  - [3.4 Git et GitHub](#34-git-et-github)
  - [3.5 Workflow complet](#35-workflow-complet)
- [4. Ressources et annexes](#4-ressources-et-annexes)

---

## 1. Introduction

### Contexte

Vous travaillez en **géomatique** et avez besoin de :
- Installer des packages complexes (GDAL, GeoPandas, Rasterio)
- Maintenir plusieurs projets avec des dépendances différentes
- Collaborer efficacement avec d'autres chercheurs
- Documenter et reproduire vos analyses

**Conda** et **VSCode** sont deux outils complémentaires qui répondent à ces besoins.

### Pourquoi Conda ?

**Python natif** est livré sans gestion d'environnements fiable. Les packages spécialisés (GDAL, Proj) requièrent une compilation correcte des dépendances.

**Conda** :
- ✅ Isole les environnements par projet
- ✅ Gère les dépendances C (GDAL, PROJ)
- ✅ Rend vos projets **reproductibles**
- ✅ Fonctionne sur Windows, macOS, Linux

### Pourquoi VSCode ?

**VSCode** :
- ✅ Léger et gratuit
- ✅ Extensions puissantes pour géomatique
- ✅ Terminal intégré détecte Conda automatiquement
- ✅ Git intégré pour collaboration
- ✅ Support Jupyter Notebooks natif

---

## 2. Conda - Gestion des environnements (40 min)

### 2.1 Théorie et contexte

#### Anaconda vs Miniforge

| Aspect | Anaconda | Miniforge |
|--------|----------|-----------|
| **Taille** | ~3 GB | ~150 MB |
| **Packages inclus** | ~250 packages | Minimal |
| **Vitesse installation** | Lente | Rapide |
| **License** | Commerciale | Open Source |
| **Recommandé pour** | Débutants | Professionnels |

**Recommandation** : Utilisez **Miniforge** pour les projets géospatiaux.

#### Alternatives à Conda

```yaml
Conda     : Gestion environnements + packages
Pip       : Seulement packages Python (pas dépendances C)
uv        : Alternative rapide à Pip (récent)
VENV      : Environnements Python seulement (limité)
Mamba     : Drop-in replacement Conda (plus rapide)
```

**Choix pour ce cours** : Conda avec canal `conda-forge`

#### Pourquoi isoler les environnements ?

Chaque projet peut avoir besoin de versions différentes du même package :

```
Projet A : GeoPandas 0.12 + GDAL 3.6
Projet B : GeoPandas 0.14 + GDAL 3.8
```

Sans isolation, installer GeoPandas 0.14 **casse** le Projet A.

Avec Conda :
```bash
conda activate projet-a   # GeoPandas 0.12
conda activate projet-b   # GeoPandas 0.14
```

Zéro conflit !

---

### 2.2 Installation guidée

#### Étape 1 : Télécharger Miniforge

1. Visiter [github.com/conda-forge/miniforge](https://github.com/conda-forge/miniforge)
2. Télécharger l'installeur pour votre système :
   - **Windows** : `Miniforge3-Windows-x86_64.exe`
   - **macOS Intel** : `Miniforge3-MacOSX-x86_64.sh`
   - **macOS Apple Silicon** : `Miniforge3-MacOSX-arm64.sh`
   - **Linux** : `Miniforge3-Linux-x86_64.sh`

#### Étape 2 : Installer

**Windows :**
- Double-cliquer l'exécutable
- Accepter la license
- Laisser chemin par défaut (ex: `C:\Users\YourName\miniforge3`)
- ✅ **IMPORTANT** : Cocher "Register Miniforge3 as my default Python"

**macOS/Linux :**
```bash
bash Miniforge3-MacOSX-x86_64.sh
# Suivre les prompts
source ~/miniforge3/bin/activate
```

#### Étape 3 : Vérifier l'installation

Ouvrir **Command Prompt** (Windows) ou **Terminal** (macOS/Linux) et taper :

```bash
conda --version
```

Résultat attendu :
```
conda 24.x.x
```

#### Étape 4 : Initialiser Conda

```bash
conda init
```

Cela crée un fichier de configuration qui active l'environnement de base au démarrage.

---

### 2.3 Création d'environnements

#### Créer un nouvel environnement

```bash
conda create -n geo-env python=3.11
```

**Explication** :
- `conda create` : créer un environnement
- `-n geo-env` : nom de l'environnement
- `python=3.11` : version Python spécifiée

#### Activer l'environnement

```bash
# Windows
conda activate geo-env

# macOS/Linux
source activate geo-env
```

Vous verrez `(geo-env)` au début de votre invite de commande.

#### Désactiver l'environnement

```bash
conda deactivate
```

Vous reveniez à l'environnement `(base)`.

#### Lister vos environnements

```bash
conda env list
```

Résultat :
```
# conda environments:
#
base                  *  C:\Users\YourName\miniforge3
geo-env                  C:\Users\YourName\miniforge3\envs\geo-env
```

---

### 2.4 Stack géospatial essentiels

#### Installer packages pour géomatique

```bash
conda activate geo-env

conda install -c conda-forge \
  geopandas \
  gdal \
  rasterio \
  folium \
  jupyter \
  matplotlib \
  numpy \
  pandas \
  scipy
```

**Packages clés expliqués** :

| Package | Utilité |
|---------|---------|
| **GeoPandas** | DataFrames avec géométries (vecteurs) |
| **GDAL** | Lecture/écriture formats raster et vecteur |
| **Rasterio** | Interface moderne pour données raster |
| **Folium** | Cartes interactives Leaflet |
| **Jupyter** | Notebooks interactifs |

#### Vérifier l'installation

```bash
python -c "import geopandas; print(geopandas.__version__)"
```

Résultat attendu :
```
0.14.x
```

#### Créer un fichier environment.yml

Pour **reproduire** l'environnement sur un autre ordinateur :

```bash
conda env export > environment.yml
```

Contenu du fichier (exemple) :
```yaml
name: geo-env
channels:
  - conda-forge
dependencies:
  - python=3.11
  - geopandas=0.14.0
  - gdal=3.8.0
  - rasterio=1.3.0
  - jupyter=1.0.0
  - matplotlib=3.8.0
  - numpy=1.24.0
```

#### Récréer l'environnement ailleurs

Quelqu'un d'autre peut recréer votre environnement avec :

```bash
conda env create -f environment.yml
```

**Avantage** : Reproductibilité garantie ! ✅

---

## 3. VSCode - Éditeur pour géomatique (45 min)

### 3.1 Prise en main de l'interface

#### Télécharger et installer VSCode

1. Visiter [code.visualstudio.com](https://code.visualstudio.com)
2. Télécharger pour votre système
3. Installer avec paramètres par défaut

#### Ouvrir un dossier projet

1. Ouvrir VSCode
2. **File** → **Open Folder**
3. Sélectionner votre dossier de projet géomatique
4. Cliquer **Select Folder**

#### Les panneaux principaux

```
┌─────────────────────────────────────────────┐
│ File Edit View Run Debug ... Help           │ Menu bar
├──┬──────────────────────────────────────────┤
│  │                                          │
│ 1│          3. Éditeur principal            │
│  │   (fichiers .py, .md, .json)             │
│  │                                          │
│  ├──────────────────────────────────────────┤
│  │ 4. Terminal intégré                      │
└──┴──────────────────────────────────────────┘

1. Sidebar gauche (Explorateur, Search, Extensions, etc.)
2. Panneau Explorateur (list fichiers)
3. Éditeur principal (code)
4. Terminal (intégré)
```

#### Les sections du Sidebar

Cliquer l'icône pour naviguer :

1. **Explorateur** (Ctrl+B) : Arborescence fichiers
2. **Search** (Ctrl+Shift+F) : Chercher dans tous fichiers
3. **Source Control** (Ctrl+Shift+G) : Git integration
4. **Run and Debug** (Ctrl+Shift+D) : Debugger Python
5. **Extensions** (Ctrl+Shift+X) : Installer packages VSCode

---

### 3.2 Extensions essentielles

#### Top 5 extensions pour géomatique

| Extension | Utilité | Installer |
|-----------|---------|-----------|
| **Python** | Support complet Python (Microsoft) | Obligatoire |
| **Jupyter** | Notebooks interactifs | Fortement recommandé |
| **Pylance** | Autocomplétion avancée | Recommandé |
| **GitLens** | Git visualization améliorée | Recommandé |
| **GDAL Tools** | Syntax highlighting GDAL | Optionnel |

#### Installer une extension

1. Ouvrir **Extensions** (Ctrl+Shift+X)
2. Chercher "Python" (par Microsoft)
3. Cliquer **Install**
4. Attendre installation et **Reload**

#### Configuration post-installation

Après installer l'extension Python :

1. Ouvrir **Command Palette** (Ctrl+Shift+P)
2. Taper "Python: Select Interpreter"
3. Choisir votre `geo-env` :
   ```
   ./env/Scripts/python.exe (geo-env)
   ```

Vérifier avec Python :
```python
import geopandas
print("Succès !")
```

---

### 3.3 Terminal intégré et Conda

#### Ouvrir le terminal intégré

```
Ctrl + `  (backtick)
```

ou **Terminal** → **New Terminal**

#### Vérifier que Conda est actif

```bash
conda --version
```

#### Activer votre environnement

```bash
conda activate geo-env
```

Vous verrez :
```
(geo-env) C:\Users\YourName\project >
```

#### Lancer Python interactif

```bash
python
```

```python
>>> import geopandas as gpd
>>> import rasterio
>>> print("Prêt pour la géomatique !")
Prêt pour la géomatique !
```

Quitter avec `exit()` ou Ctrl+D.

#### Lancer un Jupyter Notebook

```bash
jupyter notebook
```

Ou dans VSCode directement :
1. Créer fichier `analyse.ipynb`
2. Cliquer **Select Kernel**
3. Choisir `geo-env`
4. Commencer à coder !

---

### 3.4 Git et GitHub

#### Initialiser Git

Dans le terminal VSCode (avec `geo-env` actif) :

```bash
git init
```

#### Configurer Git (première fois)

```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@uqtr.ca"
```

#### Ajouter fichiers et committer

1. Ouvrir **Source Control** (Ctrl+Shift+G)
2. VSCode détecte automatiquement changements
3. Cliquer **+** pour "Stage" les fichiers
4. Entrer message commit
5. Cliquer ✓ pour committer

#### Connecter à GitHub

1. Visiter [github.com](https://github.com) et créer compte
2. Créer repository `numerilab-vscode-conda`
3. Copier URL du repo
4. Dans VSCode Terminal :
   ```bash
   git remote add origin https://github.com/votrecompte/numerilab-vscode-conda.git
   git branch -M main
   git push -u origin main
   ```

✅ Votre code est maintenant sur GitHub !

---

### 3.5 Workflow complet

#### Scénario réaliste

Vous créez une analyse de données raster :

**1. Créer fichier Python**
```python
# analyse_ndvi.py
import rasterio
import numpy as np
import geopandas as gpd

# Charger raster NDVI
with rasterio.open('donnees/ndvi.tif') as src:
    ndvi = src.read(1)

# Statistiques
print(f"Min: {ndvi.min()}, Max: {ndvi.max()}")
```

**2. Exécuter et tester**
- F5 pour run
- Ou Terminal : `python analyse_ndvi.py`
- Voir output

**3. Créer Jupyter Notebook pour exploration**
- Nouveau fichier `exploration.ipynb`
- Cells interactives avec visualisations

**4. Committer changements**
```bash
git add -A
git commit -m "Ajouter analyse NDVI avec stats de base"
git push
```

**5. Demander review sur GitHub**
- Ouvrir Pull Request
- Collecter feedback
- Merger dans `main`

---

## 4. Ressources et annexes

### Fichiers ressources

- **[environment.yml](../resources/environment.yml)** - Stack geospatial pré-configurée
- **[settings.json](../resources/settings.json)** - Configuration VSCode optimale
- **[extensions-recommandees.md](../resources/extensions-recommandees.md)** - Extensions détaillées

### Documentation officielle

- [Conda docs](https://docs.conda.io)
- [VSCode docs](https://code.visualstudio.com/docs)
- [GeoPandas](https://geopandas.org)
- [GDAL/OGR](https://gdal.org)
- [Rasterio](https://rasterio.readthedocs.io)

### Problèmes courants et solutions

| Problème | Cause | Solution |
|----------|-------|----------|
| `ModuleNotFoundError: No module named 'geopandas'` | Mauvais environnement Python | Vérifier interprète VSCode → `Python: Select Interpreter` |
| `conda: command not found` | Conda pas dans PATH | Relancer le shell ou terminal |
| GDAL installation échoue | Dépendances manquantes | Utiliser `conda-forge` channel |
| VSCode ne trouve pas Jupyter | Extension non installée | Installer extension Jupyter officielle |

### Points clés à retenir

✅ **Conda** isole chaque projet → pas de conflits de versions
✅ **environment.yml** rend projets **reproductibles**
✅ **VSCode** détecte automatiquement environnement Conda
✅ **Git/GitHub** permettent collaboration efficace
✅ **Extensions** VSCode augmentent productivité

### Prochaines étapes

1. ✅ Installer Miniforge
2. ✅ Créer `geo-env` avec GeoPandas
3. ✅ Configurer VSCode
4. ✅ Faire premier commit Git
5. ✅ Pousser sur GitHub
6. ✅ Commencer votre projet géomatique !

---

**Formation complétée !** 🎉

Pour questions : consultez les [ressources](../resources/) ou la [documentation officielle](https://docs.conda.io).
