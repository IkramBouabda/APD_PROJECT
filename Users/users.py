import json

# Données pour plusieurs utilisateurs
donnees = [
    {
        "id": "1",
        "nom": "Benhaik Meriem",
        "historique_qcm": [
            {"date": "2024-12-01", "score": 20},
            {"date": "2024-12-15", "score": 19}
        ]
    },
    {
        "id": "2",
        "nom": "Ait braham ryma",
        "historique_qcm": [
            {"date": "2024-12-05", "score":20}
        ]
    },
    {
        "id": "3",
        "nom": "Bouabda Ikram",
        "historique_qcm": []
    }
]

nom_fichier = "utilisateurs.json"
with open(nom_fichier, "w") as fichier:
    json.dump(donnees, fichier, indent=4, ensure_ascii=False)
