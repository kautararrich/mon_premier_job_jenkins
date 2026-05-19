import sys

print("=" * 40)
print("bienvenue dans mon premier job jenkins")
print("=" * 40)

if len(sys.argv) > 1 :
    nom = sys.argv[1]
else:
    nom = "etu jenkins"
print(f"bonjour {nom}, ton job jenkins a reussi")

a = 10
b = 5
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")

assert a+b ==15, "erreur dans le calcul"

print("tous les tests passent avec succes")

