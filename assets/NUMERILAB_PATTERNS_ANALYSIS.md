# Analyse des patterns pédagogiques Numérilab
## Extrait des 20+ ateliers publiés

**Date d'analyse** : 29 octobre 2025
**Ateliers analysés** : GIT, Python, Quarto, Machine Learning, PARAFAC, Quarto (4 ateliers en détail)
**Objectif** : Établir templates réutilisables pour futures formations Numérilab

---

## 📊 Catégories d'ateliers identifiées

Le site Numérilab héberge 40+ ateliers dans 6 catégories principales :

### 1. **Stats & Modélisation** (9 ateliers)
- Machine Learning (initiation)
- Modèles non-linéaires
- Transition à l'analyse bayésienne
- Boruta (sélection variables)
- PARAFAC (1 & 2, analyse spectrale)
- Meta-analyses
- Resource selection function

### 2. **Programmation** (7 ateliers)
- **Introduction à Python** (2022-10)
- **Introduction à Git** (2023-12) ← Pattern analysé
- Introduction à R
- Fonctions et itération (R)
- Applications interactives R Shiny
- Manipulation de texte (stringr)
- Bases de données relationnelles (SQL)

### 3. **Exploration de données** (5 ateliers)
- Visualisation rapide (ggplot2)
- Manipulation rapide (dplyr)
- ggplot2 avancé
- Nettoyage et imputation
- DADA2 Pipeline

### 4. **Publication & Documentation** (1 atelier)
- **Introduction à Quarto** (2024-04) ← Pattern analysé

### 5. **Géospatial (GIS)** (2 ateliers)
- Introduction à Google Earth Engine
- Introduction à QGIS

### 6. **Autres** (2 ateliers)
- LLM & Keras
- NVivo (qualitative)

---

## 🎯 Patterns pédagogiques observés

### **Pattern 1 : Structure générale (tous les ateliers)**

```
1. INTRODUCTION (2-5 min)
   ├─ Contexte/motivation
   ├─ Pourquoi cet outil existe
   └─ Ce qu'on apprendra

2. THÉORIE & CONCEPTS (15-30 min)
   ├─ Définitions fondamentales
   ├─ Comparaisons (vs alternatives)
   ├─ Méthodologies existantes
   └─ Tableaux synthèse

3. MISE EN PLACE/INSTALLATION (5-10 min)
   ├─ Prérequis
   ├─ Installation étape par étape
   └─ Vérification fonctionnement

4. ATELIER PRATIQUE (45-60 min)
   ├─ Partie 1 : Approche A (Terminal, code brut, etc.)
   ├─ Partie 2 : Approche B (GUI, interface, etc.)
   └─ Étapes détaillées avec résultats attendus

5. RESSOURCES & CONCLUSION (5 min)
   ├─ Ressources externes
   ├─ Points clés à retenir
   └─ Prochaines étapes
```

### **Pattern 2 : Tone pédagogique (CRITIQUE)**

**❌ À ÉVITER (vulgarisation excessive)**
- Analogies simplistes ("Conda c'est une pizzeria")
- Emojis omniprésents
- Langage enfantin

**✅ À ADOPTER (académique conversationnel)**
- Narratif : "Vous avez probablement rencontré cette situation..."
- Problème → Solution : "Le problème que X résout"
- Tables comparatives avec 4-6 colonnes
- Exemples concrets du domaine (NDVI, spectroscopie, etc.)
- Langue québécoise naturelle (pas anglicismes évidents)
- Pas de "vous devez faire", mais "vous avez besoin de"

**Exemples de tone Numérilab :**

Git (Jessica Malko) :
> "Git c'est un système de contrôle des versions... applicable au développement de **logiciels** (comme l'écriture de code R pour l'analyse de vos données)."

Python (Charles Martin) :
> "Contrairement à R ou à MATLAB, [Python] n'a pas été conçu spécifiquement pour l'analyse et la visualisation de données."

Quarto (Charles Martin) :
> "Quarto permet de mélanger une panoplie de contenus dans un document (du texte, des équations, des images, du code, des graphiques, etc.)"

---

### **Pattern 3 : Structure narrative Intro**

Tous les ateliers commencent par **contextualiser le problème**, pas la solution :

