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
    console = Users.User_management.Console()
    console.rule("[bold green]Welcome to the QCM Application![/bold green]")

    user_data = load_user_data(USER_DATA_FILE)
    questions = load_questions(QUESTION_FILE)

    # Demander l'ID utilisateur en premier
    user_id = input("Enter your user ID: ")
    if user_id not in user_data:
        name = input("Enter your name to register: ")
        user_data = register_user(user_id, name, user_data)
          
    # Afficher l'historique de l'utilisateur
    display_user_history(user_id, user_data)
    
    # Charger et afficher les catégories disponibles
    available_categories = get_and_display_categories(QUESTION_FILE)
    if not available_categories:
        print(Fore.RED + "No QCM yet, be back soon !")
        return
    
    # Demander à l'utilisateur de choisir une catégorie par son index, avec boucle
    selected_category = None
    while selected_category is None:
        try:
            category_index = int(input("Choose a category : "))
            if 0 <= category_index < len(available_categories):
                selected_category = available_categories[category_index]
                print(Fore.CYAN + f"Say bissmiAllah we're starting a QCM : {selected_category}")
            else:
                print(Fore.RED + "Error : Invalid Index of category. Retry.")
        except ValueError:
            print(Fore.RED + "Error : Enter a valid number.")
    
    # Lancer le test pour la catégorie choisie
    administer_test(user_id, selected_category, questions, lambda u, c, s: add_test_result(u, c, s, user_data))
      # Sauvegarder les données utilisateur
    save_user_data(USER_DATA_FILE, user_data)
    

if __name__ == "__main__":
    main()
