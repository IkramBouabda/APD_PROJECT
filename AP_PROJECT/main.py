from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
import json
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

def get_and_display_categories(question_file):
    """
    Charge les catégories disponibles à partir du fichier questions.json et les affiche avec des index.
    
    :param question_file: Chemin vers le fichier JSON contenant les questions.
    :return: Liste des catégories uniques.
    """
    try:
        with open(question_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Récupérer les catégories uniques
            categories = list({question["category"] for question in data if "category" in question})
            # Afficher les catégories avec des index
            print(Fore.YELLOW + "Choose a categorie :")
            for i, category in enumerate(categories):
                print(Fore.GREEN + f"{i} - {category}")
            return categories
    except FileNotFoundError:
        print(Fore.RED + f"Error : {question_file} no such file")
        return []
    except json.JSONDecodeError:
        print(Fore.RED + f"Error : The file {question_file} contains invalid data.")
        return []

def export_results_to_text(user_data, file_name="user_results.txt"):
    """
    Exporte les résultats des utilisateurs dans un fichier texte.

    :param user_data: Dictionnaire contenant les données utilisateur.
    :param file_name: Nom du fichier texte de sortie.
    """
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write("User Test Results\n")
            f.write("=" * 40 + "\n\n")
            for user_id, data in user_data.items():
                f.write(f"User ID: {user_id}\n")
                f.write(f"Name: {data['name']}\n")
                f.write("Tests:\n")
                if not data.get("tests"):
                    f.write("  No tests taken.\n")
                else:
                    for test in data["tests"]:
                        f.write(f"  - Date: {test['date']}\n")
                        f.write(f"    Category: {test['category']}\n")
                        f.write(f"    Score: {test['score']}\n")
                f.write("\n" + "-" * 40 + "\n")
        print(f"Results exported successfully to {file_name}!")
    except Exception as e:
        print(f"Error exporting results: {e}")

def main():
    # Initialisation de la console pour l'affichage stylisé
    console = Users.User_management.Console()
    console.rule("[bold green]Welcome to the QCM Application![/bold green]")
    
    # Charger les données utilisateur et les questions
    user_data = load_user_data(USER_DATA_FILE)
    questions = load_questions(QUESTION_FILE)
    
    while True:
        # Afficher le menu principal
        print("\n" + Fore.BLUE + "=" * 50)
        print(Fore.YELLOW + "Menu Options:")
        print("[1] Login/Register User")
        print("[2] Start a New Test")
        print("[3] Display User History")
        print("[4] Export User Results to Text")
        print("[5] Exit")
        print(Fore.BLUE + "=" * 50)

        # Demander à l'utilisateur de faire un choix
        choice = input(Fore.CYAN + "Choose an option: ")

        if choice == "1":
            # Connexion ou inscription
            user_id = input("Enter your user ID: ")
            if user_id not in user_data:
                name = input("Enter your name to register: ")
                user_data = register_user(user_id, name, user_data)
            else:
                print(Fore.GREEN + "Welcome back!")
            # Sauvegarder les données utilisateur
            save_user_data(USER_DATA_FILE, user_data)

        elif choice == "2":
            # Vérifier si l'utilisateur est connecté
            if not user_data:
                print(Fore.RED + "Error: No users registered. Please register first.")
                continue

            # Demander à l'utilisateur son ID pour démarrer un test
            user_id = input("Enter your user ID: ")
            if user_id not in user_data:
                print(Fore.RED + "Error: User ID not found. Please register first.")
                continue
            
            # Charger et afficher les catégories disponibles
            available_categories = get_and_display_categories(QUESTION_FILE)
            if not available_categories:
                print(Fore.RED + "No QCM available at the moment. Try again later.")
                continue
            
            # Demander à l'utilisateur de choisir une catégorie
            selected_category = None
            while selected_category is None:
                try:
                    category_index = int(input("Choose a category: "))
                    if 0 <= category_index < len(available_categories):
                        selected_category = available_categories[category_index]
                        print(Fore.CYAN + f"Starting the QCM for category: {selected_category}")
                    else:
                        print(Fore.RED + "Invalid category index. Please try again.")
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a number.")

            # Administrer le test
            administer_test(user_id, selected_category, questions, lambda u, c, s: add_test_result(u, c, s, user_data))
            # Sauvegarder les résultats
            save_user_data(USER_DATA_FILE, user_data)

        elif choice == "3":
            # Afficher l'historique d'un utilisateur
            user_id = input("Enter your user ID to view history: ")
            if user_id in user_data:
                display_user_history(user_id, user_data)
            else:
                print(Fore.RED + "Error: User ID not found.")

        elif choice == "4":
            # Exporter les résultats des utilisateurs dans un fichier texte
            export_results_to_text(user_data)

        elif choice == "5":
            # Quitter l'application
            save_user_data(USER_DATA_FILE, user_data)
            print(Fore.YELLOW + "Exiting... Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")


    

if __name__ == "__main__":
    main()
