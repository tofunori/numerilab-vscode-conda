# Numérilab - VSCode & Conda

## Bienvenue dans cet atelier complet!

Cet atelier vous apprend à configurer et utiliser **Conda** et **VSCode** pour développer des projets de **géomatique** reproductibles et professionnels.

### Objectifs

À la fin de cet atelier, vous serez capable de :

- **Installer et gérer** Miniforge (distribution Conda)
- **Créer et isoler** des environnements Python pour chaque projet
- **Installer des librairies** géospatiales complexes (GDAL, GeoPandas, Rasterio)
- **Configurer VSCode** pour la géomatique
- **Utiliser Git et GitHub** pour versionner et collaborer
- **Rendre vos projets reproductibles** via `environment.yml`

### Structure de l'atelier

```
├── Formation (1h30)
│   ├── Conda - Gestion des environnements
│   ├── VSCode - Éditeur pour géomatique
│   ├── Git & GitHub - Traçabilité et collaboration
│
├── Exemples Pratiques (30 min)
│   ├── Validation rapide avec données Sentinel-2
│   ├── Exemple avancé : indice NDSI
│   └── Projet complet du début à la fin
```

### Démarrage rapide

#### Option 1 : Lire la formation complète
Consultez la [formation complète](formation/0-presentation.md) pour une explication détaillée de chaque concept.

#### Option 2 : Valider votre environnement rapidement
Avez-vous déjà Conda et VSCode? Lancez directement le [notebook de validation rapide](examples/01a-validation-rapide.md) (2-3 min).

#### Option 3 : Suivre un projet de bout en bout
Travaillez à travers le [projet complet guidé](examples/02-pratique-projet.md) (45 min) qui intègre Conda + VSCode + Git.

### Prérequis

- **Windows 10/11**, macOS, ou Linux
- **Connexion internet** (pour les téléchargements)
- ~2 GB d'espace disque libre
- **Aucune connaissance préalable requise** - nous commençons de zéro!

### Lectures recommandées

1. **Débutant complet** : Commencez par [1. Introduction](formation/1-introduction.md)
2. **Expérience Python** : Allez directement à [2. Conda](formation/2.1-conda-theorie.md)
3. **VSCode déjà utilisé** : Sautez à [3.4 Git & GitHub](formation/3.4-git-github.md)

### Qu'est-ce que vous apprendrez?

**Conda** - Pourquoi c'est indispensable pour la géomatique

- Gestion des dépendances C (GDAL, PROJ)
- Isolation des environnements
- Reproductibilité garantie

**VSCode** - L'éditeur parfait pour la data science

- Extensions essentielles
- Intégration Conda automatique
- Terminal intégré et Jupyter

**Git & GitHub** - Traçabilité et collaboration

- Version locale vs. sauvegarde cloud
- Commits avec messages explicites
- Workflow git simplifié

### Ressources fournies

| Ressource | Description |
|-----------|-------------|
| **environment.yml** | Fichier prêt à l'emploi avec toutes les librairies géospatiales |
| **settings.json** | Configuration VSCode optimale pour la géomatique |
| **Notebooks** | Exemples exécutables avec données réelles (Sentinel-2) |
| **Guides PDF** | Documentation téléchargeable offline |

### Déploiement du projet

Ce projet est hébergé sur [GitHub](https://github.com/tofunori/numerilab-vscode-conda) et accessible en ligne via cette documentation.

**Pour cloner et utiliser localement** :

```bash
git clone https://github.com/tofunori/numerilab-vscode-conda.git
cd numerilab-vscode-conda
conda env create -f resources/environment.yml
conda activate numerilab
code .
```

### Contribution

Trouvez une erreur? Une suggestion? [Contribuez sur GitHub](https://github.com/tofunori/numerilab-vscode-conda/issues)!

### Support

- **Questions sur le contenu** : Ouvrez une [discussion GitHub](https://github.com/tofunori/numerilab-vscode-conda/discussions)
- **Bug/erreur** : [Issues GitHub](https://github.com/tofunori/numerilab-vscode-conda/issues)
- **Améliorations** : Pull Requests bienvenues!

---

**Prêt à commencer?** → [Lancer la formation](formation/1-introduction.md)
