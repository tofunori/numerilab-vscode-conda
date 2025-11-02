# Validation de l'environnement avec analyse NDSI

**Durée estimée** : 3-5 minutes (inclut téléchargement automatique)
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
# Configuration Google Drive
FILE_ID = "1ssjG8ZO4jP8U0bZ78jkDuotafv-Py3yH"
DATA_DIR = Path("../data")
```

**Résultat attendu** :
```
📥 Téléchargement de l'image Saskatchewan-Athabasca depuis Google Drive...
✅ Téléchargement terminé : ../data/saskatchewan_athabasca_clip.tif
   Taille : XX.X MB
```

---

## Prochaines étapes

Après validation réussie :

1. **Exemple avancé** : [01b-exemple-sentinel2-avance.md](01b-exemple-sentinel2.md)
2. **Projet complet** : [3.5 Démarche complète](../formation/3.5-demarche-complete.md)

---

**Validation réussie ?** Passez à [01b-exemple-sentinel2-avance.md](01b-exemple-sentinel2.md) pour accéder aux données cloud !
