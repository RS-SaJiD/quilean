from pathlib import Path
import tomllib
import toml
from rich.console import Console

console = Console()

CONFIG_DIR = Path.home() / ".quilean"
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG = {
    "general": {
        "default_folder": ".",
        "show_progress": True,
        "confirm_before_delete": True,
        "max_history": 10
    },
    "folders": {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".md", ".csv", ".json"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
        "Audio": [".mp3", ".wav", ".flac", ".m4a", ".ogg", ".aac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".go", ".rs", ".ts", ".jsx"],
        "Others": []
    }
}


def load_config():
    CONFIG_DIR.mkdir(exist_ok=True)
    
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        console.print("[green]Default configuration created at \~/.quilean/config.toml[/green]")
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, "rb") as f:
            return tomllib.load(f)
    except Exception:
        console.print("[yellow]Warning: Failed to load config. Using default.[/yellow]")
        return DEFAULT_CONFIG


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        toml.dump(config, f)
