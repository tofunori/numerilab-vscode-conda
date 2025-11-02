# Validation rapide de votre environnement

Durée estimée : **2-3 minutes**

---

## Objectif

Vérifier que votre environnement Conda avec librairies géospatiales est correctement installé et fonctionnel.

---

## Prérequis

- Miniforge/Conda installé (section [2.2](../formation/2.2-conda-installation.md))
- Environnement `geo-env` créé (section [2.3](../formation/2.3-conda-environnements.md))
- Librairies géospatiales installées (section [2.4](../formation/2.4-conda-librairies.md))
- VSCode ouvert avec terminal intégré

---

## Étape 1 : Lancer le notebook

### Option A : Depuis VSCode

1. Ouvrir le fichier [`01a-validation-rapide.ipynb`](https://github.com/tofunori/numerilab-vscode-conda/blob/main/atelier/notebooks/01a-validation-rapide.ipynb) depuis VSCode
2. VSCode détecte l'extension `.ipynb` et active le support Jupyter
3. Cliquer **Select Kernel** en haut à droite
4. Choisir `geo-env` (ou l'environnement que vous avez créé)

### Option B : Depuis terminal

```bash
# Activer environnement
conda activate geo-env

# Lancer Jupyter
jupyter notebook ../atelier/notebooks/01a-validation-rapide.ipynb
```

---

## Étape 2 : Exécuter les cellules

Chaque cellule teste une librairie.

**Cellule 1 : NumPy**
```python
import numpy as np
print(f"NumPy {np.__version__}")
```
**Résultat attendu** : `NumPy 1.24.x`

**Cellule 2 : GeoPandas**
```python
import geopandas
print(f"GeoPandas {geopandas.__version__}")
```
**Résultat attendu** : `GeoPandas 0.14.x`

**Cellule 3 : Rasterio**
```python
import rasterio
print(f"Rasterio {rasterio.__version__}")
```
**Résultat attendu** : `Rasterio 1.3.x`

**Cellule 4 : GDAL**
```python
from osgeo import gdal
print(f"GDAL {gdal.__version__}")
```
**Résultat attendu** : `GDAL 3.8.x`

**Cellule 5 : Folium (cartographie interactive)**
```python
import folium
# Créer une carte simple
m = folium.Map(location=[45.5, -73.6], zoom_start=10)
m.save('/tmp/test.html')
print("Carte créée avec succès !")
```
**Résultat attendu** : `Carte créée avec succès !`

---

## Résultat attendu

Si toutes les cellules s'exécutent sans erreur, votre environnement est **100% fonctionnel** pour la géomatique.

---

## Si une librairie ne s'importe pas

**Erreur** : `ModuleNotFoundError: No module named 'geopandas'`

**Solutions** :
1. Vérifier que `geo-env` est activée : `conda activate geo-env`
2. Relancer VSCode ou Jupyter
3. Réinstaller la librairie : `conda install geopandas`

Pour plus de débogage, voir section [4. Ressources et annexes](../formation/4-ressources.md).

---

## Prochaines étapes

Après validation réussie :
1. **Essayer un exemple avancé** : [01b-exemple-sentinel2-avance.ipynb](01b-exemple-sentinel2.md) (10-15 min)
2. **Suivre un projet complet** : Voir [3.5 Démarche complète](../formation/3.5-demarche-complete.md) (45 min)

---

**Validation réussie?** Vous êtes prêt pour la géomatique! Passez à [3.5 Démarche complète](../formation/3.5-demarche-complete.md).

**Erreur?** Consultez [4. Ressources et annexes - Problèmes courants](../formation/4-ressources.md).
