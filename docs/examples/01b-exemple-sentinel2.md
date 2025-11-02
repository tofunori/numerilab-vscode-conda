# Exemple avancé : Données Sentinel-2 via Planetary Computer

**Durée estimée** : 15-20 minutes
**Prérequis** : Validation de l'environnement (01a)
**Objectif** : Accéder aux données satellite dans le cloud, analyser des bandes multispéctrales et calculer le NDVI

---

## Contexte pédagogique

### Pourquoi utiliser le Planetary Computer ?

Le **Microsoft Planetary Computer** est une plateforme cloud qui héberge des pétaoctets de données géospatiales publiques. Au lieu de télécharger des images satellite de plusieurs gigaoctets, vous accédez directement aux données via des API standardisées.

**Avantages** :
- Accès instantané sans téléchargement massif
- Catalogue actualisé en temps réel (nouvelles acquisitions Sentinel-2 quotidiennes)
- Traitement dans le cloud (réduction des coûts de stockage local)
- Standardisation STAC (SpatioTemporal Asset Catalog)

**Cas d'usage typiques** :
- Analyse multi-temporelle de végétation (NDVI saisonnier)
- Détection de changements (déforestation, urbanisation)
- Cartographie de surfaces (eau, neige, cultures)

### Qu'est-ce que le NDVI ?

Le **NDVI** (Normalized Difference Vegetation Index) est l'indice de végétation le plus utilisé en télédétection. Il exploite la signature spectrale caractéristique de la végétation :

- **Bande rouge (B04)** : Absorbée par la chlorophylle (réflectance faible)
- **Bande proche-infrarouge (B08)** : Fortement réfléchie par les feuilles (réflectance élevée)

**Formule** :
```
NDVI = (NIR - Rouge) / (NIR + Rouge)
```

**Interprétation** :

| Valeur NDVI | Interprétation | Exemples |
|-------------|----------------|----------|
| 0.8 à 1.0 | Végétation dense | Forêt tropicale, cultures matures |
| 0.6 à 0.8 | Végétation modérée | Prairies, forêt tempérée |
| 0.2 à 0.6 | Végétation éparse | Arbustes, végétation sèche |
| -0.1 à 0.2 | Sol nu, roche | Désert, surfaces urbaines |
| < -0.1 | Eau, nuages | Lacs, rivières, océans |

---

## Étape 1 : Importation des librairies

**Cellule 1** : Charger les dépendances pour l'accès cloud et l'analyse

```python
import rasterio
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import planetary_computer
from pystac_client import Client

# Configuration matplotlib pour affichage inline
%matplotlib inline
```

**Librairies utilisées** :

| Librairie | Rôle | Alternatives |
|-----------|------|--------------|
| `rasterio` | Lecture/écriture rasters géoréférencés | GDAL (plus complexe) |
| `pystac_client` | Recherche dans catalogues STAC | requests (manuel) |
| `planetary_computer` | Authentification SAS tokens | Accès sans signature (limité) |
| `pandas` | Analyse tabulaire de statistiques | NumPy pur (moins intuitif) |
| `matplotlib` / `seaborn` | Visualisation scientifique | Plotly (interactif) |

---

## Étape 2 : Connexion au Planetary Computer

**Cellule 2** : Établir la connexion au catalogue STAC

```python
# Connexion au Planetary Computer
catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace
)
print("Connexion au Planetary Computer réussie")
```

**Résultat attendu** :
```
Connexion au Planetary Computer réussie
```

**Explication technique** :
- **`Client.open()`** : Initialise une connexion au catalogue STAC via l'endpoint API
- **`modifier=planetary_computer.sign_inplace`** : Ajoute automatiquement des tokens SAS (Shared Access Signature) aux URLs pour accéder aux blobs Azure Storage

**Comparaison avec téléchargement direct** :

| Méthode | Temps initial | Coût stockage | Fraîcheur données |
|---------|---------------|---------------|-------------------|
| Téléchargement local | 10-30 min (10 GB) | Élevé (disque plein) | Statique (versions datées) |
| Accès cloud STAC | < 5 sec | Nul (streaming) | Temps réel (dernières acquisitions) |

---

