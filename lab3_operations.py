# lab3_operations.py

# Variables de test
a = 15
b = 4

# Opérations arithmétiques
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")      
print(f"{a} // {b} = {a // b}")    
print(f"{a} % {b} = {a % b}")      
print(f"{a} ** {b} = {a ** b}")    

# Comparaisons
x = 20
y = 15
print(f"x == y → {x == y}")
print(f"x != y → {x != y}")
print(f"x < y → {x < y}")
print(f"x > y → {x > y}")
print(f"x <= y → {x <= y}")
print(f"x >= y → {x >= y}")

# Logique booléenne
age = 22
permis = True
casier_vierge = False
peut_conduire = (age >= 18) and permis
print(f"Peut conduire → {peut_conduire}")
peut_louer_voiture = (age >= 21) or (permis and casier_vierge)
print(f"Peut louer voiture → {peut_louer_voiture}")
sanction = not casier_vierge
print(f"Sanction → {sanction}")

# Mini-projet : réduction prix
try:
    prix_initial = float(input("Prix du produit (€) : "))
except ValueError:
    print("Saisie invalide")
    exit(1)

statut = input("Êtes-vous étudiant ? (o/n) ").strip().lower()
fidelite = input("Fidélité (en années) : ").strip()
try:
    fidelite = int(fidelite)
except ValueError:
    print("Saisie invalide")
    exit(1)

reduction = 0.0
if statut == "o":
    reduction += prix_initial * 0.10
if fidelite >= 5:
    reduction += prix_initial * 0.15
if prix_initial > 100:
    reduction += 5.0

prix_final = prix_initial - reduction
if prix_final < 0:
    prix_final = 0.0

print(f"Réduction totale : {reduction:.2f} €")
print(f"Prix final : {prix_final:.2f} €")
