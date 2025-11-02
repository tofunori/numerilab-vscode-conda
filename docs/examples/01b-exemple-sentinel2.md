# Exemple avancé : Analyse Sentinel-2 avec NDVI

Durée estimée : **10-15 minutes**

---

## Objectif

Analyser une image Sentinel-2 réelle, calculer l'indice NDVI (Normalized Difference Vegetation Index) et créer des visualisations cartographiques.

---

## Prérequis

- ✅ Environnement validé avec [01a-validation-rapide.md](01a-validation-rapide.md)
- ✅ Jupyter en cours d'exécution
- ✅ Connexion internet (pour télécharger les données de démonstration)

---

## Concepts clés

### Qu'est-ce que Sentinel-2 ?

**Sentinel-2** est une constellation de satellites européens (Copernicus) qui capture des images multi-spectrales de la Terre avec résolution 10-60m. Chaque image contient 12 bandes spectrales couvrant :
- Visible (rouge, vert, bleu)
- Infrarouge proche (NIR)
- Infrarouge thermique et autres

### Qu'est-ce que l'NDVI ?

L'indice **NDVI** (Normalized Difference Vegetation Index) utilise deux bandes :
- **Infrarouge proche (NIR)** : Les plantes reflètent fortement le NIR
- **Rouge** : Les plantes absorbent fortement le rouge

**Formule** :
```
NDVI = (NIR - Red) / (NIR + Red)
```

**Interprétation** :
- -1.0 à 0.0 : Eau ou sol nu (peu de végétation)
- 0.0 à 0.4 : Végétation peu dense
- 0.4 à 1.0 : Végétation dense (forêts, cultures)

---

## Étape 1 : Lancer le notebook

Ouvrir [`01b-exemple-sentinel2-avance.ipynb`](../../exemples/01b-exemple-sentinel2-avance.ipynb) dans VSCode ou terminal Jupyter.

---

## Étape 2 : Importer les librairies

```python
import numpy as np
import rasterio
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from rasterio.plot import show

print("✓ Librairies chargées avec succès")
```

---

## Étape 3 : Charger les données Sentinel-2

Le notebook contient un raster Sentinel-2 fictif avec bandes B04 (rouge) et B08 (NIR).

```python
# Charger les bandes
with rasterio.open('donnees/sentinel2_demo.tif') as src:
    red = src.read(1).astype(float)  # Bande 4 (Rouge)
    nir = src.read(2).astype(float)  # Bande 8 (Infrarouge proche)
    bounds = src.bounds

print(f"Dimensions: {red.shape[0]} × {red.shape[1]} pixels")
print(f"Valeurs Red: [{red.min():.0f}, {red.max():.0f}]")
print(f"Valeurs NIR: [{nir.min():.0f}, {nir.max():.0f}]")
```

---

## Étape 4 : Calculer l'NDVI

```python
# Calculer NDVI
ndvi = (nir - red) / (nir + red + 1e-8)  # Éviter division par zéro

print(f"NDVI calculé")
print(f"  Min: {ndvi.min():.4f}")
print(f"  Max: {ndvi.max():.4f}")
print(f"  Moyenne: {ndvi.mean():.4f}")

# Classifier la végétation
eau_sol = (ndvi < 0.2).sum()
vegetation = (ndvi >= 0.2).sum()
total = ndvi.size

print(f"\nCouverture:")
print(f"  Eau/Sol: {100*eau_sol/total:.1f}%")
print(f"  Végétation: {100*vegetation/total:.1f}%")
```

---

## Étape 5 : Visualiser l'NDVI

### Carte NDVI colorée

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Carte NDVI
ndvi_plot = ax1.imshow(ndvi, cmap='RdYlGn', vmin=-0.5, vmax=1.0)
ax1.set_title('NDVI - Indice de Végétation', fontsize=14)
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
cbar1 = plt.colorbar(ndvi_plot, ax=ax1)
cbar1.set_label('NDVI')

# Histogramme NDVI
ax2.hist(ndvi.flatten(), bins=50, edgecolor='black', color='steelblue', alpha=0.7)
ax2.set_xlabel('Valeur NDVI')
ax2.set_ylabel('Fréquence (pixels)')
ax2.set_title('Distribution NDVI', fontsize=14)
ax2.axvline(ndvi.mean(), color='red', linestyle='--', linewidth=2, label=f'Moyenne: {ndvi.mean():.2f}')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Classification thématique

