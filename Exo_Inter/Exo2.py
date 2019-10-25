import math
print("Exercice 2: condition d'âge")

age_user = input("Quel est votre âge? ")

if int(age_user) < 0:
    print("Merci de bien vouloir entrer votre âge réél!")

if int(age_user) >= 21:
    print("Accès autorisé.")

if int(age_user) % 2 == 0:
    print("Votre âge est pair.")

if int(age_user) == int(math.sqrt(age_user)) * int(math.sqrt(age_user)):
    print("Votre âge est un nombre carré.")

if len(age_user) == 0:
    print("Erreur! ")
