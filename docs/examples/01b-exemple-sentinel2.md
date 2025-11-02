# Exemple avancé : Données Sentinel-2 via Planetary Computer

**Durée estimée** : 5-10 minutes (+ téléchargement 30-60s)
**Prérequis** : Validation réussie avec [01a-validation-rapide.md](01a-validation-rapide.md)
**Objectif** : Télécharger et analyser des données satellite en temps réel depuis le cloud Microsoft

---

## Contexte

Le **Microsoft Planetary Computer** offre un accès gratuit à des pétaoctets de données satellite via l'API STAC (SpatioTemporal Asset Catalog).

Ce notebook montre comment :
- Authentifier et rechercher des images Sentinel-2
- Télécharger des bandes spectrales
- Calculer des statistiques avec pandas
- Visualiser avec seaborn

---

## Prérequis

- Librairies : `planetary-computer`, `pystac-client`, `pandas`, `seaborn`
- Connexion internet
- Compte Microsoft (optionnel)

---

## Étape 1 : Connexion au catalogue STAC

**Cellule 1** : Initialiser le client Planetary Computer

```python
import planetary_computer
from pystac_client import Client

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace
)
```

**Concepts clés** :
- **STAC** : Standard pour catalogues de données géospatiales
- **sign_inplace** : Authentifie automatiquement les URLs de téléchargement
- **Collection** : `sentinel-2-l2a` (niveau 2A = correction atmosphérique)

---

## Étape 2 : Récupération d'un item spécifique

Récupérer une image Sentinel-2 du catalogue

```python
item = catalog.get_collection("sentinel-2-l2a").get_item(
    "S2B_MSIL2A_20250824T185919_R013_T11UMT_20250824T224700"
)
```

---

## Étape 3 : Téléchargement et masquage

**Durée** : 30-60 secondes

Charger 4 bandes spectrales (B02, B03, B04, B08)

---

## Étape 4 : Statistiques avec pandas

Créer DataFrame avec Min, Max, Moyenne par bande

---

## Résultat attendu

✅ Connexion STAC réussie
✅ 4 bandes téléchargées
✅ Tableau statstics pandas affiché
✅ Composition RGB affichée

---

## Ressources

- [Planetary Computer Explorer](https://planetarycomputer.microsoft.com/explore)
- [Documentation STAC](https://stacspec.org/)
- [Sentinel-2 User Guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi)

---

**Analyse réussie ?** Continuez avec [3.5 Démarche complète](../formation/3.5-demarche-complete.md) !
