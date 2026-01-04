# texte.py

texte = input("Entre un mot ou une phrase : ")
print("Longueur :", len(texte))
print("Majuscules :", texte.upper())
print("Minuscules :", texte.lower())
print("Inversé :", texte[::-1])

# Vérification palindrome
texte_simplifie = texte.replace(" ", "").lower()
if texte_simplifie == texte_simplifie[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome")
