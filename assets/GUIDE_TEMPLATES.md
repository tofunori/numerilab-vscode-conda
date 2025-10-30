# Guide d'utilisation des templates Numérilab
## Pour créer rapidement des formations alignées avec le style Numérilab

---

## 📚 Documents templates disponibles

### 1. **NUMERILAB_PATTERNS_ANALYSIS.md**
- **Qu'est-ce que c'est** : Analyse détaillée de 20+ ateliers existants
- **Quand le lire** : Avant de créer une nouvelle formation
- **Contient** :
  - Patterns observés dans tous les ateliers
  - Tone pédagogique recommandé
  - Exemples directs du site Numérilab
  - Points clés à reproduire

### 2. **TEMPLATE_NOUVELLE_FORMATION.md**
- **Qu'est-ce que c'est** : Skeleton HTML/Markdown à copier-coller
- **Quand l'utiliser** : Pour créer la structure de base d'une nouvelle formation
- **Contient** :
  - Sections pré-formatées
  - Placeholders [à remplir]
  - Checklist finale

---

## 🚀 Workflow pour créer une nouvelle formation

### **Phase 1 : Planification (30 minutes)**

1. Lire **NUMERILAB_PATTERNS_ANALYSIS.md** sections pertinentes
2. Identifier catégorie de votre atelier :
   - [ ] Technologie (Conda, VSCode, Git) → **Template A**
   - [ ] Stats/Analyses (ML, modèles) → **Template B**
   - [ ] Documentation (Quarto, RMarkdown) → **Template C**
3. Rassembler :
   - Contexte du problème
   - 3-4 exemples concrets du domaine
   - Alternative tools à comparer
   - Ressources officielles

### **Phase 2 : Création structure (20 minutes)**

1. Copier **TEMPLATE_NOUVELLE_FORMATION.md**
2. Adapter les sections :
   - Remplacer `[XXX]` par vos contenus
   - Ajouter/retirer sections si nécessaire
3. Créer arborescence projet :
   ```
   numerilab-ATELIER_NAME/
   ├── README.md
   ├── docs/formation-ATELIER.md  # Votre fichier
   ├── resources/
   ├── examples/
   └── assets/
   ```

### **Phase 3 : Rédaction contenu (4-6 heures)**

1. **Section Introduction** (30 min)
   - Écrire contexte problème
   - Expliquer motivation
   - Énumérer avantages

2. **Section Concepts** (1-1.5 heures)
   - Créer tableau comparatif
   - Expliquer concepts (mode conversationnel)
   - Ajouter définitions

3. **Section Mise en place** (45 min)
   - Lister prérequis
   - Détailler étapes avec points de validation

4. **Section Atelier pratique** (2-3 heures)
   - Écrire 2+ approches
   - Ajouter code/screenshots
   - Vérifier points de validation

5. **Section Workflow intégré** (1 heure)
   - Créer scénario réaliste
   - Lier étapes ensemble

6. **Section Ressources** (30 min)
   - Points clés
   - Links documentations
   - Troubleshooting

### **Phase 4 : Captures d'écran (1-2 heures)**

Voir **assets/GUIDE_SCREENSHOTS.md** pour détails.

Minimum : 8 captures annotées
- Installation/Setup (2)
- Interface principale (2)
- Résultats/Validation (2)
- Workflow complet (2)

### **Phase 5 : Fichiers ressources (30 min)**

Créer dans `resources/` :
- `environment.yml` (si Python/R)
- `settings.json` (si VSCode)
- `extensions-recommandees.md` (si applicable)
- `.gitignore` template

### **Phase 6 : Test & validation (45 min)**

