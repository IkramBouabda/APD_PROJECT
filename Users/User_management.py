import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style

# Initialize Console globally
console = Console()

def load_user_data(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_user_data(file_path, user_data):
    with open(file_path, "w") as f:
        json.dump(user_data, f, indent=4)
    
def register_user(user_id, name, user_data):
    if user_id in user_data:
        console.print(f"[red]User {user_id} already exists.[/red]")
        return user_data
    user_data[user_id] = {"name": name, "tests": []}
    console.print(f"[green]User {name} registered successfully.[/green]")
    return user_data

def display_user_history(user_id, user_data):
    if user_id not in user_data:
        console.print(f"[red]User {user_id} does not exist.[/red]")
        return

    history_table = Table(title=f"History for {user_data[user_id]['name']}")
    history_table.add_column("Date", style="cyan")
    history_table.add_column("Category", style="magenta")
    history_table.add_column("Score", style="green")

    for test in user_data[user_id]["tests"]:
        history_table.add_row(test['date'], test['category'], str(test['score']))

    console.print(history_table)

def add_test_result(user_id, category, score, user_data):
    if user_id not in user_data:
        console.print(f"[red]User {user_id} does not exist. Please register first.[/red]")
        return user_data
    test_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_data[user_id]["tests"].append({"date": test_date, "category": category, "score": score})
    return user_data
