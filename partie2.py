##Partie 2
#Exercice 1: True ou False
var1="Coucou Bruno"
var2=""
if len(var1)==0 and len(var2)==0:
    print("True")
else:
    print("False")

#Exercice 2: Calculer mon âge

year=int(input("quelle est l'année actuelle? "))
birth_year=int(input("quelle est votre année de naissance? "))
age=year-birth_year
print(age)
neighbour_age=int(input("quelle est l'age de votre voisin? "))
print(40+neighbour_age)

#Exercice 3: Problème de chaussures

prix1=70
prix2=59
prix3=20
total=(prix1+prix2+prix3)*0.8
print(total)

#Exercice 4: une calculatrice Python

nombre1=float(input("Saisir un nombre "))
nombre2=float(input("Saisir un deuxième nombre "))
somme= nombre1+nombre2
print(somme)

#Exercice 5: travailler avec les propriétés

prenom=input("Quel est votre prénom?" )
nom=input("Quel est votre nom?" )
PremLettre_prenom=prenom[0]
DernLettre_prenom=prenom[-1]
initial_prenom=PremLettre_prenom+DernLettre_prenom
PremLettre_nom=nom[0]
DernLettre_nom=nom[-1]
initial_nom=PremLettre_nom+DernLettre_nom

print(initial_prenom.upper())
print(initial_nom.upper())
print((initial_prenom+initial_nom).upper())
