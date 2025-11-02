# Extensions VSCode recommandées

Guide détaillé des extensions essentielles pour développement en géomatique avec VSCode.

---

## Priorité 1 : OBLIGATOIRE

### Python (Microsoft)

**Pourquoi** : Support complet du langage Python, débogage, autocomplétion.

- **ID** : `ms-python.python`
- **Installe aussi** : Pylance (autocomplétion avancée)
- **Post-installation** :
  1. Ctrl+Shift+P → "Python: Select Interpreter"
  2. Choisir votre environnement Conda

**Utilité quotidienne** :
- Coloration syntaxique Python
- Débogage avec breakpoints
- Autocomplétion intelligente (via Pylance)
- Exécution de scripts

---

## Priorité 2 : HAUTEMENT RECOMMANDÉ

### Jupyter (Microsoft)

**Pourquoi** : Support natif des notebooks Jupyter dans VSCode.

- **ID** : `ms-toolsai.jupyter`
- **Éléments fournis** :
  - Création/édition de `.ipynb` directement
  - Exécution des cellules
  - Visualisation des outputs (graphiques, tableaux)
  - Kernel selection automatique

**Utilité** :
- Exploration interactive avec Jupyter
- Partage de notebooks exécutables
- Documentation avec mixes code/texte

### Pylance (Microsoft)

**Pourquoi** : Autocomplétion ultra-rapide et intelligence de code avancée.

- **ID** : `ms-python.vscode-pylance`
- **Fonctionnalités** :
  - Autocomplétion intelligente (IntelliSense)
  - Type hints visualization
  - Goto definition
  - Refactoring automatique

**Utilité** :
- Évite les erreurs de typage
- Accélère la programmation
- Suggestion contextuelles intelligentes

### GitLens (ErichBSchott)

**Pourquoi** : Visualisation Git améliorée directement dans l'éditeur.

- **ID** : `eamodio.gitlens`
- **Fonctionnalités** :
  - Blame (qui a écrit cette ligne et quand)
  - History (historique des changements)
  - Diff between commits
  - Repository explorer

**Utilité** :
- Comprendre l'historique du code
- Collaboration plus transparente
- Traçabilité rapide des modifications

---

## Priorité 3 : RECOMMANDÉ

### Data Wrangler (Microsoft)

**Pourquoi** : Exploration visuelle de dataframes Pandas.

- **ID** : `ms-toolsai.datawrangler`
- **Fonctionnalités** :
  - Preview des données en tableau
  - Filtrage et tri visuel
  - Génération de code Python automatique
  - Export en formats variés

**Utilité pour géomatique** :
- Inspectez rapidement les données vectorielles
- Explorez les attributs sans code
- Comprenez la structure des données avant analyse

### Better Comments (Aaron Bond)

**Pourquoi** : Coloration améliorée des commentaires.

- **ID** : `aaron-bond.better-comments`
- **Types de commentaires** :
  - `// !` → alerte (rouge)
  - `// ?` → question (bleu)
  - `// TODO` → à faire (orange)
  - `// *` → surligné (vert)

**Utilité** :
- Documentez votre code clairement
- Mettez en évidence les sections importantes
- Améliorez la lisibilité pour collaborateurs

### Markdown All in One (Yu Zhang)

**Pourquoi** : Support complet Markdown avec preview en temps réel.

- **ID** : `yzhang.markdown-all-in-one`
- **Fonctionnalités** :
  - Preview Markdown côte-à-côte
  - Table of contents auto
  - Formatting rapide
  - Snippets courants

**Utilité** :
- Écrivez README.md clairement
- Documentez vos analyses
- Partagez rapports formatés

---

## Utile pour géomatique spécifiquement

### Rainbow CSV

**Pourquoi** : Coloration des colonnes CSV pour lisibilité.

- **ID** : `mechatroner.rainbow-csv`
- **Utile pour** : Inspecter données CSV/TSV avant import GeoPandas

### GDAL (Tomáš Votruba)

**Pourquoi** : Syntax highlighting pour fichiers géospatiales.

- **ID** : `4source.gdal`
- **Supporte** : GeoJSON, WKT, OGR formats

### SVG (Jock)

**Pourquoi** : Preview et édition de fichiers SVG.

- **ID** : `jock.svg`
- **Utile pour** : Visualiser et modifier cartographies générées

---

## Productivité générale

### Code Spell Checker

**Pourquoi** : Détection d'erreurs orthographe en français.

- **ID** : `streetsidesoftware.code-spell-checker`
- **Langues** : Ajouter "French" dans settings

### TabNine (AutoComplete AI)

**Pourquoi** : Autocomplétion par AI (optionnel, Pylance souvent suffisant).

- **ID** : `TabNine.tabnine-vscode`
- **Alternative gratuite** : Pylance (recommandé)

---

## Installation rapide

Copier-coller ces ID dans l'onglet Extensions (Ctrl+Shift+X) :

```
ms-python.python
ms-toolsai.jupyter
eamodio.gitlens
aaron-bond.better-comments
yzhang.markdown-all-in-one
```

Ou via terminal :

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension eamodio.gitlens
code --install-extension aaron-bond.better-comments
code --install-extension yzhang.markdown-all-in-one
```

---

## Configuration recommandée dans settings.json

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "jupyter.kernels.filter": [],
  "[markdown]": {
    "editor.wordWrap": "on",
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "gitlens.hovers.currentLine.enabled": true,
  "gitlens.codeLens.enabled": true
}
```

---

## Désactiver les extensions non nécessaires

VSCode par défaut installe des extensions pour tous les langages. Pour géomatique, vous pouvez désactiver :
- C# (sauf si vous utilisez C#)
- Go, Rust, etc. (si ne vous en servez pas)

Cela accélère VSCode et réduit la consommation mémoire.

---

## Mise à jour des extensions

VSCode vérifie les mises à jour automatiquement. Vous verrez un badge de nombre dans l'onglet Extensions quand des mises à jour sont disponibles.

Recommandation : Mettre à jour mensuellement.

---

## Ressources

- [Marché VSCode Extensions](https://marketplace.visualstudio.com/)
- [Documentation Python Extension](https://github.com/microsoft/vscode-python)
- [Documentation Jupyter Extension](https://github.com/microsoft/vscode-jupyter)
- [Liste d'extensions populaires](https://marketplace.visualstudio.com/search?target=VSCode&category=All%20categories&sortBy=Installs)
