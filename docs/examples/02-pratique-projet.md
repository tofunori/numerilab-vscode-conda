# Pratique : Mettre en place un projet complet

Durée estimée : **30-45 minutes**

---

## Objectif

Appliquer l'ensemble des concepts appris (Conda, VSCode, Git) pour créer un projet de géomatique complet, reproductible et versionné.

---

## Prérequis

- ✅ Environnement Conda configuré (section [2.4](../formation/2.4-conda-librairies.md))
- ✅ VSCode installé et configuré (section [3.2](../formation/3.2-vscode-extensions.md))
- ✅ Git installé (section [3.4](../formation/3.4-git-github.md))
- ✅ Avoir complété les exemples [01a](01a-validation-rapide.md) et [01b](01b-exemple-sentinel2.md)

---

## Vue d'ensemble du projet

Ce projet simule une **analyse NDVI d'une région agricole** :

```
mon-projet-ndvi/
├── data/                          # Données (gitignored)
│   └── sentinel2_demo.tif
├── scripts/                       # Scripts Python
│   ├── analyse_ndvi.py           # Script principal
│   └── utils.py                  # Fonctions utilitaires
├── notebooks/                     # Notebooks interactifs
│   └── exploration.ipynb         # Visualisations
├── resultats/                     # Sorties (gitignored)
│   ├── rapport_ndvi.txt
│   └── ndvi_map.png
├── environment.yml               # Dépendances Conda
├── .gitignore                    # Fichiers à ignorer
└── README.md                     # Documentation
```

---

## Étape 1 : Créer la structure de projet

### Créer le répertoire

```bash
# Terminal
mkdir mon-projet-ndvi
cd mon-projet-ndvi
```

### Créer les sous-dossiers

```bash
mkdir data scripts notebooks resultats
```

---

## Étape 2 : Créer l'environnement Conda

### Générer environment.yml

```bash
conda create --name ndvi-project python=3.11 geopandas rasterio numpy matplotlib jupyter -y
conda activate ndvi-project
conda env export > environment.yml
```

**Résultat attendu** : Fichier `environment.yml` avec toutes les dépendances

### Vérifier le fichier

```bash
cat environment.yml
```

Devrait contenir :

```yaml
name: ndvi-project
channels:
  - conda-forge
dependencies:
  - python=3.11
  - geopandas
  - rasterio
  - numpy
  - matplotlib
  - jupyter
  - ...
```

---

## Étape 3 : Ouvrir dans VSCode

```bash
code .
```

VSCode s'ouvre dans le dossier du projet. **Sélectionner l'interpréteur Python** :

1. Ctrl+Shift+P → "Python: Select Interpreter"
2. Choisir `ndvi-project`

---

## Étape 4 : Créer le script d'analyse

### Créer `scripts/analyse_ndvi.py`

