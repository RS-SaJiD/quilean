# Quilean 🧹

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**A fast, smart & beautiful Python CLI tool** to organize, rename, clean and manage your messy files efficiently.

### ✨ Features

- Smart file organization by type (extension)
- Bulk Rename with custom pattern
- Junk & Temporary files cleaner
- Folder Statistics
- Colorful CLI interface
- Easy to install & use

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
