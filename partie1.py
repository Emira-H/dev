#Exercice 1: Hello world
print("hello world")
var = "hello world"
print(var)

#Exercice 2: Calculs divers
#probleme pour division 0
print(3*3)
try:
    print(12/0)
except ZeroDivisionError:
    print(4+9+78)
    print(12-7)
    print(5e4)

#Exercice 3: communiquer avec l'ordinateur
message="Entrer votre nom"
name_user=input(message)
print("bienvenue", name_user)

#Exercice 4: Nom et prénom
Nom="Harrioui"
Prenom="Emira"
print("Bonjour "+ Prenom +" "+ Nom)

#Exercice 5:Des caractères au nombre
myNumber="123"
myNumber = int(myNumber)
print(myNumber)
print(type(myNumber))

#Exercice 6:Majuscules et minuscules
word_user=input("Entrer un mot")
print(word_user.upper())
print(word_user.lower())
