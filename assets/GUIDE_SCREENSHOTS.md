# Guide des captures d'écran pour la formation

**Objectif** : Ce document liste toutes les captures d'écran recommandées pour enrichir la formation VSCode/Conda.

**Emplacement** : Toutes les captures doivent être sauvegardées dans `assets/screenshots/`

**Convention de nommage** : `section-nom-descriptif.png`
- Exemple : `conda-install-01-welcome.png`

---

## 📋 Captures essentielles (8 minimum)

### ⭐ PRIORITÉ 1 : Captures absolument nécessaires

| # | Fichier | Description | Où l'intégrer |
|---|---------|-------------|---------------|
| 1 | `conda-install-register.png` | ⚠️ **CRITIQUE** : Case "Register Miniforge3 as my default Python" cochée | docs/formation-vscode-conda.md → Section 2.2 |
| 2 | `conda-env-active.png` | Terminal montrant `(geo-env)` dans le prompt après activation | docs/formation-vscode-conda.md → Section 2.3 |
| 3 | `conda-verify-packages.png` | Python vérifiant `import geopandas` avec succès | docs/formation-vscode-conda.md → Section 2.4 |
| 4 | `vscode-interface-annotee.png` | Interface complète **annotée** (Sidebar, Explorateur, Éditeur, Terminal) | docs/formation-vscode-conda.md → Section 3.1 |
| 5 | `vscode-select-interpreter.png` | Menu "Python: Select Interpreter" avec `geo-env` visible | docs/formation-vscode-conda.md → Section 3.2 |
| 6 | `vscode-extensions.png` | Marketplace avec extension Python (Microsoft) | docs/formation-vscode-conda.md → Section 3.2 |
| 7 | `git-source-control.png` | Panneau Source Control avec fichiers à commiter | docs/formation-vscode-conda.md → Section 3.4 |
| 8 | `github-repo-final.png` | Repo GitHub avec code publié et visible | docs/formation-vscode-conda.md → Section 3.4 |

---

## 📋 Captures bonus utiles (4 supplémentaires)

### Si vous avez le temps, ajoutez ces captures pour enrichir la formation :

| # | Fichier | Description | Où l'intégrer |
|---|---------|-------------|---------------|
| 9 | `jupyter-notebook-vscode.png` | Notebook avec cellule de visualisation matplotlib | docs/formation-vscode-conda.md → Section 3.5 |
| 10 | `terminal-conda-commands.png` | Terminal montrant commandes conda essentielles (`create`, `activate`, `install`) | docs/formation-vscode-conda.md → Section 2.3 |
| 11 | `vscode-terminal-integrated.png` | Terminal intégré VSCode avec conda actif | docs/formation-vscode-conda.md → Section 3.3 |
| 12 | `workflow-complete.png` | Vue d'ensemble explorateur avec projet finalisé | examples/demo-workflow.md → Conclusion |

**Total recommandé** : 8-12 captures (8 minimum, 12 optimal)

---

## 🎨 Conseils pour prendre de bonnes captures

### Qualité technique

- **Format** : PNG (meilleure qualité pour screenshots)
- **Résolution** : 1920x1080 minimum (ou résolution native de votre écran)
- **Compression** : Minimale (PNG sans perte)
- **Taille** : Idéalement < 500 KB par image

### Composition

✅ **À faire** :
- Cadrer serré sur l'élément important
- Nettoyer les onglets/fenêtres inutiles avant capture
- Utiliser un thème clair OU sombre (cohérent dans toute la formation)
- Zoomer si texte trop petit
- Masquer informations personnelles (nom d'utilisateur si sensible)

❌ **À éviter** :
- Captures floues ou pixelisées
- Trop d'éléments distrayants
- Texte illisible
- Notifications/popups parasites

### Annotations (optionnel mais recommandé)

Outils recommandés pour annoter :
- **Windows** : Snip & Sketch (Win + Shift + S), Paint
- **macOS** : Screenshot tool (Cmd + Shift + 4), Preview
- **Multiplateforme** : Greenshot, ShareX

Annotations utiles :
- 🔴 Cercles rouges autour d'éléments clés
- ➡️ Flèches pointant vers boutons importants
- 📝 Numéros pour séquences d'étapes
- 💬 Texte explicatif court

---

## 📝 Checklist avant intégration

Avant d'intégrer vos captures dans les documents Markdown :

- [ ] Toutes les captures sont au format PNG
- [ ] Nommage cohérent selon convention (`section-nom.png`)
- [ ] Taille raisonnable (< 500 KB idéalement)
- [ ] Pas d'informations sensibles visibles
- [ ] Captures annotées si nécessaire (cercles, flèches)
- [ ] Captures sauvegardées dans `assets/screenshots/`
- [ ] Références ajoutées dans les fichiers Markdown

---

## 🔗 Intégration dans Markdown

### Syntaxe de base

```markdown
![Texte alternatif](../assets/screenshots/nom-fichier.png)
```

### Avec légende

```markdown
![Installation Miniforge](../assets/screenshots/conda-install-01-welcome.png)
*Figure 1 : Écran d'accueil de l'installeur Miniforge*
```

### Avec taille personnalisée (HTML)

```markdown
<img src="../assets/screenshots/vscode-interface-annotee.png" alt="Interface VSCode annotée" width="800">
*Figure 2 : Interface principale de VSCode avec annotations*
```

---

## ⚠️ Important : Git et taille des fichiers

**Recommandations** :
- Si captures > 2-3 MB au total : OK pour GitHub
- Si captures > 10 MB au total : Envisager Git LFS ou hébergement externe
- Compresser images avec TinyPNG ou similar avant commit

**Commandes Git après ajout captures** :

```bash
cd "D:\UQTR\Numérilab"

# Ajouter nouvelles captures
git add assets/screenshots/*.png

# Ajouter modifications aux documents Markdown
git add docs/*.md resources/*.md examples/*.md

# Commit
git commit -m "Ajouter captures d'écran pour formation VSCode/Conda

- XX captures pour section Conda
- XX captures pour section VSCode
- XX captures pour workflow exemple
- Annotations ajoutées aux points clés"

# Pousser sur GitHub
git push origin main
```

---

## 📊 Résumé

**Version allégée et réaliste pour 90 min de formation**

| Catégorie | Captures | Priorité |
|-----------|----------|----------|
| Conda essentiels | 3 | ⭐⭐⭐ OBLIGATOIRE |
| VSCode interface | 3 | ⭐⭐⭐ OBLIGATOIRE |
| Git/GitHub | 2 | ⭐⭐⭐ OBLIGATOIRE |
| **Sous-total minimum** | **8** | **CRITIQUE** |
| Jupyter Notebooks | 1 | ⭐⭐ Bonus |
| Terminal Conda | 1 | ⭐⭐ Bonus |
| Terminal intégré VSCode | 1 | ⭐⭐ Bonus |
| Workflow complet | 1 | ⭐⭐ Bonus |
| **Sous-total bonus** | **4** | **OPTIONNEL** |
| **TOTAL recommandé** | **8-12** | - |

✅ **Minimum viable** : 8 captures (20-30 min de travail)
✅ **Complet** : 12 captures (45-60 min de travail)

---

**Bon travail avec vos captures d'écran ! 📸**

Pour toute question, consultez ce guide ou référez-vous aux exemples dans les ateliers Numérilab existants.
