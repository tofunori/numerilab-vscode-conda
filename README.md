# Numérilab : Introduction à VSCode et Conda pour la géomatique

**Formation de 90 minutes** | *Numérilab UQTR*

## 📋 Présentation

Cet atelier vous guide à travers les outils essentiels pour démarrer un projet de géomatique :
- **Conda** : gestion des environnements Python isolés et reproductibles
- **VSCode** : éditeur de code configuré pour la science des données géospatiales

Designed pour **participants intermédiaires** avec une approche pédagogique interactive par démonstration.

---

## 🎯 Objectifs d'apprentissage

À la fin de cet atelier, vous serez capable de :

✅ Comprendre la différence entre Miniforge et Anaconda
✅ Créer et gérer des environnements conda isolés
✅ Installer des packages essentiels en géomatique (GDAL, GeoPandas, Rasterio)
✅ Naviguer et configurer VSCode
✅ Intégrer Git/GitHub dans votre workflow
✅ Utiliser les extensions VSCode pour améliorer la productivité

---

## 📚 Contenu

### 1. **Site web de formation**
- [`https://tofunori.github.io/numerilab-vscode-conda/`](https://tofunori.github.io/numerilab-vscode-conda/) - Formation en ligne interactive
- Navigation modulaire par sections (Conda, VSCode, Git)
- Exemples et exercices en format web

### 2. **Matériel d'atelier** (dossier [`atelier/`](atelier/))
- [`atelier/formation-vscode-conda.md`](atelier/formation-vscode-conda.md) - Document complet (90 min)
- [`atelier/notebooks/`](atelier/notebooks/) - Notebooks Jupyter exécutables
  - `01a-validation-rapide.ipynb` - Validation de l'environnement (2-3 min)
  - `01b-exemple-sentinel2-avance.ipynb` - Analyse Sentinel-2 (10-15 min)
- [`atelier/exercices/`](atelier/exercices/) - Exercices pratiques
  - `02-pratique-projet-complet.md` - Projet complet intégré (45 min)

### 3. **Ressources téléchargeables**
- [`resources/environment.yml`](resources/environment.yml) - Stack géospatial pré-configurée
- [`resources/settings.json`](resources/settings.json) - Configuration VSCode optimale
- [`resources/extensions-recommandees.md`](resources/extensions-recommandees.md) - Extensions essentielles

---

## 🚀 Avant de commencer

### Prérequis
- Windows 10+, macOS 10.15+, ou Linux
- 4 GB RAM minimum
- Connexion Internet pour téléchargements
- Terminal/Command Prompt accessible

### Installation rapide

1. **Télécharger Miniforge**
   ```bash
   # Visiter : https://github.com/conda-forge/miniforge
   ```

2. **Cloner ce projet**
   ```bash
   git clone https://github.com/votre-compte/numerilab-vscode-conda.git
   cd numerilab-vscode-conda
   ```

3. **Créer l'environnement**
   ```bash
   conda env create -f resources/environment.yml
   conda activate geo-env
   ```

4. **Ouvrir VSCode**
   ```bash
   code .
   ```

---

## 📖 Structure du projet

```
numerilab-vscode-conda/
├── README.md                          # Ce fichier
├── .gitignore                         # Fichiers à exclure de Git
├── mkdocs.yml                         # Configuration du site web MkDocs
│
├── docs/                              # 🌐 SITE WEB (MkDocs)
│   ├── formation/                     # Sections modulaires de la formation
│   ├── examples/                      # Exemples en format web (.md)
│   ├── resources/                     # Ressources documentées
│   └── about/                         # À propos et contribution
│
├── atelier/                           # 🎓 MATÉRIEL D'ATELIER
│   ├── README.md                      # Guide pour participants
│   ├── formation-vscode-conda.md      # Document complet (90 min)
│   ├── notebooks/                     # Notebooks Jupyter exécutables
│   │   ├── 01a-validation-rapide.ipynb
│   │   └── 01b-exemple-sentinel2-avance.ipynb
│   └── exercices/                     # Exercices pratiques
│       └── 02-pratique-projet-complet.md
│
└── resources/                         # 📦 RESSOURCES PARTAGÉES
    ├── environment.yml                # Stack Python géospatial
    ├── settings.json                  # Config VSCode recommandée
    └── extensions-recommandees.md     # Liste extensions
```

---

## 💡 Points clés à retenir

### Conda
- Chaque projet doit avoir son propre environnement isolé
- Les environnements se déclarent dans `environment.yml`
- Le fichier `environment.yml` rend le projet reproductible

### VSCode
- Les extensions doivent être installées **après** la configuration du workspace
- Le `settings.json` du workspace prime sur les paramètres globaux
- Le terminal intégré détecte automatiquement l'environnement actif

### Git & Collaboration
- Ne jamais placer le repo sur Google Drive ou OneDrive
- Utilisez le `.gitignore` pour exclure fichiers volumineux
- Un bon message de commit aide à retracer les changements

---

## ❓ Dépannage rapide

| Problème | Solution |
|----------|----------|
| `conda: command not found` | Conda n'est pas ajouté au PATH. Relancer le shell. |
| Python packages ne s'importent pas | Vérifier l'environnement actif : `conda activate geo-env` |
| VSCode n'affiche pas l'interprète Python | Ouvrir palette de commandes (Ctrl+Maj+P) → "Python: Select Interpreter" |
| Git non disponible dans VSCode | Installer Git : https://git-scm.com/download |

---

## 📞 Support et questions

- **Issues du projet** : Ouvrir une issue GitHub pour signaler un bug
- **Documentation Conda** : https://docs.conda.io
- **Documentation VSCode** : https://code.visualstudio.com/docs
- **GeoPandas docs** : https://geopandas.org

---

## 📄 Licence

Ce projet est sous licence **CC BY-NC-SA 4.0** (Creative Commons)

---

## ✍️ Auteur

**Présenté par** : Numérilab UQTR
**Dernière mise à jour** : 2025-10-29
**Durée** : 90 minutes

---

## 🔗 Ressources externes

- [Conda Documentation](https://docs.conda.io)
- [VSCode Documentation](https://code.visualstudio.com/docs)
- [GeoPandas](https://geopandas.org)
- [GDAL/OGR](https://gdal.org)
- [Rasterio](https://rasterio.readthedocs.io)

---

**Prêt à commencer ?** → Consultez [`docs/formation-vscode-conda.md`](docs/formation-vscode-conda.md)
