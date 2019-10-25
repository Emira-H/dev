#Exercice 3

print("Exercice 3:le nombre caché")


secret_number = 23

number_user = int(input("Devinez le nombre caché: ")                          )

while number_user > secret_number :
    print("Mauvaise réponse, le nombre caché est plus petit")
    number_user = int(input("Devinez le nombre caché: "))

while number_user < secret_number :
    print("Mauvaise réponse, le nombre caché est plus grand")
    number_user = int(input("Devinez le nombre caché: "))

if number_user == secret_number:
     print("Vous avez gagné!")