## Étape 3 : Récupération d'un item Sentinel-2

**Cellule 3** : Sélectionner une acquisition spécifique

```python
# Récupérer un item Sentinel-2 spécifique
item = catalog.get_collection("sentinel-2-l2a").get_item(
    "S2B_MSIL2A_20250824T185919_R013_T11UMT_20250824T224700"
)
print(f"Item Sentinel-2 trouvé: {item.id}")

# Extraire les URLs des bandes spectrales
# B02=Bleu, B03=Vert, B04=Rouge, B08=NIR (Near Infrared)
bands = {k: item.assets[k].href for k in ['B02', 'B03', 'B04', 'B08']}
print(f"4 bandes spectrales récupérées")
```

**Résultat attendu** :
```
Item Sentinel-2 trouvé: S2B_MSIL2A_20250824T185919_R013_T11UMT_20250824T224700
4 bandes spectrales récupérées
```

**Anatomie de l'identifiant Sentinel-2** :

```
S2B_MSIL2A_20250824T185919_R013_T11UMT_20250824T224700
│   │       │               │    │      │
│   │       │               │    │      └─ Date de traitement (24/08/2025)
│   │       │               │    └─ Tuile UTM (Zone 11, grille UMT)
│   │       │               └─ Orbite relative (013)
│   │       └─ Date/heure d'acquisition (24/08/2025, 18:59:19 UTC)
│   └─ Niveau de traitement (L2A = correction atmosphérique)
└─ Satellite (S2A ou S2B)
```

**Bandes Sentinel-2 disponibles** :

| Code | Nom | Longueur d'onde | Résolution | Usage typique |
|------|-----|-----------------|------------|---------------|
| B02 | Bleu | 490 nm | 10 m | Bathymétrie, différenciation sol/végétation |
| B03 | Vert | 560 nm | 10 m | Vigueur végétation, turbidité eau |
| B04 | Rouge | 665 nm | 10 m | Absorption chlorophylle, NDVI |
| B08 | NIR | 842 nm | 10 m | Biomasse végétale, humidité sol |
| B11 | SWIR | 1610 nm | 20 m | Humidité végétation, neige (NDSI) |

---

## Étape 4 : Chargement des bandes avec masquage

**Cellule 4** : Télécharger les bandes et éliminer les pixels invalides

```python
print("Chargement: peut prendre 30-60 secondes")

# Charger la bande bleue (B02) et extraire les métadonnées
with rasterio.open(bands['B02']) as src:
    blue = src.read(1)              # Lire la première (et unique) bande
    transform = src.transform       # Transformation affine (géoréférencement)
    crs = src.crs                   # Système de coordonnées (ex: EPSG:32618 pour UTM Zone 18N)
    nodata = src.nodata             # Valeur représentant pixels invalides (nuages, ombres)
print(f"Bande bleue chargée (B02)")

# Charger les autres bandes (réutilise les métadonnées de B02)
with rasterio.open(bands['B03']) as src:
    green = src.read(1)
print(f"Bande verte chargée (B03)")

with rasterio.open(bands['B04']) as src:
    red = src.read(1)
print(f"Bande rouge chargée (B04)")

with rasterio.open(bands['B08']) as src:
    nir = src.read(1)
print(f"Bande NIR chargée (B08)")

# Masquer les valeurs NoData
mask = (blue != nodata) & (green != nodata) & (red != nodata) & (nir != nodata)

# Remplacer pixels invalides par NaN pour calculer les stats
blue_masked = np.where(mask, blue, np.nan)
green_masked = np.where(mask, green, np.nan)
red_masked = np.where(mask, red, np.nan)
nir_masked = np.where(mask, nir, np.nan)

print(f"\nToutes les bandes chargées et masquées")
print(f"   Dimensions: {red.shape[0]} × {red.shape[1]} pixels")
print(f"   Pixels valides: {np.sum(mask):,} / {mask.size:,} ({100*np.sum(mask)/mask.size:.1f}%)")
```

**Résultat attendu** :
```
Chargement: peut prendre 30-60 secondes
Bande bleue chargée (B02)
Bande verte chargée (B03)
Bande rouge chargée (B04)
Bande NIR chargée (B08)

Toutes les bandes chargées et masquées
   Dimensions: 10980 × 10980 pixels
   Pixels valides: 118,331,336 / 120,560,400 (98.2%)
```

