import json
import time
from threading import Timer
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


init(autoreset=True, convert=True)

def administer_test(user_id, category, questions, add_test_result, time_limit_per_question=10):
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

        # Variable pour détecter si le temps est écoulé
        time_is_up = False

        # Fonction appelée lorsque le temps est écoulé
        def time_up():
            nonlocal time_is_up
            time_is_up = True
            console.print(f"\n{Fore.RED}Time's up! Moving to the next question.{Style.RESET_ALL}")

        # Initialiser le timer
        timer = Timer(time_limit_per_question, time_up)
        timer.start()

        try:
            # Demander une réponse
            start_time = time.time()
            answer = input(f"You have {time_limit_per_question} seconds to answer: ")
            elapsed_time = time.time() - start_time
            timer.cancel()

            if time_is_up:
                # Si le temps est écoulé avant que l'utilisateur ne réponde
                continue

            if elapsed_time > time_limit_per_question:
                console.print(f"\n{Fore.RED}Time's up! Moving to the next question.{Style.RESET_ALL}")
            elif question['options'][int(answer) - 1] == question['correct_answer']:
                console.print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}")
                score += 1
            else:
                console.print(f"{Fore.RED}Incorrect. The correct answer is: {question['correct_answer']}{Style.RESET_ALL}")
        except (ValueError, IndexError):
            console.print(f"{Fore.RED}Invalid input! The correct answer is: {question['correct_answer']}{Style.RESET_ALL}")
        finally:
            timer.cancel()  # Assurez-vous que le timer est annulé, même en cas d'erreur

    console.print(f"\n[bold green]Test complete! Your score: {score}/{len(questions_in_category)}[/bold green]")
    add_test_result(user_id, category, score)
