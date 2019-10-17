##Partie 2
exo1="Exercice 1: True ou False"
print(exo1)
var1="Coucou Bruno"
var2=""
if len(var1)==0 and len(var2)==0:
    print("True")
else:
    print("False")

exo2="Exercice 2: Calculer mon âge"
print(exo2)
year=int(input("quelle est l'année actuelle? "))
birth_year=int(input("quelle est votre année de naissance? "))
age=year-birth_year
print(age)
neighbour_age=int(input("quelle est l'age de votre voisin? "))
print(40+neighbour_age)

exo3="Exercice 3:Problème de chaussures"
print(exo3)
prix1=70
prix2=59
prix3=20
total=(prix1+prix2+prix3)*0.8
print(total)

exo4="Exercice 4: une calculatrice Python"
print(exo4)
nombre1=float(input("Saisir un nombre "))
nombre2=float(input("Saisir un deuxième nombre "))
somme= nombre1+nombre2
print(somme)

exo5="Exercice 5: travailler avec les propriétés"
print(exo5)
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

age_user=float(input("Saisissez votre age"))
print(int(round(age_user/33,0)))
