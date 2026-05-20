# Quilean 🧹

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-yellow)

**A fast, smart and modern Python CLI tool** to organize, clean, rename and manage your files efficiently.


### ✨ Features

- 📁 Smart File Organizer (by file type)
- 🔍 Duplicate File Finder & Remover
- ✍️ Bulk Rename with custom pattern
- 🗑️ Junk & Temporary File Cleaner
- 🏷️ Smart Tagging (keyword based)
- ↩️ Undo Last Operation
- 📊 Folder Statistics
- ⚙️ Config File Support (`\~/.quilean/config.toml`)
- 🎨 Beautiful Rich CLI with colors

### 🚀 Installation

```bash
# From GitHub
pip install git+https://github.com/RS-SaJiD/quilean.git

# After install
quilean --help
```

### 📋 Basic Usage 
```bash
quilean --help                    # See all commands
quilean organize                  # Organize current folder
quilean organize \~/Downloads      # Specific folder
quilean duplicates                # Find duplicate files
quilean clean                     # Delete junk files
quilean rename                    # Bulk rename
quilean tag                       # Smart tagging
quilean stats                     # Folder statistics
quilean undo                      # Undo last action
```

### 📌 Commands 
| Command          | Description                          |
|------------------|--------------------------------------|
| `organize`       | 📁 Files organize by type            |
| `duplicates`     | 🔍 Find and delete duplicate files   |
| `clean`          | 🗑️ Clean junk/temp files            |
| `rename`         | ✍️ Bulk rename files                 |
| `tag`            | 🏷️ Apply smart tags                  |
| `stats`          | 📊 Show folder statistics            |
| `undo`           | ↩️ Undo last operation               |

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
├── quilean/                      # Main Package
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── organizer.py
│   ├── renamer.py
│   ├── cleaner.py
│   ├── utils.py
│   ├── duplicates.py
│   ├── history.py
│   └── tagger.py
├── tests/                        # Unit Tests
│   ├── __init__.py
│   ├── test_organizer.py
│   └── test_cli.py
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
└── setup.py
```