**Explication du masquage** :

Le masquage élimine trois types de pixels problématiques :

1. **Nuages opaques** : Bloquent totalement le signal de surface (valeur NoData)
2. **Ombres de nuages** : Réduisent artificiellement la réflectance
3. **Pixels hors scène** : Zones sans données (bordures de tuile)

**Approche 1 : Masquage booléen (utilisée ici)** :
```python
mask = (blue != nodata) & (green != nodata) & (red != nodata) & (nir != nodata)
blue_masked = np.where(mask, blue, np.nan)
```

**Approche 2 : Utilisation de la bande SCL (Scene Classification Layer)** :
```python
# Sentinel-2 L2A inclut une bande SCL avec 11 classes
# 0=No Data, 1=Saturé, 3=Ombres nuages, 8=Nuages moyens, 9=Nuages élevés
scl = src.read(1)  # Bande SCL
mask = (scl == 4) | (scl == 5)  # 4=Végétation, 5=Sol nu
```

---

## Étape 5 : Statistiques descriptives avec Pandas

**Cellule 5** : Créer un tableau de statistiques pour chaque bande

```python
stats = pd.DataFrame({
    'Bande': ['Bleu', 'Vert', 'Rouge', 'NIR'],
    'Min': [np.nanmin(blue_masked), np.nanmin(green_masked), np.nanmin(red_masked), np.nanmin(nir_masked)],
    'Max': [np.nanmax(blue_masked), np.nanmax(green_masked), np.nanmax(red_masked), np.nanmax(nir_masked)],
    'Moyenne': [np.nanmean(blue_masked), np.nanmean(green_masked), np.nanmean(red_masked), np.nanmean(nir_masked)]
}).round(1)

stats
```

**Résultat attendu** :

| Bande | Min | Max | Moyenne |
|-------|-----|-----|---------|
| Bleu | 1.0 | 18144.0 | 1960.8 |
| Vert | 1.0 | 17472.0 | 2121.8 |
| Rouge | 203.0 | 17008.0 | 2080.1 |
| NIR | 1.0 | 16544.0 | 3114.8 |

**Interprétation** :

1. **Valeurs brutes Sentinel-2** : Les réflectances sont stockées en entiers 16-bit (0-10000 = 0-100% de réflectance)
2. **NIR élevé** : La moyenne NIR (3114.8) est 50% supérieure au rouge (2080.1), indiquant une présence significative de végétation active
3. **Bleu faible** : Cohérent avec l'absorption atmosphérique dans les courtes longueurs d'onde

**Point de validation** :
- Si NIR > Rouge : Zone végétalisée (forêt, prairies)
- Si Rouge > NIR : Zone urbaine, désertique ou eau

---

## Étape 6 : Visualisation RGB avec correction gamma

**Cellule 6** : Créer une composition en couleurs naturelles

```python
# Normalisation avec ajustement de brightness et gamma
def norm(band, brightness=1.2, gamma=1.6):
    """
    Normaliser une bande spectrale pour affichage visuel optimal

    Args:
        band: Tableau NumPy 2D contenant les valeurs de réflectance
        brightness: Multiplicateur de luminosité (>1 éclaircit)
        gamma: Exposant de correction gamma (>1 augmente contraste tons moyens)

    Returns:
        Tableau normalisé entre 0 et 1
    """
    # Étape 1 : Éliminer valeurs extrêmes (percentiles 2-98)
    p2, p98 = np.nanpercentile(band, (2, 98))
    normalized = np.clip((band - p2) / (p98 - p2), 0, 1)

    # Étape 2 : Appliquer brightness
    normalized = normalized * brightness
    normalized = np.clip(normalized, 0, 1)

    # Étape 3 : Appliquer gamma correction
    normalized = np.power(normalized, 1/gamma)

    return normalized

# Créer composition RGB avec ajustements
rgb = np.dstack([
    norm(red_masked, brightness=1.2, gamma=1.6),
    norm(green_masked, brightness=1.2, gamma=1.6),
    norm(blue_masked, brightness=1.2, gamma=1.6)
])

plt.figure(figsize=(10, 10))
plt.imshow(rgb)
plt.title('Sentinel-2 RGB (Couleurs naturelles)', fontsize=14, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()
```

