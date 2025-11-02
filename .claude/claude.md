# Instructions pour Claude Code - Projet Numérilab

## 🎯 Règles générales pour ce projet

### Vérification systématique du skill Numérilab

**IMPORTANT** : Avant de créer, modifier ou valider toute formation Numérilab, **TOUJOURS** vérifier la conformité avec le skill `numerilab-formation-builder`.

#### Quand vérifier ?
- ✅ Lors de la création d'une nouvelle formation
- ✅ Lors de la modification d'une section existante
- ✅ Lors de la révision/validation d'un document
- ✅ Avant de committer des changements sur une formation

#### Comment vérifier ?
```bash
# Activer le skill pour validation
/numerilab-formation-builder
```

#### Critères de conformité Numérilab

1. **Ton académique québécois** : Français québécois formel, vouvoiement, terminologie locale
2. **Structure pédagogique** : Problème → Solution → Exercice pratique
3. **Reproductibilité** : Exemples concrets, commandes copiables, environment.yml
4. **Niveau approprié** : Contexte d'abord, puis détails techniques
5. **Patterns obligatoires** :
   - ✅ Contexte/problème avant la solution
   - ✅ Au moins 2 approches comparées
   - ✅ Points de validation ("Résultat attendu:")
   - ✅ Exemples concrets du domaine (géomatique)
   - ✅ Tableaux de comparaison
   - ✅ Code avec commentaires
   - ✅ Ressources et références
   - ✅ Section troubleshooting

#### Terminologie obligatoire

**TOUJOURS utiliser les termes suivants** (terminologie québécoise académique) :

- ✅ **librairies** (et NON "paquets", "packages", "bibliothèques", "stack")
- ✅ **environnement** (et NON "env")
- ✅ **terminal** (et NON "console", "ligne de commande")

**Exemple correct** :
> "Installez les librairies géospatiales dans votre environnement conda via le terminal."

**Exemple incorrect** :
> "Installez les paquets géospatiaux dans votre env conda via la console."

### Structure de fichiers Numérilab

```
numerilab-*/
├── docs/
│   ├── formation-*.md          # Document principal
│   ├── formation-*.html        # Export HTML
│   └── images/                 # Captures d'écran
├── resources/
│   ├── environment.yml         # Stack conda
│   ├── settings.json           # Config VSCode
│   └── *.md                    # Guides annexes
├── exercices/                  # Exercices pratiques
└── README.md                   # Vue d'ensemble
```

## 📋 Checklist avant commit

- [ ] Conformité vérifiée avec skill numerilab-formation-builder
- [ ] Captures d'écran ajoutées si nécessaire
- [ ] Exemples testés et fonctionnels
- [ ] Commandes copiables (blocs code)
- [ ] Ton académique québécois respecté
- [ ] Structure pédagogique (problème-solution) respectée
- [ ] Points de validation présents
- [ ] Fichiers resources à jour (environment.yml, etc.)

## 🚫 À éviter

- ❌ Ne jamais supprimer de sections sans demander confirmation
- ❌ Ne pas utiliser de ton familier ou informel
- ❌ Ne pas créer de formations sans valider avec le skill
- ❌ Ne pas committer sans tester les commandes

## Émojis et symboles

**Symboles AUTORISÉS uniquement** :
- ★ ☞ ➜ ♦︎ ✸ ✤ ✓ ✦ 𖦹 ✎ ⃠ ● ⌨︎ ⚠︎

**AUCUN autre emoji** n'est autorisé dans la documentation, les notebooks, le code ou les commentaires.

## 🔗 Référence rapide

- Skill principal : `numerilab-formation-builder`
- Domaines : Géomatique, Python scientifique, R géospatial
- Public cible : Chercheurs universitaires (maîtrise/doctorat)
- Institution : UQTR, Québec
