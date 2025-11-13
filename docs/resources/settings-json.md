# Configuration VSCode (settings.json)

Fichier de configuration VSCode optimisé pour la géomatique et la science des données.

## Installation

1. Dans votre projet, créer le dossier `.vscode/` à la racine
2. Copier le contenu ci-dessous dans `.vscode/settings.json`
3. Relancer VSCode

## Contenu du fichier

```json
{
  // === PYTHON ===
  "python.defaultInterpreterPath": "${workspaceFolder}/env/Scripts/python.exe",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": ["--max-line-length=120"],
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length=120"],
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    },
    "editor.defaultFormatter": "ms-python.python"
  },

  // === JUPYTER NOTEBOOKS ===
  "jupyter.notebookFileRoot": "${workspaceFolder}",
  "notebook.cellToolbarLocation": "right",
  "[jupyter]": {
    "editor.defaultFormatter": "ms-python.python"
  },

  // === EDITOR ===
  "editor.fontSize": 12,
  "editor.fontFamily": "'IBM Plex Mono', 'Courier New', monospace",
  "editor.lineHeight": 1.6,
  "editor.rulers": [80, 120],
  "editor.wordWrap": "on",
  "editor.formatOnSave": true,
  "editor.insertSpaces": true,
  "editor.tabSize": 4,
  "editor.trimAutoWhitespace": true,

  // === APPEARANCE ===
  "workbench.colorTheme": "One Dark Pro",
  "workbench.iconTheme": "vs-nomo-dark",
  "editor.minimap.enabled": true,
  "editor.renderWhitespace": "selection",

  // === FILE EXPLORER ===
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/.ipynb_checkpoints": true,
    "**/.env": true
  },
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/*/**": true,
    "**/.pytest_cache/**": true
  },

  // === GIT ===
  "git.enabled": true,
  "git.ignoreLimitWarning": true,
  "github.copilot.enable": {
    "*": true,
    "markdown": true,
    "plaintext": false
  },

  // === TERMINAL ===
  "terminal.integrated.defaultProfile.windows": "Command Prompt",
  "terminal.integrated.profiles.windows": {
    "PowerShell": {
      "source": "PowerShell",
      "icon": "terminal-powershell"
    },
    "Command Prompt": {
      "path": ["${env:windir}\\Sysnative\\cmd.exe", "${env:windir}\\System32\\cmd.exe"],
      "args": [],
      "icon": "terminal-cmd"
    }
  },
  "terminal.integrated.fontSize": 12,
  "terminal.integrated.lineHeight": 1.4,

  // === EXTENSIONS ===
  "extensions.ignoreRecommendations": false,

  // === SEARCH ===
  "search.exclude": {
    "**/.git": true,
    "**/node_modules": true,
    "**/__pycache__": true,
    "**/*.egg-info": true
  },

  // === TELEMETRY (optionnel) ===
  "telemetry.telemetryLevel": "off"
}
```

## Téléchargement direct

<a href="https://raw.githubusercontent.com/tofunori/numerilab-vscode-conda/master/docs/resources/settings.json"
   download="settings.json"
   style="display: inline-block; padding: 10px 20px; background-color: #2196F3; color: white; text-decoration: none; border-radius: 4px; margin: 10px 0;">
  ⬇ Télécharger settings.json
</a>

## Sections principales

### Python
- Configuration de l'interpréteur par défaut
- Activation du linting avec flake8
- Formatage automatique avec Black (120 caractères)
- Organisation automatique des imports

### Jupyter Notebooks
- Racine des notebooks au niveau du projet
- Barre d'outils des cellules à droite

### Éditeur
- Police IBM Plex Mono
- Règles visuelles à 80 et 120 caractères
- Retour à la ligne automatique
- Formatage à la sauvegarde

### Terminal
- Terminal par défaut : Command Prompt (compatible Conda)
- Configuration PowerShell disponible

### Fichiers exclus
- Cache Python (`__pycache__`, `.pyc`)
- Checkpoints Jupyter
- Fichiers Git volumineux