**Résultat attendu** : Image composite RVB affichant le paysage en couleurs naturelles

**Comparaison des techniques de normalisation** :

| Technique | Avantages | Inconvénients | Cas d'usage |
|-----------|-----------|---------------|-------------|
| Min-Max simple | Rapide, intuitif | Sensible aux outliers | Données homogènes |
| Percentiles (2-98%) | Robuste aux extrêmes | Perd information dans queues de distribution | Scènes avec nuages résiduels |
| Standardisation Z-score | Préserve distribution | Pas borné [0,1] | Analyses statistiques |
| Gamma correction | Améliore contraste visuel | Subjectif (choix gamma) | Visualisation finale |

**Effet du paramètre gamma** :

- **gamma < 1** : Éclaircit les zones sombres (utile pour forêts denses)
- **gamma = 1** : Pas de correction (linéaire)
- **gamma > 1** : Assombrit les zones claires (réduit éblouissement zones arides)

---

## Étape 7 : Distribution spectrale avec Seaborn

**Cellule 7** : Analyser la densité de probabilité des valeurs de réflectance

```python
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

# Filtrer les NaN et sous-échantillonner pour performances
sample_size = 50000
blue_valid = blue_masked[~np.isnan(blue_masked)]
green_valid = green_masked[~np.isnan(green_masked)]
red_valid = red_masked[~np.isnan(red_masked)]
nir_valid = nir_masked[~np.isnan(nir_masked)]

blue_sample = np.random.choice(blue_valid, size=min(sample_size, blue_valid.size), replace=False)
green_sample = np.random.choice(green_valid, size=min(sample_size, green_valid.size), replace=False)
red_sample = np.random.choice(red_valid, size=min(sample_size, red_valid.size), replace=False)
nir_sample = np.random.choice(nir_valid, size=min(sample_size, nir_valid.size), replace=False)

# Kernel Density Estimation (KDE) pour courbes lissées
sns.kdeplot(blue_sample, color='blue', linewidth=2.5, bw_adjust=2, label='Bleu')
sns.kdeplot(green_sample, color='green', linewidth=2.5, bw_adjust=2, label='Vert')
sns.kdeplot(red_sample, color='red', linewidth=2.5, bw_adjust=2, label='Rouge')
sns.kdeplot(nir_sample, color='darkred', linewidth=2.5, bw_adjust=2, label='NIR')

plt.xlim(np.percentile(np.concatenate([blue_sample, green_sample, red_sample, nir_sample]), [1, 99]))
plt.title('Distribution des bandes spectrales Sentinel-2', fontsize=14, fontweight='bold')
plt.xlabel('Réflectance')
plt.ylabel('Densité de probabilité')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
```

**Résultat attendu** : Graphique KDE avec 4 courbes colorées montrant la distribution de chaque bande

**Interprétation des distributions** :

1. **Pic NIR décalé vers la droite** : Confirme la forte réflectance infrarouge de la végétation
2. **Chevauchement Bleu-Vert-Rouge** : Surfaces mixtes (sol nu + végétation éparse)
3. **Queue de distribution longue** : Présence de surfaces très réfléchissantes (toits métalliques, neige résiduelle)

**Pourquoi sous-échantillonner à 50,000 pixels ?**

- Image complète : 10,980 × 10,980 = 120,560,400 pixels
- Calcul KDE sur 120M points : Très lent (> 2 minutes)
- Échantillon de 50,000 : Représentatif statistiquement + rapide (< 5 secondes)

---

## Étape 8 : Calcul du NDVI

**Cellule 8** : Calculer et visualiser l'indice de végétation

