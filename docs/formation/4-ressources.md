# 4. Ressources et annexes

← [Section précédente](3.5-demarche-complete.md)

---

## Fichiers ressources

- [**environment.yml**](../resources/environment.yml) - Librairies géospatiales pré-configurées
- [**settings.json**](../resources/settings.json) - Configuration VSCode optimale
- [**extensions-recommandees.md**](../resources/extensions-recommandees.md) - Extensions détaillées

---

## Documentation officielle

- [Conda docs](https://docs.conda.io)
- [VSCode docs](https://code.visualstudio.com/docs)
- [GeoPandas](https://geopandas.org)
- [GDAL/OGR](https://gdal.org)
- [Rasterio](https://rasterio.readthedocs.io)

---

## Problèmes courants et solutions

| Problème | Cause | Solution |
|---------------------------|-------------------|---------------------------|
| `ModuleNotFoundError: No module named 'geopandas'` | Mauvais environnement Python | Vérifier interprète VSCode → `Python: Select Interpreter` |
| `conda: command not found` | Conda pas dans PATH | Relancer le shell ou terminal |
| GDAL installation échoue | Dépendances manquantes | Utiliser `conda-forge` channel |
| VSCode ne trouve pas Jupyter | Extension non installée | Installer extension Jupyter officielle |

---

## Points clés à retenir

- **Conda** isole chaque projet → pas de conflits de versions
- **environment.yml** rend projets **reproductibles**
- **VSCode** détecte automatiquement environnement Conda
- **Git/GitHub** permettent collaboration efficace
- **Extensions** VSCode augmentent productivité

---

## Prochaines étapes

1. Installer Miniforge
2. Créer `geo-env` avec GeoPandas
3. Configurer VSCode
4. Faire premier commit Git
5. Pousser sur GitHub
6. Commencer votre projet géomatique !

---

**Formation complétée !**

Pour questions : consultez les [ressources](../resources/index.md) ou la [documentation officielle](https://docs.conda.io).

---

← [Section précédente](3.5-demarche-complete.md)
