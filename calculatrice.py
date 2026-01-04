# calculatrice.py

try:
    n1 = float(input("Premier nombre : "))
    n2 = float(input("Deuxième nombre : "))
except ValueError:
    print("Saisie invalide")
    exit(1)

operateur = input("Choisis une opération (+, -, *, /) : ").strip()

if operateur == "+":
    resultat = n1 + n2
elif operateur == "-":
    resultat = n1 - n2
elif operateur == "*":
    resultat = n1 * n2
elif operateur == "/":
    if n2 != 0:
        resultat = n1 / n2
    else:
        print("Erreur : division par zéro")
        exit(1)
else:
    print("Opérateur invalide")
    exit(1)

print(f"{n1} {operateur} {n2} = {resultat}")
