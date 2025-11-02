# Guide de contribution

Merci d'intéresser à la contribution! Ce document explique comment participer à l'amélioration du projet Numérilab.

---

## Types de contributions

### 1. Signaler un bug

Vous avez trouvé une erreur ou une inconsistance ?

1. Visiter [GitHub Issues](https://github.com/tofunori/numerilab-vscode-conda/issues)
2. Cliquer **New Issue**
3. Décrire le problème :
   - Quelle erreur avez-vous rencontrée ?
   - Quels étaient les étapes pour reproduire ?
   - Quel était le comportement attendu ?
   - Quel est votre environnement (OS, Python, Conda) ?

### 2. Proposer une amélioration

Vous avez une idée pour améliorer la documentation ou le code ?

1. Ouvrir une [Discussion](https://github.com/tofunori/numerilab-vscode-conda/discussions)
2. Décrivez votre idée
3. Attendez les commentaires de la communauté

### 3. Soumettre du code ou de la documentation

Pour contribuer du code ou corriger de la documentation :

1. **Fork** le repo (cliquer "Fork" sur GitHub)
2. Cloner votre fork localement :
   ```bash
   git clone https://github.com/VOTRE_COMPTE/numerilab-vscode-conda.git
   cd numerilab-vscode-conda
   ```
3. Créer une branche pour votre changement :
   ```bash
   git checkout -b fix/mon-correction
   # ou
   git checkout -b feature/ma-nouvelle-fonctionnalite
   ```
4. Faire vos changements
5. Committer avec message explicite :
   ```bash
   git commit -m "Corriger X en changeant Y (fix #123)"
   ```
6. Pousser vers votre fork :
   ```bash
   git push origin fix/mon-correction
   ```
7. Ouvrir une **Pull Request** (bouton "New Pull Request" sur GitHub)

---

## Standards de qualité

Pour que votre contribution soit acceptée, veuillez respecter :

### Documentation

- Français québécois académique
- Explications claires avant code
- Exemples pratiques concrets
- Tableaux de comparaison quand approprié
- Liens vers ressources officielles

### Code

- Commentaires clairs en français
- Docstrings pour fonctions
- Tests pour nouvelles fonctionnalités
- Respect des conventions du projet

### Commits

- Messages explicites en français
- Une feature/fix par commit
- Lier à un issue (ex: "fix #42")

---

## Process de révision

1. Vous soumettez une PR
2. Nous examinons votre code
3. Nous demandons des changements si nécessaire
4. Une fois approuvé, votre contribution est fusionnée
5. Vous êtes crédité comme contributeur !

---

## Questions ?

- **Problèmes avec Git** : Voir la section [3.4 Git et GitHub](../formation/3.4-git-github.md)
- **Structure du projet** : Voir la [page d'accueil](../index.md)
- **Discussion** : Ouvrir une [Discussion](https://github.com/tofunori/numerilab-vscode-conda/discussions)

---

Merci de contribuer au projet !
