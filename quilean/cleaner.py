from pathlib import Path
from rich.console import Console
from rich.prompt import Confirm
from .config import load_config

console = Console()
config = load_config()

JUNK_EXTENSIONS = {'.tmp', '.temp', '.log', '.cache', '.pyc', '.pyo', '.DS_Store'}
JUNK_FOLDERS = {'__pycache__', '.cache', 'temp', 'logs'}


def clean_junk(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    deleted_count = 0

    console.print(f"[cyan]Scanning for junk files in:[/cyan] {target}")

    # Delete junk files
    for item in target.rglob("*"):
        if item.is_file() and item.suffix.lower() in JUNK_EXTENSIONS:
            try:
                item.unlink()
                console.print(f"[red]Deleted:[/red] {item.name}")
                deleted_count += 1
            except Exception:
                pass

        elif item.is_dir() and item.name in JUNK_FOLDERS:
            try:
                import shutil
                shutil.rmtree(item, ignore_errors=True)
                console.print(f"[red]Deleted folder:[/red] {item.name}/")
                deleted_count += 1
            except Exception:
                pass

    console.print(f"\n[bold green]✅ Cleaned {deleted_count} junk items.[/bold green]")