```python
# Créer classification
classification = np.zeros_like(ndvi, dtype=int)
classification[ndvi < -0.1] = 1  # Eau
classification[(ndvi >= -0.1) & (ndvi < 0.2)] = 2  # Sol nu
classification[ndvi >= 0.2] = 3  # Végétation

# Visualiser
fig, ax = plt.subplots(figsize=(12, 8))
colors_map = {
    1: (0, 0, 1),      # Bleu pour eau
    2: (0.8, 0.7, 0.4), # Beige pour sol
    3: (0, 0.8, 0)     # Vert pour végétation
}

im = ax.imshow(classification, cmap='tab10', vmin=0, vmax=3)
ax.set_title('Classification de couverture', fontsize=14)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Légende
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=(0, 0, 1), label='Eau'),
    Patch(facecolor=(0.8, 0.7, 0.4), label='Sol nu'),
    Patch(facecolor=(0, 0.8, 0), label='Végétation')
]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.show()
```

---

## Étape 6 : Générer un rapport

```python
# Sauvegarder rapport texte
report = f"""
RAPPORT ANALYSE SENTINEL-2
{'='*60}

DATE: 2025-10-15
IMAGE: Sentinel-2 L2A - Région test

STATISTIQUES NDVI
  Minimum: {ndvi.min():.4f}
  Maximum: {ndvi.max():.4f}
  Moyenne: {ndvi.mean():.4f}
  Écart-type: {ndvi.std():.4f}

COUVERTURE (pixels)
  Eau: {(classification == 1).sum():,} pixels ({100*(classification == 1).sum()/total:.1f}%)
  Sol nu: {(classification == 2).sum():,} pixels ({100*(classification == 2).sum()/total:.1f}%)
  Végétation: {(classification == 3).sum():,} pixels ({100*(classification == 3).sum()/total:.1f}%)

INTERPRÉTATION
  La région présente une couverture végétale variée avec des zones
  de sol nu et d'eau, typique d'une région agricole/urbaine mixte.
"""

print(report)

# Sauvegarder dans fichier
with open('resultats/rapport_sentinel2.txt', 'w') as f:
    f.write(report)

print("\n✓ Rapport sauvegardé: resultats/rapport_sentinel2.txt")
```

---

## Points clés

1. **Sentinel-2** fournit 12 bandes spectrales à haute résolution
2. **NDVI** combine bandes rouge et infrarouge pour analyser végétation
3. **Classification** convertit NDVI en catégories (eau, sol, végétation)
4. **Visualisation** rend les résultats accessibles et interprétables

---

## Résultat attendu

À la fin du notebook, vous devriez avoir :
- ✅ Carte NDVI colorée (rouge = faible, vert = fort)
- ✅ Histogramme montrant distribution NDVI
- ✅ Classification thématique en 3 classes
- ✅ Rapport texte avec statistiques

---

## Prochaines étapes

1. **Utiliser vraies données Sentinel-2** : Télécharger depuis [Copernicus Browser](https://browser.dataspace.copernicus.eu/)
2. **Ajouter autres indices** : NDSI (neige), NDBI (zones bâties), NDMI (humidité)
3. **Analyser séries temporelles** : Voir évolution NDVI sur mois/années
4. **Intégrer données vectorielles** : Croiser NDVI avec limites administratives (GeoPandas)

---

## Pour en savoir plus

- [Sentinel-2 Documentation](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi)
- [NDVI Tutorial](https://www.usgs.gov/faqs/what-normalized-difference-vegetation-index-ndvi)
- [Rasterio Documentation](https://rasterio.readthedocs.io)
- [Exemple complet (3.5)](../formation/3.5-demarche-complete.md)

---

✅ **Analyse réussie?** Continuez avec [3.5 Démarche complète](../formation/3.5-demarche-complete.md) pour intégrer tout dans un projet GitHub.

❓ **Questions?** Consultez [4. Ressources et annexes](../formation/4-ressources.md).
