from pathlib import Path
from collections import defaultdict
import hashlib
from rich.console import Console
from rich.progress import Progress
from rich.table import Table
from rich.prompt import Confirm
from .config import load_config
from .logger import logger

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

    files = [f for f in target.rglob("*") if f.is_file()]
    console.print(f"[cyan]Scanning {len(files)} files for duplicates...[/cyan]")

    hash_dict = defaultdict(list)

    with Progress() as progress:
        task = progress.add_task("[yellow]Calculating hashes...", total=len(files))

        for file in files:
            file_hash = get_file_hash(file)
            if file_hash:
                hash_dict[file_hash].append(file)
            progress.update(task, advance=1)

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
        delete_list.extend(files[1:])

    console.print(table)

    if delete_list and config["general"].get("confirm_before_delete", True):
        if Confirm.ask(f"Delete {len(delete_list)} duplicate file(s)?", default=False):
            deleted = 0
            with Progress() as progress:
                task = progress.add_task("[red]Deleting duplicates...", total=len(delete_list))
                for file in delete_list:
                    try:
                        file.unlink()
                        logger.info(f"Deleted duplicate: {file.name}")
                        deleted += 1
                    except Exception as e:
                        logger.error(f"Failed to delete {file.name}: {e}")
                    progress.update(task, advance=1)
            
            console.print(f"\n[bold green]✅ Deleted {deleted} duplicate files.[/bold green]")
