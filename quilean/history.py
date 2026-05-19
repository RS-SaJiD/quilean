import json
from pathlib import Path
from datetime import datetime
from rich.console import Console

console = Console()

HISTORY_FILE = Path.home() / ".quilean" / "history.json"

def save_operation(operation_type, details):
    """Save operation for undo"""
    HISTORY_FILE.parent.mkdir(exist_ok=True)
    
    history = []
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
        except:
            history = []

    record = {
        "timestamp": datetime.now().isoformat(),
        "operation": operation_type,
        "details": details
    }
    
    history.append(record)
    
    # Keep only last 10 operations
    if len(history) > 10:
        history = history[-10:]
    
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def get_last_operation():
    """Get last operation for undo"""
    if not HISTORY_FILE.exists():
        return None
    
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
        return history[-1] if history else None
    except:
        return None

def clear_history():
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()
