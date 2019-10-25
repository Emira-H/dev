exo1="Exercice 1: Hello world"
print=exo1
print("hello world")
var = "hello word"
print(var)

exo2="Exercice 2: Calculs divers"
print(exo2)
print(3*3)
try:
    print(12/0)
except ZeroDivisionError:
    print(4+9+78)
    print(12-7)
    print(5e4)

exo3="Exercice 3: communiquer avec l'ordinateur"
print(exo3)
message="Entrer votre nom"
name_user=input(message)
print("bienvenue", name_user)
print("bonjour {}".format(nom))

exo4="Exercice 4: Nom et prénom"
print(exo4)
Nom = "Harrioui"
Prenom = "Emira"
print("Bonjour {} {}".format(Prenom, Nom))
print("Bonjour "+ Prenom +" "+ Nom)

exo5="Exercice 5:Des caractères au nombre"
print(exo5)
myNumber="123"
myNumber = int(myNumber)
print(myNumber)
print(type(myNumber))

exo6="Exercice 6:Majuscules et minuscules"
print(exo6)
word_user=input("Entrer un mot")
print(word_user.upper())
print(word_user.lower())
