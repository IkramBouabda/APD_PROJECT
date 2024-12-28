import json
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style,init

# Initialize colorama with conversion
init(autoreset=True, convert=True)
def load_questions(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def administer_test(user_id, category, questions, add_test_result):
    console = Console()
    questions_in_category = [q for q in questions if q['category'].lower() == category.lower()]
    if not questions_in_category:
        console.print("[yellow]No questions available in this category.[/yellow]")
        return

    score = 0
    for j, question in enumerate(questions_in_category, start=1):
        console.print(f"{Fore.CYAN}Question {j} :{Fore.LIGHTBLACK_EX} {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            console.print(f"  {i}. {Fore.LIGHTBLACK_EX}{option}")
        try:
            answer = int(input("Your answer: "))
            if question['options'][answer - 1] == question['correct_answer']:
                console.print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                score += 1
            else:
                console.print(f"{Fore.RED}Incorrect. The correct answer is: {question['correct_answer']}{Style.RESET_ALL}")
        except (ValueError, IndexError):
            console.print(f"{Fore.RED}Invalid input!. The correct answer is: {question['correct_answer']}{Style.RESET_ALL}")

    console.print(f"\n[bold green]Test complete! Your score: {score}/{len(questions_in_category)}[/bold green]")
    add_test_result(user_id, category, score)
