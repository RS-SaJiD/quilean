from pathlib import Path
from rich.console import Console
from rich.progress import Progress
from .config import load_config
from .logger import logger

console = Console()
config = load_config()

def add_smart_tags(target_path="."):
    target = Path(target_path).resolve()
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    files = [f for f in target.rglob("*") if f.is_file()]
    if not files:
        console.print("[yellow]No files found.[/yellow]")
        return

    console.print(f"[cyan]Applying smart tags to {len(files)} files...[/cyan]")

    keywords = {
        "important": ["important", "urgent", "final", "submission", "report", "invoice"],
        "backup": ["backup", "old", "copy", "bkp"],
        "personal": ["personal", "private", "family", "photo", "selfie"],
        "work": ["work", "office", "client", "meeting", "project", "proposal"],
        "archive": ["archive", "old", "202", "completed"]
    }

    tagged_count = 0

    with Progress() as progress:
        task = progress.add_task("[magenta]Tagging files...", total=len(files))

        for file in files:
            name_lower = file.name.lower()
            added = set()  # Use set to avoid duplicates

            for tag, words in keywords.items():
                if any(word in name_lower for word in words):
                    added.add(tag)

            if added:
                tag_str = ",".join(sorted(added))  # Sort for consistency
                new_name = f"[{tag_str}] {file.name}"
                try:
                    file.rename(file.parent / new_name)
                    console.print(f"[blue]Tagged:[/blue] {file.name} → {new_name}")
                    logger.info(f"Tagged {file.name} with {added}")
                    tagged_count += 1
                except Exception as e:
                    logger.error(f"Failed to tag {file.name}: {e}")

            progress.update(task, advance=1)

    console.print(f"\n[bold green]✅ Smart tagging completed! {tagged_count} files tagged.[/bold green]")
