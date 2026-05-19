from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

def show_stats(target_path="."):
    target = Path(target_path).resolve()
    
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    files = [f for f in target.rglob("*") if f.is_file()]
    dirs = [d for d in target.rglob("*") if d.is_dir()]
    total_size = sum(f.stat().st_size for f in files)

    table = Table(title="📊 Folder Statistics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Total Files", str(len(files)))
    table.add_row("Total Folders", str(len(dirs)))
    table.add_row("Total Size", f"{total_size / (1024*1024):.2f} MB")

    console.print(table)