```python
# Calcul NDVI = (NIR - Rouge) / (NIR + Rouge)
# Attention : Division par zéro quand (NIR + Rouge) = 0
denominator = nir_masked + red_masked
ndvi = np.divide(nir_masked - red_masked, denominator,
                 where=denominator!=0,
                 out=np.full_like(denominator, np.nan, dtype=float))

print(f"Statistiques NDVI :")
print(f"  Min : {np.nanmin(ndvi):.3f}")
print(f"  Max : {np.nanmax(ndvi):.3f}")
print(f"  Moyenne : {np.nanmean(ndvi):.3f}")
print(f"  Médiane : {np.nanmedian(ndvi):.3f}")

# Visualiser NDVI
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Composition RGB
ax1.imshow(rgb)
ax1.set_title('Composition RGB (Couleurs naturelles)', fontweight='bold')
ax1.axis('off')

# NDVI avec colormap
im = ax2.imshow(ndvi, cmap='RdYlGn', vmin=-0.2, vmax=0.9)
ax2.set_title('Indice NDVI (Normalized Difference Vegetation Index)', fontweight='bold')
ax2.axis('off')

# Barre de couleur avec annotation
cbar = plt.colorbar(im, ax=ax2, label='NDVI', shrink=0.8)
cbar.ax.axhline(y=0.6, color='blue', linestyle='--', linewidth=2)
cbar.ax.text(1.5, 0.6, 'Seuil végétation dense', va='center', fontsize=10)

plt.tight_layout()
plt.show()

# Classification automatique
water_clouds = np.sum(ndvi < 0.0)
bare_soil = np.sum((ndvi >= 0.0) & (ndvi < 0.2))
sparse_veg = np.sum((ndvi >= 0.2) & (ndvi < 0.6))
dense_veg = np.sum(ndvi >= 0.6)
total_pixels = np.sum(~np.isnan(ndvi))

print(f"\nClassification des pixels :")
print(f"  Eau/Nuages (< 0.0) : {100*water_clouds/total_pixels:.1f}%")
print(f"  Sol nu (0.0-0.2) : {100*bare_soil/total_pixels:.1f}%")
print(f"  Végétation éparse (0.2-0.6) : {100*sparse_veg/total_pixels:.1f}%")
print(f"  Végétation dense (> 0.6) : {100*dense_veg/total_pixels:.1f}%")
```

**Résultat attendu** :
```
Statistiques NDVI :
  Min : -0.421
  Max : 0.887
  Moyenne : 0.412
  Médiane : 0.456

Classification des pixels :
  Eau/Nuages (< 0.0) : 8.3%
  Sol nu (0.0-0.2) : 12.5%
  Végétation éparse (0.2-0.6) : 48.7%
  Végétation dense (> 0.6) : 30.5%
```

**Points de validation** :
- NDVI entre -1 et +1 (hors de cette plage = erreur de calcul)
- Moyenne positive (> 0.2) indique zone végétalisée
- Cohérence spatiale : Forêts en vert foncé, routes en rouge

---

## Extensions possibles

### Extension 1 : Analyse multi-temporelle (série chronologique NDVI)

**Objectif** : Détecter les changements saisonniers de végétation

```python
# Rechercher toutes les images Sentinel-2 d'une zone sur 6 mois
from datetime import datetime

search_bbox = [-123.5, 48.0, -122.5, 49.0]  # Vancouver, Canada
date_range = "2024-04-01/2024-10-01"

search = catalog.search(
    collections=["sentinel-2-l2a"],
    bbox=search_bbox,
    datetime=date_range,
    query={"eo:cloud_cover": {"lt": 20}}  # < 20% de nuages
)

items = list(search.items())
print(f"{len(items)} images trouvées")

# Calculer NDVI moyen pour chaque date
ndvi_timeseries = []
for item in items:
    red_url = item.assets['B04'].href
    nir_url = item.assets['B08'].href

    with rasterio.open(red_url) as src:
        red = src.read(1)
    with rasterio.open(nir_url) as src:
        nir = src.read(1)

    ndvi = (nir - red) / (nir + red + 0.0001)
    ndvi_mean = np.nanmean(ndvi)

    ndvi_timeseries.append({
        'date': item.datetime,
        'ndvi': ndvi_mean
    })

# Visualiser série temporelle
df = pd.DataFrame(ndvi_timeseries)
df.plot(x='date', y='ndvi', marker='o', figsize=(12, 4))
plt.title('Évolution du NDVI (Avril-Octobre 2024)')
plt.ylabel('NDVI moyen')
plt.xlabel('Date')
plt.grid(True)
plt.show()
```