```markdown
## 1. Introduction

### Contexte
- **Situation réelle** : Vous avez besoin de X
- **Problème actuel** : Y pose un défi
- **Qui doit savoir ça** : Chercheurs en [domaine], analystes, etc.

### Pourquoi cet outil ?
- ✅ Avantage 1
- ✅ Avantage 2
- ✅ Avantage 3
- (comparé implicitement aux alternatives)
```

**Exemples directs du site :**

Git intro (Jessica Malko) :
- Commence par MÉTHODOLOGIES (Waterfall, Agile, LEAN, DevOps)
- Puis VERSION CONTROL SYSTEM (le concept)
- ALORS seulement Git (l'outil)

Python intro (Charles Martin) :
- "Python est un langage général"
- "Contrairement à R, pas conçu pour données"
- "C'est pourquoi on utilise Colab et libraries comme pandas"

---

### **Pattern 4 : Théorie avec tableaux comparatifs**

**Tous les ateliers** incluent des tableaux 4-6 colonnes comparant :
- Git : centralisé vs distribué, branching, etc.
- Python : listes vs dicts vs arrays (NumPy)
- Quarto : inline vs display equations, etc.

**Numérilab VSCode/Conda a déjà adopté ce pattern :**

```markdown
| Aspect | Anaconda | Miniforge |
|--------|----------|-----------|
| Taille | 3 GB | 150 MB |
| Pre-installés | 250 packages | Aucun |
| License | Commerciale | Open Source |
```

---

### **Pattern 5 : Ateliers pratiques à 2-3 approches**

**Git (Jessica Malko)** :
- Partie 1 : Terminal (ligne de commande)
- Partie 2 : GitHub Desktop (GUI)

**Python (Charles Martin)** :
- Code inline dans Colab (cloud)
- Vs installation locale Anaconda (local)

**Pattern implicite :**
> "Montrer la façon "hardcore" (terminal), puis la façon accessible (GUI), pour que chacun trouve son confort."

---

### **Pattern 6 : Étapes numérotées + Points de validation**

Tous les ateliers pratiques incluent :

```markdown
### Étape 1 : [Action descriptive]
[Code/instructions]
**Point de validation** : Vous devriez voir...

### Étape 2 : [Action suivante]
```

**Exemple Git (Jessica) :**
```
### Étape 3 : Vérifier répertoire
`pwd`
Point de validation : Terminal affiche le chemin courant
```

**Exemple VSCode/Conda (déjà appliqué) :**
```
**Point de validation** : Vous voyez `(ndvi-project)` au début de votre invite.
```

---

### **Pattern 7 : Points clés à retenir (conclusion)**

TOUS les ateliers terminent par une section "Points clés" ou "À retenir" :

**Git (Jessica) :**
```markdown
## Points à retenir:

1. Git n'est pas un logiciel à partir duquel travailler...
2. Une fois que votre dossier est pris en charge par Git...
3. Continuer de travailler comme vous le faisiez avant...
```

**Python (Charles) :**
```markdown
## Ressources
- **Python Crash Course, 2nd edition** - Eric Matthes
- **Practical Statistics for Data Scientists** - Bruce, Bruce, Gedeck
```

---

### **Pattern 8 : Références externes minimales**

Numérilab ateliers **NE SONT PAS** des copies-colles de docs officielles. Ils :
- Réexpliquent les concepts avec ton propre langage
- Renvoient à docs officielles seulement pour cas avancés
- Incluent exemples domaine-spécifiques (iris dataset, specs, spectro, etc.)

---

## 📐 Templates proposés pour futures formations

### **Template A : Formation technologie (Conda, VSCode, Git)**
```
1. Introduction
   - Contexte géomatique
   - Pourquoi cet outil pour la géomatique

2. Théorie & Comparaisons
   - Concept fondamental
   - Tableau comparatif (4-6 cols)
   - Alternative tools

3. Installation/Mise en place (5-10 min)
   - Prérequis
   - Étapes avec points de validation

4. Atelier pratique
   - Approche A (avancée/CLI)
   - Approche B (accessible/GUI)
   - Etapes 1-N avec points de validation

5. Workflow intégré
   - Comment ça marche avec autres outils
   - Exemple réaliste (NDVI, spectro, etc.)

6. Points clés + ressources
```

### **Template B : Formation stats/analyses (modèles, ML, etc.)**
```
1. Introduction
   - Contexte scientifique
   - Quand utiliser cette technique

2. Théorie & Méthodologies
   - Concepts fondamentaux
   - Comparaison avec techniques existantes
   - Avantages/inconvénients

3. Données d'exemple
   - Dataset présenté
   - Caractéristiques

4. Atelier pratique
   - R ET Python (si applicable)
   - Étapes détaillées
   - Interprétation résultats

5. Points clés
```

### **Template C : Formation documentation (Quarto, etc.)**
```
1. Introduction
   - Contexte : comment documenter analyses
   - Pourquoi cet outil

2. Concepts fondamentaux
   - Syntaxe de base
   - Tableaux de fonctionnalités

3. Mise en place
   - Créer document
   - Configuration

4. Atelier pratique
   - Formatage texte
   - Code intégré (R/Python)
   - Figures et équations
   - Publication

5. Prochaines étapes (livres, blogs)
```

---

## 🎓 Éléments à incorporer dans TOUS les ateliers Numérilab

### **Obligatoire**

1. ✅ **Contexte problème** (avant solution)
2. ✅ **Tableau comparatif** 4-6 colonnes au moins une fois
3. ✅ **Tone académique conversationnel** (pas vulgarisé, pas jargonné)
4. ✅ **2+ approches** (CLI + GUI, R + Python, etc.)
5. ✅ **Points de validation** à chaque étape ("vous devriez voir...")
6. ✅ **Étapes numérotées et claires**
7. ✅ **Points clés à retenir** (récap finale)
8. ✅ **Ressources** (docs officielles, lectures)
9. ✅ **Exemples domaine-spécifique** (pas données génériques iris)

### **Recommandé**

- Captures d'écran annotées (8-12 per atelier)
- Narratif "vous avez probablement rencontré..."
- Exemple réaliste étape-par-étape (workflow)
- Github repo public avec code exemple
- environment.yml ou équivalent
- .gitignore template

---

## 📁 Structure proposée pour nouveaux ateliers

```
numerilab-ATELIER_NAME/
├── README.md                    # Présentation + liens
├── .gitignore                   # Standard Numérilab
├── docs/
│   └── formation-ATELIER.md     # Document 60-90 min
├── resources/
│   ├── environment.yml          # Stack Python/R
│   ├── settings.json            # VSCode config (si applicable)
│   └── extensions-recommended.md # Extensions
├── examples/
│   ├── demo-workflow.md         # Exercice étape par étape
│   └── dataset_example.csv      # Données exemple
└── assets/
    ├── screenshots/             # 8-12 captures annotées
    └── GUIDE_SCREENSHOTS.md     # Instructions captures
```

---

## 🔗 Intégration avec site Numérilab

### **Frontmatter YAML pour page web**

```yaml
---
title: "Introduction à Conda et VSCode pour la géomatique"
author: "Numérilab UQTR"
date: "2025-10-29"
duration: "90 minutes"
level: "Intermédiaire"
category: "Programmation"
tags:
  - Python
  - Conda
  - VSCode
  - Géomatique
thumbnail: "assets/vscode-icon.png"
github_repo: "https://github.com/numerilab/formation-vscode-conda"
---
```

---

## 📈 Exemples de réussite (sites existants)

**Numérilab patterns appliqués dans VSCode/Conda :**
- ✅ Sections 2.1, 2.4, 3.4, 3.5 réécrites avec tone Numérilab
- ✅ Tableaux comparatifs (Anaconda vs Miniforge, Conda vs Pip, etc.)
- ✅ Points de validation ("vous devriez voir...")
- ✅ Workflow réaliste (NDVI analysis)
- ✅ Structure claire (Intro → Théorie → Pratique → Points clés)

---

## 💡 Recommandation pour skill/agent Numérilab

**Arguments POUR créer un agent :**
- ✅ 4-6+ futures formations prévues → automatisation utile
- ✅ Patterns clairs et reproductibles identifiés
- ✅ Template réutilisables possibles
- ✅ Validation de tone/structure (checker pédagogique)
- ✅ Génération de structure (arborescence, README, etc.)

**Cas d'usage agent Numérilab :**
1. Créer structure projet automatiquement
2. Valider tone = académique québécois (pas vulgarisé)
3. Vérifier que chaque section suit pattern Numérilab
4. Générer environment.yml basé sur domaine
5. Créer guide captures d'écran
6. Générer README avec template Numérilab

---

**Document créé pour** : Planification futures formations Numérilab
**À utiliser pour** : Créer skill ou agir comme checklist manuelle
