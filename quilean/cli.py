import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

from .organizer import organize_files
from .renamer import bulk_rename
from .cleaner import clean_junk
from .utils import show_stats
from .history import get_last_operation

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


@main.command()
def undo():
    """Undo the last operation"""
    last_op = get_last_operation()
    if not last_op:
        console.print("[yellow]No operation history found to undo.[/yellow]")
        return

    console.print(f"[bold yellow]Last Operation:[/bold yellow] {last_op['operation']} at {last_op['timestamp']}")
    
    if last_op['operation'] == "organize":
        moved_files = last_op['details'].get('moved_files', [])
        for file in reversed(moved_files):
            try:
                Path(file['to']).rename(file['from'])
                console.print(f"[green]Reverted:[/green] {Path(file['to']).name}")
            except Exception as e:
                console.print(f"[red]Failed to revert {file['to']}: {e}[/red]")
        console.print("[bold green]✅ Undo completed successfully![/bold green]")
    else:
        console.print("[yellow]Undo for this operation type is not implemented yet.[/yellow]")


if __name__ == "__main__":
    main()