- [ ] Lire document complet (erreurs typo, ton)
- [ ] Vérifier tous les liens internes
- [ ] Tester étapes pratiques si possible
- [ ] Appliquer **checklist finale** du template
- [ ] Peer review (demander feedback quelqu'un autre)

### **Phase 7 : Publication (20 min)**

1. Créer repo GitHub public
2. Ajouter frontmatter YAML dans README.md
3. Pousser sur GitHub
4. Tester liens et accès
5. Ajouter lien sur main README.md du projet

---

## ✅ Checklist : 8 éléments NON-NÉGOCIABLES

Tous les ateliers Numérilab doivent avoir :

### 1. ✅ **Contexte problème AVANT solution**
❌ **Mauvais** : "Conda est un gestionnaire de packages..."
✅ **Bon** : "Vous avez probablement rencontré cette erreur : 'pip install gdal' échoue. Pourquoi ? Parce que GDAL..."

**Où vérifier** : Section 1 & 2.1

### 2. ✅ **Tone académique conversationnel**
❌ **Mauvais** : "Conda est comme une pizzeria qui livre des packages" (vulgarisation)
✅ **Bon** : "Conda est un gestionnaire de paquets qui... Contrairement à pip, Conda peut gérer les dépendances C."

**Où vérifier** : Lire à voix haute, tone naturel

### 3. ✅ **Tableau comparatif 4-6 colonnes**
Au minimum une fois dans le document.

**Exemples** :
- Conda vs Pip vs Mamba vs VENV
- Anaconda vs Miniforge
- Centralisé vs Distribué

**Où vérifier** : Section 2 (Concepts)

### 4. ✅ **2+ approches différentes**
Terminal + GUI, R + Python, CLI + Interface, etc.

❌ **Mauvais** : "Voici comment faire avec la commande X"
✅ **Bon** :
- Approche A : Terminal (avancé)
- Approche B : GitHub Desktop (accessible)

**Où vérifier** : Section 4 (Atelier pratique)

### 5. ✅ **Points de validation à chaque étape**
"Vous devriez voir..." ou "L'output attendu est..."

**Exemple** :
```
### Étape 2 : Activer environnement
conda activate mon-env

**Point de validation** : Vous voyez `(mon-env)` au début de votre invite.
```

**Où vérifier** : Chaque "#### Étape X" doit avoir un point de validation

### 6. ✅ **Points clés à retenir (récap)**
Liste à puces à la fin.

```markdown
✅ **Concept 1** - Explication courte
✅ **Concept 2** - Explication courte
```

**Où vérifier** : Section 6 (Points clés)

### 7. ✅ **Exemples domaine-spécifique**
Pas iris dataset ou données génériques.

✅ **Bons exemples** :
- NDVI (géomatique)
- Spectroscopie (chimie)
- Microbiome (bio)

**Où vérifier** : Sections Atelier & Workflow

### 8. ✅ **Structure complète du projet**
```
numerilab-ATELIER/
├── README.md ✅
├── .gitignore ✅
├── docs/formation-ATELIER.md ✅
├── resources/
│   ├── environment.yml ✅
│   ├── settings.json (si applicable)
│   └── extensions-recommandees.md
├── examples/
│   └── demo-workflow.md
└── assets/
    ├── screenshots/
    └── GUIDE_SCREENSHOTS.md
```

---

## 🎯 Pour chaque section : Conseils spécifiques

### **Section 1 : Introduction**

```markdown
## 1. Introduction

### Contexte
**Situation réelle :** Vous travaillez en [domaine]...
- Besoin 1
- Besoin 2

### Pourquoi [outil] ?
✅ Avantage 1 (spécifique à votre domaine)
✅ Avantage 2
```

**Conseil** : Commencer par le problème, pas l'outil.

---

### **Section 2 : Concepts**

**Structure requise** :
1. Le problème que X résout
2. Qu'est-ce que X ?
3. Tableau comparatif
4. Méthodologies (si applicable)

**Conseil** : Pas de jargon. Si vous écrivez un terme technique, l'expliquer.

---

### **Section 4 : Atelier pratique**

**Approche A : Avancée** (Terminal, code, CLI)
- Pour utilisateurs confortables avec ligne de commande
- Montrer la façon "pure" de faire

**Approche B : Accessible** (GUI, interface, point-and-click)
- Pour débutants ou qui préfèrent interface visuelle
- Montrer même résultats mais via interface

**Conseil** : Les deux approches doivent mener aux MÊMES résultats.

---

### **Section 5 : Workflow intégré**

Ce qui différencie Numérilab : montrer comment les concepts **s'assemblent**.

**Pattern** :
- "Pourquoi cette séquence ?"
- Scénario réaliste complet
- Tableau montrant rôle de chaque tool
- "Impossible d'atteindre ça avec juste A, juste B..."

**Conseil** : C'est LA section qui montre pourquoi on a appris tout ça.

---

### **Section 6 : Ressources**

```markdown
### Points clés à retenir
✅ **[Concept]** - Une phrase
✅ **[Concept]** - Une phrase

### Documentation officielle
- [Nom docs](lien)

### Troubleshooting
| Problème | Cause | Solution |
```

**Conseil** : Pas de ressources > 3-4. Garder essentiels seulement.

---

## 🔍 Checklist auto-validation AVANT push

**Lisibilité & Tone (10 min)**
- [ ] Document se lit naturellement (pas robotique)
- [ ] Pas de "vous devez" (plutôt "vous pouvez", "vous avez besoin de")
- [ ] Pas d'anglicismes évidentes (API → interface, bug → erreur, etc.)
- [ ] Pas d'emojis excessifs (max 5-10 total)

**Structure (10 min)**
- [ ] Table des matières correcte
- [ ] Tous les [XXX] remplacés
- [ ] Titres hiérarchie logique (#, ##, ###)
- [ ] Sections dans ordre correct

**Contenu (20 min)**
- [ ] Intro contextualise le problème
- [ ] Tableau comparatif présent
- [ ] 2+ approches différentes
- [ ] Points de validation à chaque étape
- [ ] Points clés à la fin
- [ ] Ressources listées
- [ ] Exemples domaine-spécifique (pas iris)

**Technique (10 min)**
- [ ] Code blocks formatés correctement
- [ ] Liens internes fonctionnels
- [ ] Images/screenshots en bons chemins
- [ ] Pas d'erreurs typo

**Projet (10 min)**
- [ ] README.md complet
- [ ] resources/ remplie
- [ ] examples/ présent
- [ ] assets/screenshots/ avec 8-12 images
- [ ] .gitignore configuré
- [ ] Prêt pour GitHub

---

## 🚨 Erreurs courantes à ÉVITER

### ❌ Erreur 1 : "Explication d'abord, problème jamais"
```
❌ MAUVAIS :
Conda est un gestionnaire de packages et d'environnements qui...

✅ BON :
Vous avez probablement rencontré cette erreur : "pip install gdal" échoue...
C'est ici que Conda intervient.
```

### ❌ Erreur 2 : Ton enfantin/vulgarisé
```
❌ MAUVAIS :
Conda c'est comme une boîte magique qui donne les packages 😄🎁

✅ BON :
Conda gère les dépendances C (GDAL, PROJ) en téléchargeant des versions
pré-compilées au lieu de tenter une compilation locale.
```

### ❌ Erreur 3 : "Je mets un approche seule"
```
❌ MAUVAIS :
### Atelier
git init
git add .

✅ BON :
### Approche A : Terminal (avancé)
git init
git add .

### Approche B : GitHub Desktop (accessible)
1. Ouvrir GitHub Desktop
2. New Repository
```

### ❌ Erreur 4 : Points de validation inexistants
```
❌ MAUVAIS :
### Étape 1 : Installer
conda install package

### Étape 2 : Vérifier
python -c "import package"

✅ BON :
### Étape 1 : Installer
conda install package
**Point de validation** : Vous voyez "Solving environment" puis succès.

### Étape 2 : Vérifier
python -c "import package"
**Point de validation** : Aucune erreur. Le module s'importe correctement.
```

### ❌ Erreur 5 : Données iris ou génériques
```
❌ MAUVAIS :
Charger le dataset iris...

✅ BON :
Vous téléchargez une image NDVI Sentinel-2 d'une zone protégée...
```

---

## 📞 Questions fréquentes

### Q: Combien de temps ça prend créer une formation ?
**R:** 6-8 heures pour une formation 60-90 min
- Planification : 0.5h
- Structure : 0.5h
- Rédaction : 4-5h
- Captures : 1-2h

### Q: Faut-il absolument 8+ captures ?
**R:** Oui, c'est le standard Numérilab. Mais elles peuvent être simple (screenshots + boîtes texte).

### Q: Je dois créer 2+ approches pour TOUS les ateliers ?
**R:** Oui, tous les ateliers Numérilab le font. C'est une signature.

### Q: Mon tableau comparatif doit faire combien de colonnes ?
**R:** Minimum 4 colonnes, idéalement 4-6. Plus clair que 3.

### Q: Peux-je réutiliser contenu d'autres sites ?
**R:** Oui, mais réécris avec ton propre langage. Numérilab ateliers ne sont pas copies-colles.

### Q: Les ressources peuvent être en anglais ?
**R:** Oui, documentation officielle est souvent anglaise. Mais présentation Numérilab = français québécois.

---

## 🎓 Exemples de formations bien exécutées

**Dans ce projet (Numérilab VSCode/Conda)** :
- ✅ Section 2.1 : Théorie contextualisée
- ✅ Section 2.4 : Table comparatif + exemples domaine
- ✅ Section 3.4 : Importance science + collaboration
- ✅ Section 3.5 : Workflow intégré avec 6 étapes
- ✅ Points de validation à chaque étape
- ✅ Structure README + resources + examples

**Sur site Numérilab** :
- Git (Jessica Malko) : 2 approches (Terminal + GitHub Desktop)
- Python (Charles Martin) : Colab + local, tons d'exemples concrets
- Quarto (Charles Martin) : Syntaxe → Mise en place → Atelier détaillé

---

**Bon travail ! Vous êtes prêt(e) à créer votre prochaine formation Numérilab.** 🚀

Pour questions : Vérifier **NUMERILAB_PATTERNS_ANALYSIS.md** section pertinente.
