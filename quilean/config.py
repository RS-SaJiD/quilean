from pathlib import Path
import sys
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
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        console.print("[green]✅ Default config created[/green]")
        return DEFAULT_CONFIG

    try:
        if sys.version_info >= (3, 11):
            import tomllib
            with open(CONFIG_FILE, "rb") as f:
                return tomllib.load(f)
        else:
            import toml
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return toml.load(f)
    except Exception as e:
        console.print(f"[yellow]Warning: Could not load config: {e}. Using default.[/yellow]")
        return DEFAULT_CONFIG


def save_config(config):
    try:
        import toml
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            toml.dump(config, f)
    except ImportError:
        console.print("[red]Error: 'toml' package is not installed.[/red]")
        console.print("Run: pip install toml")


# Load config once
config = load_config()
