from pathlib import Path
from collections import defaultdict
import hashlib
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm

console = Console()

def get_file_hash(file_path: Path, chunk_size=8192):
    """Generate hash for file (fast method)"""
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

    console.print(f"[cyan]Scanning for duplicate files in:[/cyan] {target}")
    
    hash_dict = defaultdict(list)
    total_files = 0

    for file in target.rglob("*"):
        if file.is_file():
            total_files += 1
            file_hash = get_file_hash(file)
            if file_hash:
                hash_dict[file_hash].append(file)

    # Find duplicates
    duplicates = {h: files for h, files in hash_dict.items() if len(files) > 1}

    if not duplicates:
        console.print("[bold green]🎉 No duplicate files found![/bold green]")
        return

    console.print(f"\n[bold red]Found {len(duplicates)} group(s) of duplicate files:[/bold red]\n")

    table = Table(title="Duplicate Files")
    table.add_column("Size", style="cyan")
    table.add_column("Files", style="yellow")

    delete_list = []

    for files in duplicates.values():
        size = files[0].stat().st_size / (1024*1024)  # in MB
        table.add_row(f"{size:.2f} MB", "\n".join([f.name for f in files]))
        
        # Keep the first file, suggest deleting others
        for f in files[1:]:
            delete_list.append(f)

    console.print(table)

    if delete_list and Confirm.ask(f"\nDelete {len(delete_list)} duplicate file(s)?", default=False):
        deleted = 0
        for file in delete_list:
            try:
                file.unlink()
                console.print(f"[red]Deleted:[/red] {file.name}")
                deleted += 1
            except Exception as e:
                console.print(f"[red]Failed to delete {file.name}: {e}[/red]")
        
        console.print(f"\n[bold green]✅ Deleted {deleted} duplicate files.[/bold green]")
