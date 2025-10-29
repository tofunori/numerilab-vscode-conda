# Extensions VSCode recommandées pour géomatique

## Extensions essentielles (installer en priorité)

### 1. **Python** (Microsoft)
- **ID** : `ms-python.python`
- **Utilité** : Support complet Python (intellisense, debugging, linting)
- **Installation** : Chercher "Python" dans Extensions et installer

### 2. **Jupyter** (Microsoft)
- **ID** : `ms-toolsai.jupyter`
- **Utilité** : Support Jupyter Notebooks interactifs dans VSCode
- **Installation** : Chercher "Jupyter" et installer

### 3. **Pylance** (Microsoft)
- **ID** : `ms-python.vscode-pylance`
- **Utilité** : Autocomplétion et type checking avancé
- **Dépend de** : Extension Python
- **Installation** : Installer automatiquement avec Python

---

## Extensions fortement recommandées

### 4. **GitLens** (GitKraken)
- **ID** : `eamodio.gitlens`
- **Utilité** : Visualisation Git avancée, blame, history
- **Installation** : Chercher "GitLens" et installer
- **Utilisation** : Voir autheur/date modifications en hover sur code

### 5. **Git Graph** (mhutchie)
- **ID** : `mhutchie.git-graph`
- **Utilité** : Visualisation arborescence commits et branches
- **Installation** : Chercher "Git Graph" et installer
- **Accès** : Cliquer icône Git Graph dans Source Control

### 6. **Thunder Client** (Ranga Vadhineni)
- **ID** : `rangav.vscode-thunder-client`
- **Utilité** : Tester APIs REST sans quitter VSCode
- **Installation** : Chercher "Thunder Client" et installer
- **Cas d'usage** : Tester services web géomatiques (GeoServer, etc.)

---

## Extensions optionnelles (selon préférences)

### 7. **GDAL Tools** (justinelliotmeyers)
- **ID** : `justinelliotmeyers.gdal-tools`
- **Utilité** : Syntax highlighting pour commandes GDAL
- **Installation** : Chercher "GDAL Tools" et installer

### 8. **Markdown All in One** (Yu Zhang)
- **ID** : `yzhang.markdown-all-in-one`
- **Utilité** : Support Markdown enrichi (TOC auto, preview)
- **Installation** : Chercher "Markdown All in One" et installer
- **Cas d'usage** : Écrire README.md et documentation

### 9. **Better Comments** (Aaron Bond)
- **ID** : `aaron-bond.better-comments`
- **Utilité** : Colorer commentaires (TODO, FIXME, NOTE)
- **Installation** : Chercher "Better Comments" et installer
- **Exemple** :
  ```python
  # TODO: Implémenter validation
  # FIXME: Bug détecté ici
  # NOTE: Important!
  ```

### 10. **Code Spell Checker** (Street Side Software)
- **ID** : `streetsidesoftware.code-spell-checker`
- **Utilité** : Vérifier l'orthographe dans code et commentaires
- **Installation** : Chercher "Code Spell Checker" et installer

### 11. **Even Better TOML** (tamasfe)
- **ID** : `tamasfe.even-better-toml`
- **Utilité** : Support TOML (fichiers config comme `pyproject.toml`)
- **Installation** : Chercher "Even Better TOML" et installer

### 12. **Docker** (Microsoft)
- **ID** : `ms-vscode.docker`
- **Utilité** : Gestion conteneurs Docker (si vous utilisez Docker)
- **Installation** : Chercher "Docker" et installer
- **Cas d'usage** : Environnements reproductibles pour géomatique

---

## Installation rapide (une extension à la fois)

### Méthode 1 : Via marketplace VSCode
1. **Ctrl+Shift+X** → Extensions
2. Chercher nom extension
3. Cliquer **Install**
4. Cliquer **Reload** si demandé

### Méthode 2 : Via terminal VSCode
```bash
# Installer une extension
code --install-extension ms-python.python

# Installer plusieurs extensions
code --install-extension ms-python.python \
     --install-extension ms-toolsai.jupyter \
     --install-extension eamodio.gitlens
```

---

## Configuration post-installation

Après installer les extensions principales :

### 1. Configurer interprète Python
1. **Ctrl+Shift+P**
2. Taper "Python: Select Interpreter"
3. Choisir votre `geo-env` :
   ```
   ./miniforge3/envs/geo-env/python.exe
   ```

### 2. Configurer Jupyter Kernel
1. Ouvrir fichier `.ipynb`
2. Cliquer **Select Kernel** en haut
3. Choisir `geo-env`

### 3. Copier settings.json
1. Créer dossier `.vscode` dans votre projet
2. Copier `resources/settings.json` → `.vscode/settings.json`
3. Cliquer **Reload** pour appliquer

---

## Personnalisation thème (optionnel)

### Installer un thème sombre
Recommandations populaires :
- **One Dark Pro** : Sombre, contrasté, agréable
- **Dracula** : Sombre, violet, moderne
- **Material Icon Theme** : Icônes colorées pour fichiers

Installation :
1. **Ctrl+Shift+X** → Extensions
2. Chercher "One Dark Pro"
3. Installer et sélectionner comme thème

---

## Troubleshooting extensions

| Problème | Cause | Solution |
|----------|-------|----------|
| Extension Python ne fonctionne pas | Python non détecté | **Ctrl+Shift+P** → "Python: Select Interpreter" |
| Jupyter notebooks vides | Kernel non sélectionné | Cliquer **Select Kernel** en haut notebook |
| GitLens montre erreurs | Git pas initialisé | **Terminal** → `git init` dans dossier projet |
| Extension perd configuration | Settings globaux vs workspace | Vérifier `.vscode/settings.json` du projet |

---

## Résumé : Stack minimal recommandé

**Pour commencer** (3 extensions) :
```
✅ Python (Microsoft)
✅ Jupyter (Microsoft)
✅ GitLens (GitKraken)
```

**Pour productivité optimale** (8 extensions) :
```
✅ Python (Microsoft)
✅ Jupyter (Microsoft)
✅ Pylance (Microsoft)
✅ GitLens (GitKraken)
✅ Git Graph (mhutchie)
✅ Thunder Client (Ranga Vadhineni)
✅ Markdown All in One (Yu Zhang)
✅ Better Comments (Aaron Bond)
```

---

**Conseil** : Installer progressivement et tester chaque extension pour comprendre son utilité. Ne pas surcharger VSCode ! 🎯
