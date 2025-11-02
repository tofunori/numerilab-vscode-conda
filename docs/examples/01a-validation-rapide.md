# Validation de l'environnement avec analyse NDSI

**Durée estimée** : 5-10 minutes (inclut téléchargement automatique)
**Prérequis** : Section 3.3 de la formation
**Objectif** : Vérifier que les librairies géospatiales fonctionnent avec une vraie image satellite

---

## 📦 Données requises

Ce notebook utilise une image Sentinel-2 de la région Saskatchewan-Athabasca (Canada).

**Téléchargement** : [Google Drive - saskatchewan_athabasca_clip.tif](https://drive.google.com/file/d/1ssjG8ZO4jP8U0bZ78jkDuotafv-Py3yH/view)
**Placement** : `atelier/data/saskatchewan_athabasca_clip.tif`

Le notebook téléchargera automatiquement les données lors de la première exécution.

---

## Contexte pédagogique

Ce notebook valide votre installation en analysant une vraie image satellite et en calculant l'indice **NDSI** (Normalized Difference Snow Index).

### Qu'est-ce que le NDSI ?

L'indice NDSI détecte la neige et la glace en comparant deux bandes spectrales :

- **Bande verte (B3)** : La neige reflète fortement le vert
- **Bande SWIR (B11)** : La neige absorbe l'infrarouge moyen

**Formule** :
```
NDSI = (Vert - SWIR) / (Vert + SWIR)
```

**Interprétation** :
- NDSI > 0.4 : Neige ou glace
- 0.0 < NDSI < 0.4 : Sol nu, roche
- NDSI < 0.0 : Végétation, eau

---

## Étape 1 : Lancer le notebook

### Option A : Depuis VSCode

1. Ouvrir [`01a-validation-rapide.ipynb`](https://github.com/tofunori/numerilab-vscode-conda/blob/main/atelier/notebooks/01a-validation-rapide.ipynb)
2. VSCode détecte l'extension `.ipynb` et active le support Jupyter
3. Cliquer **Select Kernel** en haut à droite
4. Choisir `geo-env` (ou votre environnement conda)

### Option B : Depuis terminal

```bash
# Activer environnement
conda activate geo-env

# Lancer Jupyter
jupyter notebook atelier/notebooks/01a-validation-rapide.ipynb
```

---

## Étape 2 : Téléchargement automatique

**Cellule 1** : Le script télécharge automatiquement l'image depuis Google Drive

```python
import os
import requests
from pathlib import Path

FILE_ID = "1ssjG8ZO4jP8U0bZ78jkDuotafv-Py3yH"
DATA_DIR = Path("../data")
FILE_PATH = DATA_DIR / "saskatchewan_athabasca_clip.tif"

DATA_DIR.mkdir(exist_ok=True)

if not FILE_PATH.exists():
    print("📥 Téléchargement de l'image Saskatchewan-Athabasca depuis Google Drive...")
    url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()

    with open(FILE_PATH, 'wb') as f:
        f.write(response.content)

    file_size_mb = FILE_PATH.stat().st_size / 1024 / 1024
    print(f"✅ Téléchargement terminé : {FILE_PATH}")
    print(f"   Taille : {file_size_mb:.1f} MB")
else:
    print(f"✅ Données déjà présentes : {FILE_PATH}")
```

**Résultat attendu** :
```
📥 Téléchargement de l'image Saskatchewan-Athabasca depuis Google Drive...
✅ Téléchargement terminé : ../data/saskatchewan_athabasca_clip.tif
   Taille : XX.X MB
```

---

## Étape 3 : Importations et configuration

**Cellule 2** : Importer les librairies géospatiales

```python
import numpy as np
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Configuration Jupyter
%matplotlib inline
plt.rcParams['figure.figsize'] = (14, 6)
```

---

## Étape 4 : Lecture des bandes spectrales

**Cellule 3** : Charger l'image Sentinel-2 et lire les bandes

```python
# Chemin du fichier
FILE_PATH = Path("../data/saskatchewan_athabasca_clip.tif")

# Ouvrir le fichier raster avec rasterio
with rasterio.open(FILE_PATH) as src:
    print(f"📊 Métadonnées de l'image :")
    print(f"  CRS : {src.crs}")
    print(f"  Dimensions : {src.height} x {src.width} pixels")
    print(f"  Nombre de bandes : {src.count}")
    print(f"  Type de données : {src.dtypes[0]}")

    # Lire les bandes
    # Sentinel-2 a 11 bandes : B2, B3, B4, B5, B6, B7, B8, B8A, B11, B12, SCL
    # Dans ce fichier : B3 (vert), B4 (rouge), B8 (NIR), B11 (SWIR)
    band_data = src.read()

    print(f"\n📈 Bandes présentes : {band_data.shape}")

# Extraire les bandes individuelles
green = band_data[0].astype(float)  # B3 - Vert
red = band_data[1].astype(float)    # B4 - Rouge
nir = band_data[2].astype(float)    # B8 - NIR
swir = band_data[3].astype(float)   # B11 - SWIR

print(f"\nBande Vert (B3) : min={green.min()}, max={green.max()}, mean={green.mean():.0f}")
print(f"Bande Rouge (B4) : min={red.min()}, max={red.max()}, mean={red.mean():.0f}")
print(f"Bande NIR (B8) : min={nir.min()}, max={nir.max()}, mean={nir.mean():.0f}")
print(f"Bande SWIR (B11) : min={swir.min()}, max={swir.max()}, mean={swir.mean():.0f}")
```

---

## Étape 5 : Correction de contraste

**Cellule 4** : Appliquer normalisation et correction de brillance

```python
def normalize_band(band, percentile_min=2, percentile_max=98):
    """Normaliser une bande en utilisant des percentiles pour rejeter les valeurs extrêmes"""
    vmin = np.percentile(band, percentile_min)
    vmax = np.percentile(band, percentile_max)

    normalized = np.clip((band - vmin) / (vmax - vmin), 0, 1)
    return normalized

def apply_gamma_correction(band, gamma=1.5):
    """Appliquer correction gamma pour améliorer le contraste visuel"""
    return np.power(band, 1/gamma)

# Normaliser toutes les bandes
green_norm = normalize_band(green)
red_norm = normalize_band(red)
nir_norm = normalize_band(nir)
swir_norm = normalize_band(swir)

# Appliquer correction gamma
green_gamma = apply_gamma_correction(green_norm, gamma=1.5)
red_gamma = apply_gamma_correction(red_norm, gamma=1.5)
nir_gamma = apply_gamma_correction(nir_norm, gamma=1.5)
swir_gamma = apply_gamma_correction(swir_norm, gamma=1.5)

print("✅ Normalisation et correction gamma appliquées")
```

**Explication** :
- **Percentiles** : Ignorer les 2% valeurs les plus basses et hautes (limiter l'effet des anomalies)
- **Normalisation min-max** : Mettre toutes les bandes sur l'échelle [0, 1]
- **Correction gamma** : Amplifier les tons moyens pour améliorer la visibilité (gamma > 1 assombrit, < 1 éclaircit)

---

## Étape 6 : Histogrammes et statistiques

**Cellule 5** : Afficher les histogrammes des bandes

```python
import seaborn as sns

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution spectrale des bandes Sentinel-2', fontsize=14, fontweight='bold')

# Histogrammes avec density estimation
sns.kdeplot(data=green.flatten(), ax=axes[0, 0], fill=True, color='green', alpha=0.6)
axes[0, 0].set_title('Bande 3 (Vert)')
axes[0, 0].set_xlabel('Réflectance')

sns.kdeplot(data=red.flatten(), ax=axes[0, 1], fill=True, color='red', alpha=0.6)
axes[0, 1].set_title('Bande 4 (Rouge)')
axes[0, 1].set_xlabel('Réflectance')

sns.kdeplot(data=nir.flatten(), ax=axes[1, 0], fill=True, color='brown', alpha=0.6)
axes[1, 0].set_title('Bande 8 (NIR)')
axes[1, 0].set_xlabel('Réflectance')

sns.kdeplot(data=swir.flatten(), ax=axes[1, 1], fill=True, color='orange', alpha=0.6)
axes[1, 1].set_title('Bande 11 (SWIR)')
axes[1, 1].set_xlabel('Réflectance')

plt.tight_layout()
plt.show()

# Tableau des statistiques
import pandas as pd

stats = pd.DataFrame({
    'Bande': ['Vert (B3)', 'Rouge (B4)', 'NIR (B8)', 'SWIR (B11)'],
    'Min': [green.min(), red.min(), nir.min(), swir.min()],
    'Max': [green.max(), red.max(), nir.max(), swir.max()],
    'Moyenne': [green.mean(), red.mean(), nir.mean(), swir.mean()],
    'Écart-type': [green.std(), red.std(), nir.std(), swir.std()]
})

print("\n📊 Tableau statistique des bandes :")
print(stats.to_string(index=False))
```

| Bande | Min | Max | Moyenne | Écart-type | Interprétation |
|-------|-----|-----|---------|------------|-----------------|
| Vert (B3) | 500 | 2000 | 1200 | 350 | Reflectance modérée (végétation + eau) |
| Rouge (B4) | 1500 | 3000 | 2100 | 450 | Plus haute reflectance en zones découvertes |
| NIR (B8) | 2000 | 5000 | 3500 | 800 | Forte reflectance (indicateur végétation) |
| SWIR (B11) | 1000 | 2500 | 1600 | 400 | Absorption par la neige, faible en eau |

---

## Étape 7 : Calcul et visualisation NDSI

**Cellule 6** : Calculer l'indice NDSI et afficher le résultat

```python
# Calcul NDSI = (Vert - SWIR) / (Vert + SWIR)
# Attention : Division par zéro quand (Vert + SWIR) = 0
denominator = green + swir
ndsi = np.divide(green - swir, denominator,
                 where=denominator!=0,
                 out=np.full_like(denominator, -999, dtype=float))

print(f"📊 Statistiques NDSI :")
print(f"  Min : {ndsi[ndsi > -999].min():.3f}")
print(f"  Max : {ndsi[ndsi > -999].max():.3f}")
print(f"  Moyenne : {ndsi[ndsi > -999].mean():.3f}")

# Visualiser NDSI
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Composition RGB (fausse couleur infrarouge)
rgb_image = np.stack([nir_gamma, red_gamma, green_gamma], axis=2)
ax1.imshow(rgb_image)
ax1.set_title('Composition RVB fausses couleurs (NIR-Rouge-Vert)', fontweight='bold')
ax1.axis('off')

# NDSI avec colormap
im = ax2.imshow(ndsi, cmap='RdYlGn', vmin=-0.5, vmax=0.8)
ax2.set_title('Indice NDSI (Normalized Difference Snow Index)', fontweight='bold')
ax2.axis('off')

cbar = plt.colorbar(im, ax=ax2, label='NDSI')
cbar.ax.axhline(y=0.4, color='blue', linestyle='--', linewidth=2, label='Seuil neige')

# Ajouter légende d'interprétation
legend_elements = [
    mpatches.Patch(facecolor='green', label='Végétation (NDSI < 0)'),
    mpatches.Patch(facecolor='yellow', label='Sol nu (0 < NDSI < 0.4)'),
    mpatches.Patch(facecolor='red', label='Neige/Glace (NDSI > 0.4)')
]
ax2.legend(handles=legend_elements, loc='lower left')

plt.tight_layout()
plt.show()

# Statistiques de classification
snow_pixels = np.sum(ndsi > 0.4)
bare_soil_pixels = np.sum((ndsi > 0.0) & (ndsi <= 0.4))
vegetation_pixels = np.sum(ndsi <= 0.0)
total_pixels = ndsi.size

print(f"\n📈 Classification des pixels :")
print(f"  Neige/Glace ({snow_pixels} pixels, {100*snow_pixels/total_pixels:.1f}%)")
print(f"  Sol nu ({bare_soil_pixels} pixels, {100*bare_soil_pixels/total_pixels:.1f}%)")
print(f"  Végétation ({vegetation_pixels} pixels, {100*vegetation_pixels/total_pixels:.1f}%)")
```

---

## Résultat attendu

✅ Connexion et lecture de l'image réussie
✅ 4 bandes spectrales chargées
✅ Histogrammes et statistiques affichés
✅ Composition RVB visualisée
✅ Indice NDSI calculé avec classification
✅ Pourcentages de neige/sol/végétation affichés

---

## Dépannage (Troubleshooting)

### FileNotFoundError: [Errno 2] No such file or directory

**Symptôme** :
```
FileNotFoundError: [Errno 2] No such file or directory: '../data/saskatchewan_athabasca_clip.tif'
```

**Solutions** :
1. Vérifier que la cellule de téléchargement a été exécutée sans erreur
2. Vérifier le chemin : `Path("../data/saskatchewan_athabasca_clip.tif").exists()`
3. Vérifier les permissions du dossier `atelier/data/`
4. Télécharger manuellement depuis Google Drive et placer le fichier

---

### ModuleNotFoundError: No module named 'rasterio'

**Symptôme** :
```
ModuleNotFoundError: No module named 'rasterio'
```

**Solutions** :
1. Vérifier l'environnement actif : `conda info | grep "active environment"`
2. Installer rasterio : `conda install -c conda-forge rasterio`
3. Redémarrer le kernel Jupyter : **Kernel > Restart**

---

### HTTPError 403 lors du téléchargement

**Symptôme** :
```
HTTPError: 403 Client Error: Forbidden for url: https://drive.google.com/uc?export=download&id=...
```

**Cause** : Lien Google Drive expiré ou permissions manquantes

**Solutions** :
1. Vérifier que le lien est publiquement accessible
2. Télécharger manuellement depuis : https://drive.google.com/file/d/1ssjG8ZO4jP8U0bZ78jkDuotafv-Py3yH/view
3. Placer le fichier dans `atelier/data/`

---

### Erreur de mémoire RAM lors de la charge

**Symptôme** :
```
MemoryError: Unable to allocate ... GiB for an array
```

**Solutions** :
1. Fermer les autres applications
2. Réduire les dimensions du raster : utiliser `rasterio.open()` avec `window` parameter
3. Traiter par tuiles plutôt que chargement complet

---

## Pour en savoir plus

**Concepts NDSI** :
- [USGS - Normalized Difference Snow Index](https://www.usgs.gov/faqs/what-normalized-difference-snow-index)
- [NASA Remote Sensing Tutorial](https://www.earthobservatory.nasa.gov/images/topic/snow-ice)

**Données Sentinel-2** :
- [Sentinel-2 User Guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi)
- [Sentinel-2 L2A Processing](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-2-msi/level-2a)

**Librairies géospatiales** :
- [Rasterio Documentation](https://rasterio.readthedocs.io/)
- [NumPy Array Operations](https://numpy.org/doc/stable/reference/arrays.html)
- [Matplotlib Colormaps](https://matplotlib.org/stable/tutorials/colors/colormaps.html)

**Pratique avancée** :
- [Band Math in Rasterio](https://github.com/rasterio/rasterio/blob/main/examples/band_math.py)
- [Géotraitement avec Python - Université Côte d'Azur](https://geodatascience.github.io/)

---

**Validation réussie ?** Continuez avec [01b-exemple-sentinel2-avance.md](01b-exemple-sentinel2.md) pour accéder aux données cloud !
