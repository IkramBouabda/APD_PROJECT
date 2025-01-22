import json
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table

# Initialize Colorama
init(autoreset=True, convert=True)
# Console for Rich
console = Console()

# File path
QUESTIONS_FILE = "AP_PROJECT\Quextions\questions.json"

# Load questions from JSON
try:
    with open(QUESTIONS_FILE, "r") as f:
        questions = json.load(f)
except FileNotFoundError:
    questions = []

# Functions for Question Management
def add_question(category, question, options, correct_answer):
    if correct_answer not in options:
        console.print(f"{Fore.RED}Error: Correct answer must be one of the options.{Style.RESET_ALL}")
        return
    questions.append({
        "category": category,
        "question": question,
        "options": options,
        "correct_answer": correct_answer
    })
    console.print(f"{Fore.GREEN}Question added successfully.{Style.RESET_ALL}")

def display_questions():
    if not questions:
        console.print(f"{Fore.YELLOW}No questions available.{Style.RESET_ALL}")
        return

    table = Table(title="Question List")
    table.add_column("#", style="cyan", justify="center")
    table.add_column("Category", style="magenta", justify="left")
    table.add_column("Question", style="dim cyan", justify="left")
    table.add_column("Options", style="yellow", justify="left")
    table.add_column("Correct Answer", style="green", justify="center")

    for i, question in enumerate(questions, start=1):
        options_formatted = ", ".join(question['options'])
        table.add_row(
            str(i),
            question['category'],
            question['question'],
            options_formatted,
            question['correct_answer']
        )

    console.print(table)

def save_questions():
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(questions, f, indent=4)
    console.print(f"{Fore.GREEN}Questions saved to JSON file.{Style.RESET_ALL}")

# Menu for Question Management
if __name__ == "__main__":
    while True:
        console.rule("\n[bold green]Question Management Menu[/bold green]")
        console.print("[bold green]1.[/bold green] Add Question")
        console.print("[bold green]2.[/bold green] Display Questions")
        console.print("[bold green]3.[/bold green] Save Questions")
        console.print("[bold green]4.[/bold green] Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            category = input("Enter the category: ")
            question = input("Enter the question: ")
            options = input("Enter options separated by commas: ").split(",")
            correct_answer = input("Enter the correct answer: ")
            add_question(
                category.strip(),
                question.strip(),
                [opt.strip() for opt in options],
                correct_answer.strip()
            )
        elif choice == "2":
            display_questions()
        elif choice == "3":
            save_questions()
        elif choice == "4":
            save_questions()
            console.print(f"{Fore.CYAN}Exiting... Goodbye!{Style.RESET_ALL}")
            break
        else:
            console.print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
