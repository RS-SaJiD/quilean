# Quilean 🧹

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-yellow)

**A fast, smart and modern Python CLI tool** to organize, clean, rename and manage your files efficiently.


### ✨ Features

- Smart File Organizer (by file type)
- Duplicate File Finder & Remover
- Bulk Rename with pattern
- Junk/Temp File Cleaner
- Smart Tagging (keyword based)
- Undo Last Operation
- Folder Statistics
- Config File Support (`\~/.quilean/config.toml`)
- Beautiful Rich CLI Interface


### Installation

```bash
# From GitHub
pip install git+https://github.com/RS-SaJiD/quilean.git

# After install
quilean --help
```

### Commands 
- quilean organize [path] → Organizes files
- quilean rename [path] → Bulk rename
- quilean clean [path] → Deletes junk files
- quilean stats [path] → Shows folder information.

### Test 
```bash
# To run a test
python -m pytest tests/ -v
# Or
python -m unittest discover -s tests
```


### 📁 Project Structure

```bash
quilean/
├── quilean/                  # Main Python Package
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── organizer.py
│   ├── renamer.py
│   ├── cleaner.py
│   └── utils.py
├── tests/                    # Unit tests
│   ├── __init__.py
│   ├── test_organizer.py
│   └── test_cli.py
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
└── setup.py
