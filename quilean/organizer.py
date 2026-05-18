import os
from pathlib import Path
from rich.console import Console
from .config import DEFAULT_FOLDERS

console = Console()

def organize_files(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    for item in target.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            moved = False
            
            for folder_name, extensions in DEFAULT_FOLDERS.items():
                if ext in extensions:
                    folder_path = target / folder_name
                    folder_path.mkdir(exist_ok=True)
                    item.rename(folder_path / item.name)
                    console.print(f"[green]Moved:[/green] {item.name} → {folder_name}/")
                    moved = True
                    break
            
            if not moved:
                folder_path = target / "Others"
                folder_path.mkdir(exist_ok=True)
                item.rename(folder_path / item.name)
                console.print(f"[yellow]Moved:[/yellow] {item.name} → Others/")
