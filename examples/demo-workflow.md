# Workflow complet : de l'installation à la première analyse

**Durée estimée** : 30 minutes
**Prérequis** : Lire les sections 2 et 3 du document de formation

---

## 📋 Scénario

Vous démarrez un **nouveau projet de cartographie** et vous voulez :
1. ✅ Configurer l'environnement Python isolé
2. ✅ Ouvrir le projet dans VSCode
3. ✅ Créer une première analyse (charger et visualiser un raster)
4. ✅ Sauvegarder sur GitHub

---

## Étape 1 : Préparer le dossier du projet (3 min)

### 1.1 Créer l'arborescence

Ouvrir **Command Prompt** ou **PowerShell** :

```bash
# Créer dossier projet
mkdir "D:\Projets\mon-projet-geo"
cd "D:\Projets\mon-projet-geo"

# Créer sous-dossiers
mkdir donnees
mkdir scripts
mkdir resultats
```

### 1.2 Vérifier Conda

```bash
conda --version
# Résultat attendu: conda 24.x.x
```

Si erreur, relancer le terminal.

---

## Étape 2 : Créer l'environnement Conda (5 min)

### 2.1 Créer l'environnement

```bash
conda create -n mon-geo python=3.11 -y
```

**-y** accepte automatiquement les installations.

### 2.2 Activer l'environnement

```bash
conda activate mon-geo
```

Vous verrez `(mon-geo)` au début de votre invite.

### 2.3 Installer packages géospatials

```bash
conda install -c conda-forge geopandas rasterio gdal -y
```

**Temps d'installation** : 5-10 min selon votre connexion.

### 2.4 Vérifier l'installation

```bash
python -c "import geopandas; print('✅ GeoPandas OK')"
python -c "import rasterio; print('✅ Rasterio OK')"
```

Résultat attendu :
```
✅ GeoPandas OK
✅ Rasterio OK
```

### 2.5 Exporter l'environnement

```bash
conda env export > environment.yml
```

Cela crée un fichier `environment.yml` que vous pouvez partager pour reproduire l'environnement.

---

## Étape 3 : Ouvrir le projet dans VSCode (2 min)

### 3.1 Ouvrir VSCode

```bash
# Depuis le terminal, dans le dossier projet
code .
```

VSCode ouvre le dossier `mon-projet-geo`.

### 3.2 Configurer l'interprète Python

1. **Ctrl+Shift+P** (Command Palette)
2. Taper : `Python: Select Interpreter`
3. Choisir votre `mon-geo` :
   ```
   ./miniforge3/envs/mon-geo/python.exe
   ```

### 3.3 Vérifier que Conda est actif dans le terminal VSCode

1. **Ctrl+`** (ouvrir terminal intégré)
2. Vérifier que vous voyez :
   ```
   (mon-geo) D:\Projets\mon-projet-geo>
   ```

Si pas de `(mon-geo)` :
```bash
conda activate mon-geo
```

---

## Étape 4 : Créer votre première analyse (10 min)

### 4.1 Créer fichier Python

1. Cliquer **New File** dans Explorateur (ou Ctrl+N)
2. Nommer : `analyse_ndvi.py`
3. Sauvegarder dans dossier `scripts/`

### 4.2 Écrire le code d'analyse

Copier-coller ce code :

```python
"""
Analyse NDVI simple
Charge un raster NDVI et calcule statistiques
"""

import numpy as np
import rasterio
from pathlib import Path

# Configuration
data_dir = Path("donnees")
output_dir = Path("resultats")

# Créer dossiers s'ils n'existent pas
output_dir.mkdir(exist_ok=True)

# Fichier exemple (à remplacer par vos données)
ndvi_file = data_dir / "ndvi_exemple.tif"

# Vérifier fichier existe
if not ndvi_file.exists():
    print(f"⚠️  Fichier non trouvé: {ndvi_file}")
    print("Créons un raster NDVI fictif pour la démo...")

    # Créer raster NDVI fictif (pour démo)
    from rasterio.transform import from_bounds

    # Données NDVI fictives (valeurs entre -1 et 1)
    ndvi_data = np.random.uniform(-0.5, 0.8, size=(256, 256)).astype(np.float32)

    # Métadonnées
    bounds = (-73.0, 45.0, -72.0, 46.0)  # Exemple: région Montréal
    transform = from_bounds(*bounds, 256, 256)

    # Écrire fichier
    with rasterio.open(
        ndvi_file,
        'w',
        driver='GTiff',
        height=256, width=256,
        count=1,
        dtype=ndvi_data.dtype,
        crs='EPSG:4326',
        transform=transform
    ) as dst:
        dst.write(ndvi_data, 1)

    print(f"✅ Raster créé: {ndvi_file}")

# Charger raster NDVI
with rasterio.open(ndvi_file) as src:
    ndvi = src.read(1)
    profile = src.profile

    print(f"\n📊 STATISTIQUES NDVI")
    print(f"  Shape: {ndvi.shape}")
    print(f"  Min: {ndvi.min():.4f}")
    print(f"  Max: {ndvi.max():.4f}")
    print(f"  Moyenne: {ndvi.mean():.4f}")
    print(f"  Écart-type: {ndvi.std():.4f}")

    # Compter pixels par catégorie
    n_eau = np.sum(ndvi < -0.1)
    n_sol = np.sum((ndvi >= -0.1) & (ndvi < 0.2))
    n_vegetation = np.sum(ndvi >= 0.2)

    print(f"\n🌍 COUVERTURE (approx.)")
    print(f"  Eau: {n_eau:,} pixels")
    print(f"  Sol nu: {n_sol:,} pixels")
    print(f"  Végétation: {n_vegetation:,} pixels")

    # Sauvegarder fichier rapport
    report = output_dir / "rapport_ndvi.txt"
    with open(report, 'w') as f:
        f.write("RAPPORT ANALYSE NDVI\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Min: {ndvi.min():.4f}\n")
        f.write(f"Max: {ndvi.max():.4f}\n")
        f.write(f"Moyenne: {ndvi.mean():.4f}\n")
        f.write(f"Écart-type: {ndvi.std():.4f}\n")
        f.write(f"\nCouverture:\n")
        f.write(f"  Eau: {n_eau:,}\n")
        f.write(f"  Sol nu: {n_sol:,}\n")
        f.write(f"  Végétation: {n_vegetation:,}\n")

    print(f"\n✅ Rapport sauvegardé: {report}")

