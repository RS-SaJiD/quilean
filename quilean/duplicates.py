from pathlib import Path
from collections import defaultdict
import hashlib
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm
from .config import load_config

console = Console()
config = load_config()


def get_file_hash(file_path: Path, chunk_size=8192):
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None


def find_duplicates(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    console.print(f"[cyan]Scanning for duplicates in:[/cyan] {target}")
    
    hash_dict = defaultdict(list)

    for file in target.rglob("*"):
        if file.is_file():
            file_hash = get_file_hash(file)
            if file_hash:
                hash_dict[file_hash].append(file)

    duplicates = {h: files for h, files in hash_dict.items() if len(files) > 1}

    if not duplicates:
        console.print("[bold green]🎉 No duplicate files found![/bold green]")
        return

    console.print(f"\n[bold red]Found {len(duplicates)} group(s) of duplicate files[/bold red]\n")

    table = Table(title="Duplicate Files")
    table.add_column("Size (MB)", style="cyan")
    table.add_column("Count", style="magenta")
    table.add_column("Files", style="yellow")

    delete_list = []

    for files in duplicates.values():
        size_mb = files[0].stat().st_size / (1024 * 1024)
        table.add_row(f"{size_mb:.2f}", str(len(files)), "\n".join([f.name for f in files]))
        
        # Keep first file, mark others for deletion
        delete_list.extend(files[1:])

    console.print(table)

    if delete_list and config["general"].get("confirm_before_delete", True):
        if Confirm.ask(f"Delete {len(delete_list)} duplicate file(s)?", default=False):
            deleted = 0
            for file in delete_list:
                try:
                    file.unlink()
                    console.print(f"[red]Deleted:[/red] {file.name}")
                    deleted += 1
                except Exception as e:
                    console.print(f"[red]Failed to delete {file.name}[/red]")
            console.print(f"\n[bold green]✅ Deleted {deleted} duplicate files.[/bold green]")
