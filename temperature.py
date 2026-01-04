# temperature.py

try:
    c = float(input("Température en °C : "))
except ValueError:
    print("Saisie invalide")
    exit(1)

f = c * 9/5 + 32
k = c + 273.15
print(f"{c}°C = {f}°F = {k}K")

# Bonus : conversion inverse
try:
    f_input = float(input("Température en °F : "))
except ValueError:
    print("Saisie invalide")
    exit(1)

c_from_f = (f_input - 32) * 5/9
k_from_f = c_from_f + 273.15
print(f"{f_input}°F = {c_from_f:.2f}°C = {k_from_f:.2f}K")