```python
"""
Analyse NDVI d'une image Sentinel-2

Cet script :
1. Charge une image Sentinel-2 (bandes rouge et NIR)
2. Calcule l'indice NDVI
3. Classifie les pixels en 3 catégories
4. Génère un rapport avec statistiques
"""

import numpy as np
import rasterio
from pathlib import Path

# Configuration
DATA_PATH = Path("data/sentinel2_demo.tif")
RESULTS_PATH = Path("resultats")
RESULTS_PATH.mkdir(exist_ok=True)

def create_demo_data():
    """Créer données de démonstration si elles n'existent pas"""
    data_path = Path("data")
    data_path.mkdir(exist_ok=True)

    if DATA_PATH.exists():
        print(f"✓ Données trouvées: {DATA_PATH}")
        return

    print("⚠ Création de données de démonstration...")

    # Créer raster fictif
    np.random.seed(42)
    red = np.random.randint(0, 200, (100, 100), dtype=np.uint8)
    nir = np.random.randint(50, 255, (100, 100), dtype=np.uint8)

    # Écrire en tant que GeoTIFF multi-bande (mock)
    from rasterio.transform import Affine
    transform = Affine.identity()

    with rasterio.open(
        DATA_PATH, 'w',
        driver='GTiff',
        height=100, width=100,
        count=2, dtype=red.dtype,
        transform=transform
    ) as dst:
        dst.write(red, 1)  # Bande 1 : rouge
        dst.write(nir, 2)  # Bande 2 : NIR

    print(f"✓ Données créées: {DATA_PATH}")

def load_bands():
    """Charger bandes rouge et NIR"""
    with rasterio.open(DATA_PATH) as src:
        red = src.read(1).astype(float)
        nir = src.read(2).astype(float)

    return red, nir

def calculate_ndvi(red, nir):
    """Calculer NDVI = (NIR - Red) / (NIR + Red)"""
    ndvi = (nir - red) / (nir + red + 1e-8)  # Éviter division par zéro
    return ndvi

def classify_ndvi(ndvi):
    """Classifier NDVI en 3 catégories"""
    classification = np.zeros_like(ndvi, dtype=int)
    classification[ndvi < 0.2] = 1   # Eau/sol
    classification[(ndvi >= 0.2) & (ndvi < 0.5)] = 2  # Végétation faible
    classification[ndvi >= 0.5] = 3  # Végétation dense
    return classification

def generate_report(ndvi, classification):
    """Générer rapport texte avec statistiques"""
    water_soil = (classification == 1).sum()
    sparse_veg = (classification == 2).sum()
    dense_veg = (classification == 3).sum()
    total = ndvi.size

    report = f"""
RAPPORT ANALYSE NDVI
{'='*60}

STATISTIQUES NDVI
  Minimum: {ndvi.min():.4f}
  Maximum: {ndvi.max():.4f}
  Moyenne: {ndvi.mean():.4f}
  Écart-type: {ndvi.std():.4f}

COUVERTURE (pixels)
  Eau/Sol nu: {water_soil:,} pixels ({100*water_soil/total:.1f}%)
  Végétation faible: {sparse_veg:,} pixels ({100*sparse_veg/total:.1f}%)
  Végétation dense: {dense_veg:,} pixels ({100*dense_veg/total:.1f}%)

INTERPRÉTATION
  La région montre une distribution variée de couverture végétale.
  Les zones de végétation dense couvrent environ {100*dense_veg/total:.1f}% de la surface.
"""
    return report.strip()

def main():
    """Workflow complet"""
    print("\n📊 ANALYSE NDVI - Démarrage")
    print("-" * 60)

    # 1. Créer/charger données
    create_demo_data()

    # 2. Charger bandes
    print("\n📡 Chargement des bandes...")
    red, nir = load_bands()
    print(f"✓ Dimensions: {red.shape[0]} × {red.shape[1]} pixels")

    # 3. Calculer NDVI
    print("\n🌱 Calcul NDVI...")
    ndvi = calculate_ndvi(red, nir)
    print(f"✓ NDVI calculé ({ndvi.min():.3f} à {ndvi.max():.3f})")

    # 4. Classifier
    print("\n📊 Classification...")
    classification = classify_ndvi(ndvi)
    print("✓ Classification en 3 catégories")

    # 5. Générer rapport
    print("\n📝 Génération du rapport...")
    report = generate_report(ndvi, classification)

    # 6. Sauvegarder rapport
    report_path = RESULTS_PATH / "rapport_ndvi.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    # 7. Afficher rapport
    print("\n" + report)
    print(f"\n✓ Rapport sauvegardé: {report_path}")
    print("\n✅ Analyse terminée!")

if __name__ == "__main__":
    main()
```

### Tester le script

```bash
# Depuis le terminal VSCode (Ctrl+`)
conda activate ndvi-project
python scripts/analyse_ndvi.py
```

**Résultat attendu** :

```
📊 ANALYSE NDVI - Démarrage
------------------------------------------------------------

⚠ Création de données de démonstration...
✓ Données créées: data/sentinel2_demo.tif

📡 Chargement des bandes...
✓ Dimensions: 100 × 100 pixels

🌱 Calcul NDVI...
✓ NDVI calculé (-0.733 à 0.833)

📊 Classification...
✓ Classification en 3 catégories

📝 Génération du rapport...
...
✓ Rapport sauvegardé: resultats/rapport_ndvi.txt

✅ Analyse terminée!
```

---

## Étape 5 : Créer un Jupyter Notebook pour l'exploration

### Créer `notebooks/exploration.ipynb`

Depuis VSCode :

1. Créer nouveau fichier → `notebooks/exploration.ipynb`
2. Sélectionner kernel `ndvi-project`
3. Ajouter cellules :

**Cellule 1** : Imports

```python
import numpy as np
import rasterio
import matplotlib.pyplot as plt
from pathlib import Path

# Charger données
with rasterio.open('../data/sentinel2_demo.tif') as src:
    red = src.read(1).astype(float)
    nir = src.read(2).astype(float)

