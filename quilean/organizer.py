from pathlib import Path
import os
from rich.console import Console
from rich.progress import Progress
from .config import load_config
from .history import save_operation
from .logger import logger

console = Console()
config = load_config()


def organize_files(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    files = [item for item in target.iterdir() if item.is_file()]
    if not files:
        console.print("[yellow]No files found to organize.[/yellow]")
        return

    moved_files = []
    folders_config = config["folders"]

    with Progress() as progress:
        task = progress.add_task("[green]Organizing files...", total=len(files))

        for item in files:
            ext = item.suffix.lower()
            moved = False

            for folder_name, extensions in folders_config.items():
                if ext in [e.lower() for e in extensions]:
                    folder_path = target / folder_name
                    folder_path.mkdir(exist_ok=True)

                    dest = folder_path / item.name
                    counter = 1
                    original_name = item.name
                    
                    while dest.exists():
                        name, suffix = os.path.splitext(original_name)
                        dest = folder_path / f"{name}_{counter}{suffix}"
                        counter += 1

                    item.rename(dest)
                    moved_files.append({"from": str(item), "to": str(dest)})
                    logger.info(f"Moved {item.name} to {folder_name}/")
                    moved = True
                    break

            if not moved:
                folder_path = target / "Others"
                folder_path.mkdir(exist_ok=True)
                dest = folder_path / item.name
                item.rename(dest)
                moved_files.append({"from": str(item), "to": str(dest)})
                logger.info(f"Moved {item.name} to Others/")

            progress.update(task, advance=1)

    if moved_files:
        save_operation("organize", {
            "target": str(target),
            "moved_files": moved_files
        })
        console.print(f"\n[bold green]✅ Organization completed! {len(moved_files)} files moved.[/bold green]")
