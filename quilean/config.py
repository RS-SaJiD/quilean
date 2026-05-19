from pathlib import Path
import tomllib
import os
from rich.console import Console

console = Console()

CONFIG_DIR = Path.home() / ".quilean"
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG = {
    "general": {
        "default_folder": ".",
        "show_progress": True,
        "confirm_before_delete": True
    },
    "folders": {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".md", ".csv"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
        "Audio": [".mp3", ".wav", ".flac", ".m4a", ".ogg"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".go", ".rs", ".ts"],
        "Others": []
    }
}

def load_config():
    CONFIG_DIR.mkdir(exist_ok=True)
    
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        console.print("[green]✅ Default config created at \~/.quilean/config.toml[/green]")
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        console.print(f"[yellow]Warning: Could not load config, using default. {e}[/yellow]")
        return DEFAULT_CONFIG

def save_config(config):
    import toml
    with open(CONFIG_FILE, "w") as f:
        toml.dump(config, f)