### Extension 2 : Exportation en GeoTIFF géoréférencé

**Objectif** : Sauvegarder le NDVI pour utilisation dans QGIS/ArcGIS

```python
# Exporter NDVI avec géoréférencement
output_path = "ndvi_output.tif"

with rasterio.open(
    output_path,
    'w',
    driver='GTiff',
    height=ndvi.shape[0],
    width=ndvi.shape[1],
    count=1,
    dtype=ndvi.dtype,
    crs=crs,
    transform=transform,
    nodata=np.nan
) as dst:
    dst.write(ndvi, 1)
    dst.set_band_description(1, 'NDVI')

print(f"NDVI exporté : {output_path}")
print(f"   CRS : {crs}")
print(f"   Résolution : {transform.a} m/pixel")
```

### Extension 3 : Calcul d'autres indices spectraux

**NDWI** (Normalized Difference Water Index) :
```python
# NDWI = (Vert - NIR) / (Vert + NIR)
ndwi = (green_masked - nir_masked) / (green_masked + nir_masked + 0.0001)
# Valeurs > 0.3 : Eau
```

**NDBI** (Normalized Difference Built-up Index) :
```python
# Nécessite bande SWIR (B11)
with rasterio.open(bands['B11']) as src:
    swir = src.read(1)

# NDBI = (SWIR - NIR) / (SWIR + NIR)
ndbi = (swir - nir_masked) / (swir + nir_masked + 0.0001)
# Valeurs > 0.1 : Zones urbaines
```

---

## Dépannage (Troubleshooting)

### Erreur 1 : ConnectionError - Impossible de se connecter au Planetary Computer

**Symptôme** :
```
ConnectionError: HTTPSConnectionPool(host='planetarycomputer.microsoft.com', port=443):
Max retries exceeded with url: /api/stac/v1
```

**Causes possibles** :
1. Pas de connexion Internet active
2. Firewall bloquant l'accès à Azure
3. Planetary Computer en maintenance

**Solutions** :
1. Vérifier connexion : `ping planetarycomputer.microsoft.com`
2. Vérifier statut service : https://status.azure.com
3. Utiliser un proxy si derrière firewall institutionnel :
   ```python
   import os
   os.environ['HTTPS_PROXY'] = 'http://proxy.universite.ca:8080'
   ```
