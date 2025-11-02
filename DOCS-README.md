# Documentation MkDocs

Cette documentation est générée avec [MkDocs](https://www.mkdocs.org/) et le thème [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Installation locale

### Prérequis
- Python 3.11+
- pip

### Étapes

1. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

2. **Lancer le serveur local**
```bash
mkdocs serve
```

3. **Ouvrir dans le navigateur**
```
http://localhost:8000
```

Le serveur se relancera automatiquement quand vous modifiez les fichiers Markdown.

## Structure

```
docs/
├── index.md                    # Page d'accueil
├── formation/
│   ├── 0-presentation.md
│   ├── 1-introduction.md
│   ├── 2.x-*.md               # Sections Conda
│   ├── 3.x-*.md               # Sections VSCode
│   └── formation-vscode-conda.md  # Complet
├── examples/
│   └── *.md                    # Notebooks et guides
└── images/
    └── *.png                   # Captures d'écran
```

## Configuration

Le fichier `mkdocs.yml` à la racine contient :
- Métadonnées du site
- Thème Material avec palette sombre/clair
- Extensions Markdown
- Navigation et structure

## Déploiement

La documentation est déployée automatiquement sur **GitHub Pages** quand vous pushez sur la branche `master`.

### URL de production
```
https://tofunori.github.io/numerilab-vscode-conda/
```

### Workflow GitHub Actions
Le fichier `.github/workflows/deploy.yml` automatise le déploiement:
1. Build la doc avec MkDocs
2. Publie sur GitHub Pages
3. S'exécute à chaque push sur `master`

## Édition

### Ajouter une page
1. Créer un fichier `.md` dans le dossier approprié
2. Ajouter l'entrée dans `nav` dans `mkdocs.yml`
3. Committer et pousser

### Format Markdown supporté
- Headings, listes, tableaux
- Blocs de code avec coloration syntaxique
- Admonitions (note, warning, etc.)
- Emojis
- Attributs personnalisés

Voir [Material for MkDocs - Reference](https://squidfunk.github.io/mkdocs-material/reference/) pour la documentation complète.

## Conseil de contribution

Avant de pousser, testez localement :
```bash
mkdocs serve
# Vérifier http://localhost:8000
mkdocs build
# Vérifier qu'il n'y a pas d'erreurs
```

## Questions ?

Consultez la [documentation MkDocs](https://www.mkdocs.org/) ou [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
