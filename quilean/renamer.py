from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def bulk_rename(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    files = [f for f in target.iterdir() if f.is_file()]
    if not files:
        console.print("[yellow]No files found in this directory.[/yellow]")
        return

    console.print(f"[cyan]{len(files)} files found.[/cyan]")
    pattern = Prompt.ask("Enter new name pattern (use {n} for number)", default="file_{n}")
    start_num = int(Prompt.ask("Starting number", default="1"))

    for i, file in enumerate(files, start=start_num):
        new_name = pattern.replace("{n}", str(i)) + file.suffix
        new_path = target / new_name

        counter = 1
        while new_path.exists():
            new_name = f"{pattern.replace('{n}', str(i))}_{counter}{file.suffix}"
            new_path = target / new_name
            counter += 1

        file.rename(new_path)
        console.print(f"[green]Renamed:[/green] {file.name} → {new_name}")
