from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
import Users.User_management
from Users.User_management import (
    load_user_data, save_user_data, register_user, display_user_history, add_test_result
)
from QCM.testAdministration import load_questions, administer_test

# Initialisation de colorama
init(autoreset=True)
# File paths
USER_DATA_FILE = "User_data.json"
QUESTION_FILE = "questions.json"

def main():
    console = Users.User_management.Console()
    console.rule("[bold green]Welcome to the QCM Application![/bold green]")
    
    user_data = load_user_data(USER_DATA_FILE)
    questions = load_questions(QUESTION_FILE)
    
    user_id = input("Enter your user ID: ")
    if user_id not in user_data:
        name = input("Enter your name to register: ")
        user_data = register_user(user_id, name, user_data)
    
    display_user_history(user_id, user_data)
    
    category = input("Enter the category for the QCM (e.g: Databases, Complexity): ")
    administer_test(user_id, category, questions, lambda u, c, s: add_test_result(u, c, s, user_data))
    
    save_user_data(USER_DATA_FILE, user_data)

if __name__ == "__main__":
    main()
