from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt
from .config import load_config

console = Console()
config = load_config()


def bulk_rename(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    files = [f for f in target.iterdir() if f.is_file()]
    if not files:
        console.print("[yellow]No files found to rename.[/yellow]")
        return

    console.print(f"[cyan]{len(files)} files found.[/cyan]")
    
    pattern = Prompt.ask("Enter new name pattern (use {n} for number)", default="file_{n}")
    start_num = int(Prompt.ask("Starting number", default="1"))

    renamed_count = 0
    for i, file in enumerate(files, start=start_num):
        new_name = pattern.replace("{n}", str(i)) + file.suffix
        new_path = target / new_name

        counter = 1
        while new_path.exists():
            name, suffix = Path(new_name).stem, Path(new_name).suffix
            new_name = f"{name}_{counter}{suffix}"
            new_path = target / new_name
            counter += 1

        try:
            file.rename(new_path)
            console.print(f"[green]Renamed:[/green] {file.name} → {new_name}")
            renamed_count += 1
        except Exception as e:
            console.print(f"[red]Failed to rename {file.name}: {e}[/red]")

    console.print(f"\n[bold green]✅ Successfully renamed {renamed_count} files.[/bold green]")
