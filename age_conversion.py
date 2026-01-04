# age_conversion.py

try:
    age_str = input("Quel âge as-tu ? ")
    age = int(age_str)
    print("Après conversion :", age, "→", type(age))
except ValueError:
    print("Saisie invalide, merci d'entrer un entier.")

# Exemple float
try:
    note_str = input("Saisis une note (décimal possible) : ")
    note = float(note_str)
    print("Après conversion :", note, "→", type(note))
except ValueError:
    print("Saisie invalide, merci d'entrer un nombre.")
