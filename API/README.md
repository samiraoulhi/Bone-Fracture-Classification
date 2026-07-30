## Installation et lancement

### 1. Cloner le projet
```bash
git clone https://github.com/<ton-username>/Bone-Fracture-Classification.git
cd Bone-Fracture-Classification
```

### 2. Créer l'environnement virtuel
```bash
python -m venv .venv
```

### 3. Autoriser l'exécution des scripts (PowerShell, une seule fois)

Par défaut, Windows bloque l'exécution des scripts PowerShell. Cette commande autorise les scripts locaux signés, pour l'utilisateur courant uniquement :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. Activer l'environnement virtuel
```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 6. Lancer l'application
```bash
python -m streamlit run streamlit_class.py
```