4. Temporiser avec téléchargement manuel depuis [Planetary Computer Explorer](https://planetarycomputer.microsoft.com/explore)

---

### Erreur 2 : ValueError - Division by zero in NDVI calculation

**Symptôme** :
```
RuntimeWarning: invalid value encountered in divide
ndvi = (nir - red) / (nir + red)
```

**Cause** : Pixels avec NIR + Rouge = 0 (zones masquées ou très sombres)

**Solutions** :

**Approche sécurisée 1 (utilisée dans étape 8)** :
```python
denominator = nir + red
ndvi = np.divide(nir - red, denominator,
                 where=denominator!=0,
                 out=np.full_like(denominator, np.nan, dtype=float))
```

**Approche sécurisée 2 (ajout d'epsilon)** :
```python
ndvi = (nir - red) / (nir + red + 1e-10)
```

**Approche sécurisée 3 (masquage préalable)** :
```python
valid_mask = (nir + red) > 0
ndvi = np.full_like(nir, np.nan)
ndvi[valid_mask] = (nir[valid_mask] - red[valid_mask]) / (nir[valid_mask] + red[valid_mask])
```

---

### Erreur 3 : MemoryError lors du chargement de grandes scènes

**Symptôme** :
```
MemoryError: Unable to allocate 4.35 GiB for an array with shape (10980, 10980) and data type float64
```

**Causes** :
- RAM insuffisante (< 8 GB disponible)
- Chargement simultané de multiples bandes en float64

**Solutions** :

**Solution 1 : Réduire la résolution avec fenêtrage** :
```python
# Charger seulement 1/4 de l'image
window = rasterio.windows.Window(0, 0, 5490, 5490)
with rasterio.open(bands['B04']) as src:
    red = src.read(1, window=window)
```

**Solution 2 : Utiliser dtype plus léger** :
```python
# float32 au lieu de float64 (divise par 2 l'usage RAM)
with rasterio.open(bands['B04']) as src:
    red = src.read(1, out_dtype='float32')
```

**Solution 3 : Traitement par blocs** :
```python
# Traiter par tuiles de 1024x1024
from rasterio.windows import Window

with rasterio.open(bands['B04']) as src:
    for i in range(0, src.height, 1024):
        for j in range(0, src.width, 1024):
            window = Window(j, i, 1024, 1024)
            red_block = src.read(1, window=window)
            # Traiter le bloc...
```

---

### Erreur 4 : HTTPError 403 Forbidden lors de l'accès aux bandes

**Symptôme** :
```
HTTPError: 403 Client Error: Forbidden for url: https://sentinel2l2a01.blob.core.windows.net/...
```

**Cause** : Token SAS expiré ou absent

**Solutions** :

1. **Vérifier que `modifier=planetary_computer.sign_inplace` est présent** :
   ```python
   catalog = Client.open(
       "https://planetarycomputer.microsoft.com/api/stac/v1",
       modifier=planetary_computer.sign_inplace  # ← ESSENTIEL
   )
   ```

2. **Régénérer les tokens si expirés (> 1h)** :
   ```python
   # Forcer signature manuelle
   signed_item = planetary_computer.sign(item)
   bands = {k: signed_item.assets[k].href for k in ['B02', 'B03', 'B04', 'B08']}
   ```

3. **Vérifier version de `planetary-computer`** :
   ```bash
   conda list planetary-computer
   # Si version < 1.0 : conda update planetary-computer
   ```

---

## Ressources et références

### Documentation officielle

**Planetary Computer** :
- [Catalogue STAC Explorer](https://planetarycomputer.microsoft.com/explore)
- [Data Catalog Documentation](https://planetarycomputer.microsoft.com/docs/overview/about)
- [API Reference](https://planetarycomputer.microsoft.com/api/stac/v1/docs)

**Sentinel-2** :
- [Sentinel-2 User Handbook](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi)
- [L2A Product Specification](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-2-msi/level-2a/algorithm)
- [Spectral Response Functions](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-2-msi/msi-instrument)

### Tutoriels avancés

**Analyse de séries temporelles** :
- [Earth Engine Timeseries Analysis](https://developers.google.com/earth-engine/tutorials/tutorial_api_04)
- [Python Geospatial Workflows](https://geohackweek.github.io/raster/)

**Indices de télédétection** :
- [Index Database (IDB)](https://www.indexdatabase.de/) - Répertoire de 500+ indices
- [USGS Spectral Indices Guide](https://www.usgs.gov/landsat-missions/landsat-surface-reflectance-derived-spectral-indices)

**Librairies géospatiales Python** :
- [Rasterio Documentation](https://rasterio.readthedocs.io/)
- [PySTAC Client Tutorial](https://pystac-client.readthedocs.io/en/stable/tutorials.html)
- [Xarray for Raster Stacks](https://xarray.pydata.org/en/stable/)

### Données alternatives

Si Planetary Computer est indisponible :

| Plateforme | Collections | Avantages | Inconvénients |
|------------|-------------|-----------|---------------|
| **Google Earth Engine** | Landsat, Sentinel, MODIS | Puissance calcul cloud | API JavaScript complexe |
| **AWS Open Data** | Sentinel-2 COGs | Gratuit, sans authentification | Pas de catalogue STAC intégré |
| **Copernicus Data Space** | Sentinel officiel | Archive complète depuis 2015 | Requiert compte ESA |
| **Element84 Earth Search** | Sentinel-2, Landsat | STAC natif, rapide | Couverture partielle |

**Exemple avec AWS Open Data** :
```python
# Accès direct sans authentification
import rasterio

aws_url = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/2024/S2B_MSIL2A_20240824T185919_R013_T11UMT_20240824T224700/B04.tif"
with rasterio.open(aws_url) as src:
    red = src.read(1)
```

---

**Prochaines étapes** : Explorez l'analyse multi-temporelle pour détecter les changements saisonniers de végétation !