print(f"Chargé: {red.shape}")
```

**Cellule 2** : Calculer et visualiser NDVI

```python
# Calculer NDVI
ndvi = (nir - red) / (nir + red + 1e-8)

# Visualiser
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Carte NDVI
im1 = axes[0].imshow(ndvi, cmap='RdYlGn', vmin=-0.5, vmax=1.0)
axes[0].set_title('Carte NDVI')
plt.colorbar(im1, ax=axes[0])

# Histogramme
axes[1].hist(ndvi.flatten(), bins=30, edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Valeur NDVI')
axes[1].set_ylabel('Fréquence (pixels)')
axes[1].set_title('Distribution NDVI')
axes[1].axvline(ndvi.mean(), color='red', linestyle='--', label=f'Moyenne: {ndvi.mean():.2f}')
axes[1].legend()

plt.tight_layout()
plt.show()
```

---

## Étape 6 : Mettre en place Git et versionner

### Initialiser le dépôt Git

```bash
git init
git config user.name "Votre Nom"
git config user.email "votre.email@exemple.com"
```

### Créer `.gitignore`

```bash
# Fichier .gitignore
```

Ajouter :

```
# Données (trop volumineux)
data/*.tif
data/*.tiff
data/*.img

# Résultats
resultats/*.txt
resultats/*.png
resultats/*.jpg

# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# VSCode
.vscode/
*.code-workspace

# Conda/env
.env
venv/
```

### Créer README.md

```bash
```markdown
# Analyse NDVI - Projet Géomatique

Analyse de l'indice NDVI sur image Sentinel-2.

## Installation rapide

```bash
conda env create -f environment.yml
conda activate ndvi-project
python scripts/analyse_ndvi.py
```

## Structure

- `data/` : Données Sentinel-2
- `scripts/` : Scripts Python
- `notebooks/` : Notebooks Jupyter
- `resultats/` : Rapports et visualisations

## Auteur

Votre nom (année)
```

### Première validation et commit

```bash
# Vérifier les fichiers
git status

# Ajouter tous les fichiers (sauf .gitignore)
git add .

# Commit initial
git commit -m "Initial commit: projet NDVI avec structure complète

- Environnement Conda avec dépendances géospatiales
- Script d'analyse NDVI principal
- Notebook Jupyter pour exploration
- Données de démonstration
- README et documentation"
```

**Résultat attendu** :

```
[master (root-commit) abc1234] Initial commit: projet NDVI avec structure complète
 6 files changed, 250 insertions(+)
 create mode ...
```

---

## Étape 7 : Publier sur GitHub (optionnel)

### Créer un dépôt GitHub

1. Aller à [github.com/new](https://github.com/new)
2. Nommer le dépôt : `mon-projet-ndvi`
3. Ajouter description : "Analyse NDVI avec Sentinel-2"
4. **Ne pas** initialiser README (vous l'avez déjà)

### Pousser vers GitHub

```bash
git branch -M main
git remote add origin https://github.com/VOTRE_USERNAME/mon-projet-ndvi.git
git push -u origin main
```

### Vérifier sur GitHub

Aller à `https://github.com/VOTRE_USERNAME/mon-projet-ndvi`

---

## Résultat final

À la fin, vous avez :

✅ **Structure complète** : dossiers data, scripts, notebooks organisés
✅ **Environnement reproductible** : `environment.yml` pour cloner le projet
✅ **Analyse fonctionnelle** : script Python qui calcule NDVI
✅ **Exploration interactive** : Notebook Jupyter avec visualisations
✅ **Versionné** : Git + GitHub pour collaborer
✅ **Documenté** : README clair et instructions d'installation

---

## Prochaines étapes

1. **Améliorer le script** : Ajouter autres indices (NDSI, NDBI)
2. **Analyser vraies données** : Télécharger depuis [Copernicus Browser](https://browser.dataspace.copernicus.eu/)
3. **Collaborer** : Inviter collègues à cloner le dépôt
4. **Déployer** : Documenter résultats sur GitHub Pages (voir [3.5 Démarche complète](../formation/3.5-demarche-complete.md))

---

✅ **Projet terminé?** Vous maîtrisez maintenant Conda, VSCode, Git et GitHub pour des projets de géomatique professionnels!

❓ **Questions?** Consultez [4. Ressources et annexes](../formation/4-ressources.md).