print("\n🎉 Analyse complétée !")
```

### 4.3 Exécuter le code

1. **F5** pour run
2. Ou Terminal : `python scripts/analyse_ndvi.py`

Résultat attendu :
```
📊 STATISTIQUES NDVI
  Shape: (256, 256)
  Min: -0.4987
  Max: 0.7923
  Moyenne: 0.1234
  Écart-type: 0.3456

🌍 COUVERTURE (approx.)
  Eau: 12,345 pixels
  Sol nu: 34,567 pixels
  Végétation: 56,789 pixels

✅ Rapport sauvegardé: resultats/rapport_ndvi.txt

🎉 Analyse complétée !
```

---

## Étape 5 : Créer un Jupyter Notebook (5 min)

### 5.1 Créer notebook

1. Cliquer **New File** → nommer `exploration.ipynb`
2. VSCode crée un notebook vide

### 5.2 Ajouter cellules d'exploration

**Cellule 1** (code) :
```python
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from pathlib import Path

# Charger le raster
ndvi_file = Path("donnees/ndvi_exemple.tif")
with rasterio.open(ndvi_file) as src:
    ndvi = src.read(1)

print(f"NDVI shape: {ndvi.shape}")
print(f"NDVI range: [{ndvi.min():.2f}, {ndvi.max():.2f}]")
```

**Cellule 2** (code) :
```python
# Visualiser l'histogramme
plt.figure(figsize=(10, 5))
plt.hist(ndvi.flatten(), bins=50, edgecolor='black')
plt.xlabel("Valeur NDVI")
plt.ylabel("Fréquence")
plt.title("Distribution NDVI")
plt.grid(True, alpha=0.3)
plt.show()
```

**Cellule 3** (code) :
```python
# Visualiser la carte
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(ndvi, cmap='RdYlGn', vmin=-0.5, vmax=0.8)
plt.colorbar(im, ax=ax, label='NDVI')
ax.set_title("Carte NDVI")
plt.show()
```

Exécuter chaque cellule avec **Shift+Enter**.

---

## Étape 6 : Initialiser Git et GitHub (3 min)

### 6.1 Initialiser Git

Dans le terminal VSCode :

```bash
git init
git config user.name "Votre Nom"
git config user.email "votre.email@uqtr.ca"
```

### 6.2 Créer fichier `.gitignore`

Créer `.gitignore` à la racine du projet :

```
# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/

# Data
donnees/*.tif
donnees/*.shp
donnees/*.dbf

# Results
resultats/*.tif
resultats/*.csv

# IDE
.vscode/
.idea/
*.swp

# System
.DS_Store
Thumbs.db
```

### 6.3 Premier commit

```bash
git add .
git commit -m "Initialiser projet géomatique avec analyse NDVI"
```

### 6.4 Créer repo GitHub

1. Visiter [github.com/new](https://github.com/new)
2. Créer repository `mon-projet-geo`
3. Copier commands donnés par GitHub
4. Exécuter dans le terminal VSCode :

```bash
git branch -M main
git remote add origin https://github.com/votrecompte/mon-projet-geo.git
git push -u origin main
```

✅ Votre code est maintenant sur GitHub !

---

## Résumé du workflow

| Étape | Commande | Temps |
|-------|----------|-------|
| Créer dossier projet | `mkdir & cd` | 1 min |
| Créer environnement Conda | `conda create -n mon-geo ...` | 5 min |
| Installer packages | `conda install -c conda-forge ...` | 5 min |
| Ouvrir VSCode | `code .` | 1 min |
| Configurer interprète | Ctrl+Shift+P → Select Interpreter | 1 min |
| Créer analyse Python | Écrire script | 5 min |
| Créer notebook | Nouveau fichier `.ipynb` | 5 min |
| Initialiser Git | `git init && git config` | 1 min |
| Premier commit | `git add . && git commit` | 1 min |
| Pousser sur GitHub | `git push` | 1 min |
| **TOTAL** | | **25 min** |

---

## ✅ Checklist de validation

À la fin du workflow, vous devez avoir :

- [ ] Dossier projet avec structure claire
- [ ] Environnement Conda `mon-geo` créé et actif
- [ ] VSCode ouvert avec bon interprète Python
- [ ] Script Python exécutable
- [ ] Jupyter Notebook avec visualisations
- [ ] Fichier `environment.yml` pour reproduire l'env
- [ ] Dépôt Git local initialisé
- [ ] Dépôt GitHub public avec code pushé

---

## 🎓 Prochaines étapes

**Maintenant que votre workflow est en place :**

1. **Charger données réelles** : Remplacer le raster fictif par vos données
2. **Ajouter analyses** : Créer nouveaux scripts pour différentes analyses
3. **Documenter** : Ajouter comments et README au projet
4. **Collaborer** : Inviter collègues sur GitHub
5. **Versionner** : Faire commits réguliers pour tracer progrès

---

**Congratulations ! 🎉 Vous avez complété votre premier workflow géomatique professionnel !**
