##Partie 2
exo1="Exercice 1: True ou False"
print(exo1)

#2ème méthode
var = ""
var1= "test"
print(len(var))==0)
print(len(var1)==0)

# 3ème méthode avec le booléén
print(bool(var))
print(bool(var1))


exo2="Exercice 2: Calculer mon âge"
print(exo2)
year = int(input("quelle est l'année actuelle? "))
birth_year = int(input("quelle est votre année de naissance? "))
age = year-birth_year
print(age)
neighbour_age = int(input("quelle est l'age de votre voisin? "))
print(40+neighbour_age)


exo3="Exercice 3:Problème de chaussures"
print(exo3)
prix1=70
prix2=59
prix3=20
total=(prix1+prix2+prix3)*0.8
print(total)

#Méthode de Sofiane avec lambda
somme = lambda total:total * 0,8
print("le prix total est {}.format(somme(prix1 + prix2 + prix3))")

exo4 = "Exercice 4: une calculatrice Python"
print(exo4)
nombre1 = float(input("Saisir un nombre "))
nombre2 = float(input("Saisir un deuxième nombre "))
somme = nombre1 + nombre2
print(somme)

exo5="Exercice 5: travailler avec les propriétés"
print(exo5)

prenom = input("Quel est votre prénom?" )
nom = input("Quel est votre nom?" )

PremLettre_prenom = prenom[0]
DernLettre_prenom = prenom[-1]
initial_prenom = PremLettre_prenom+DernLettre_prenom

PremLettre_nom = nom[0]
DernLettre_nom = nom[-1]
initial_nom = PremLettre_nom + DernLettre_nom

print(initial_prenom.upper())
print(initial_nom.upper())
print(initial_prenom + initial_nom)

age_user = float(input("Saisissez votre age"))
print(round(age_user / 33))
