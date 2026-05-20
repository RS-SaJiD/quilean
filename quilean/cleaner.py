from pathlib import Path
from rich.console import Console
from rich.progress import Progress
from rich.prompt import Confirm
from .config import load_config
from .logger import logger

console = Console()
config = load_config()

JUNK_EXTENSIONS = {'.tmp', '.temp', '.log', '.cache', '.pyc', '.pyo', '.DS_Store'}
JUNK_FOLDERS = {'__pycache__', '.cache', 'temp', 'logs'}


def clean_junk(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    console.print(f"[cyan]Scanning for junk files in:[/cyan] {target}")

    junk_items = []

    # Collect all junk items first
    for item in target.rglob("*"):
        if item.is_file() and item.suffix.lower() in JUNK_EXTENSIONS:
            junk_items.append(item)
        elif item.is_dir() and item.name in JUNK_FOLDERS:
            junk_items.append(item)

    if not junk_items:
        console.print("[bold green]🎉 No junk files or folders found![/bold green]")
        return

    console.print("[yellow]⚠️ Junk items found:[/yellow]")
    for item in junk_items:
        console.print(f"  - {item.relative_to(target)}")
    
    if not Confirm.ask(f"Delete {len(junk_items)} junk item(s)?", default=False):
        console.print("[yellow]Cleanup cancelled.[/yellow]")
        return

    deleted = 0

    with Progress() as progress:
        task = progress.add_task("[red]Cleaning junk items...", total=len(junk_items))

        for item in junk_items:
            try:
                if item.is_file():
                    item.unlink()
                    logger.info(f"Deleted junk file: {item.name}")
                elif item.is_dir():
                    import shutil
                    shutil.rmtree(item, ignore_errors=True)
                    logger.info(f"Deleted junk folder: {item.name}")
                deleted += 1
                console.print(f"[red]Deleted:[/red] {item.name}")
            except Exception as e:
                logger.error(f"Failed to delete {item}: {e}")

            progress.update(task, advance=1)

    console.print(f"\n[bold green]✅ Successfully cleaned {deleted} junk items.[/bold green]")
