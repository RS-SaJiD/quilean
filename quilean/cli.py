import click
from rich.console import Console
from rich.panel import Panel
from .organizer import organize_files
from .renamer import bulk_rename
from .cleaner import clean_junk
from .utils import show_stats

console = Console()

@click.group()
@click.version_option(version="1.0.0")
def main():
    """Quilean - Smart File Organizer & Cleaner CLI"""
    pass

@main.command()
@click.argument("path", default=".", required=False)
def organize(path):
    """Organize files into folders by type"""
    console.print(Panel.fit("[bold green]Starting Smart Organization...[/bold green]"))
    organize_files(path)
    console.print("[bold green]✅ Organization completed![/bold green]")

@main.command()
@click.argument("path", default=".", required=False)
def rename(path):
    """Bulk rename files with pattern"""
    console.print(Panel.fit("[bold cyan]Bulk Rename Tool[/bold cyan]"))
    bulk_rename(path)

@main.command()
@click.argument("path", default=".", required=False)
def clean(path):
    """Clean junk and temporary files"""
    console.print(Panel.fit("[bold yellow]Cleaning junk files...[/bold yellow]"))
    clean_junk(path)

@main.command()
@click.argument("path", default=".", required=False)
def stats(path):
    """Show folder statistics"""
    show_stats(path)

if __name__ == "__main__":
    main()
