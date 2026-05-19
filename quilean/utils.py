from pathlib import Path
from rich.console import Console
from rich.table import Table
from .config import load_config

console = Console()
config = load_config()


def show_stats(target_path="."):
    target = Path(target_path).resolve()
    
    if not target.exists():
        console.print("[red]Error: Path does not exist![/red]")
        return

    files = [f for f in target.rglob("*") if f.is_file()]
    dirs = [d for d in target.iterdir() if d.is_dir()]
    
    total_size = sum(f.stat().st_size for f in files)
    size_mb = total_size / (1024 * 1024)

    table = Table(title="📊 Folder Statistics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Total Files", str(len(files)))
    table.add_row("Total Folders", str(len(dirs)))
    table.add_row("Total Size", f"{size_mb:.2f} MB")
    table.add_row("Largest File", max((f.stat().st_size for f in files), default=0) / (1024*1024))

    console.print(table)
