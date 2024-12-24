import json

# Charger les données depuis un fichier JSON
def charger_donnees(fichier):
    try:
        with open(fichier, 'r') as f:
            return json.load(f)  # La donnée est une liste directement
    except FileNotFoundError:
        return []  # Retourne une liste vide si le fichier n'existe pas

# Sauvegarder les données dans un fichier JSON
def sauvegarder_donnees(fichier, donnees):
    with open(fichier, 'w') as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)

# Créer un nouvel utilisateur
def creer_utilisateur(donnees, nom_utilisateur):
    nouvel_id = str(len(donnees) + 1)  # Générer un ID unique
    nouvel_utilisateur = {
        "id": nouvel_id,
        "nom": nom_utilisateur,
        "historique_qcm": []
    }
    donnees.append(nouvel_utilisateur)
    print(f"L'utilisateur '{nom_utilisateur}' a été créé avec succès.")
    return nouvel_utilisateur

# Fonction principale : chercher ou créer un utilisateur
def chercher_ou_creer_utilisateur(fichier, nom_utilisateur):
    donnees = charger_donnees(fichier)
    
    # Supprimer tous les espaces internes et convertir en minuscules
    nom_utilisateur_min = "".join(nom_utilisateur.strip().lower().split())
    
    # Affichage de la bienvenue avant de chercher ou créer un utilisateur
    
    # Rechercher l'utilisateur
    for utilisateur in donnees:
        # Supprimer les espaces internes et convertir en minuscules
        utilisateur_nom_min = "".join(utilisateur["nom"].strip().lower().split())
        
        if utilisateur_nom_min == nom_utilisateur_min:
            print(f"Historique de {utilisateur['nom']} :")
            for qcm in utilisateur["historique_qcm"]:
                print(f" - Date: {qcm['date']}, Score: {qcm['score']}/20")
            return utilisateur

    # Si l'utilisateur n'est pas trouvé, le créer
    nouvel_utilisateur = creer_utilisateur(donnees, nom_utilisateur)
    sauvegarder_donnees(fichier, donnees)
    return nouvel_utilisateur

# Exemple d'utilisation
fichier = "utilisateurs.json"
print("Bienvenue au QCM Informatique !")
nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
chercher_ou_creer_utilisateur(fichier, nom_utilisateur)
