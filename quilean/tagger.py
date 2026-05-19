from pathlib import Path
from rich.console import Console
from rich.prompt import Confirm
from .config import load_config

console = Console()
config = load_config()


def add_smart_tags(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    console.print(f"[cyan]Applying smart tags in:[/cyan] {target}")
    tagged = 0

    keywords = {
        "important": ["important", "urgent", "final", "report"],
        "backup": ["backup", "old", "copy"],
        "personal": ["personal", "private", "family"],
        "work": ["work", "office", "client", "meeting"]
    }

    for file in target.rglob("*"):
        if file.is_file():
            name_lower = file.name.lower()
            added_tags = []

            for tag, words in keywords.items():
                if any(word in name_lower for word in words):
                    # For now, we'll just print suggested tag (we can extend to rename or metadata later)
                    console.print(f"[blue][TAG][/blue] {file.name} → [bold]{tag}[/bold]")
                    added_tags.append(tag)
                    tagged += 1

    if tagged == 0:
        console.print("[yellow]No files matched smart tagging rules.[/yellow]")
    else:
        console.print(f"\n[bold green]✅ Smart tagging completed on {tagged} files.[/bold green]")
