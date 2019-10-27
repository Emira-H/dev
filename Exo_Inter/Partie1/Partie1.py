## Exercice 1: le nombre le plus grand
# définition des 4 variables
import math,random
a = random.randint(1,20)
b = random.randint(1,20)
c = random.randint(1,20)
d = random.randint(1,20)

liste = [a,b,c,d]

#Méthode1

max1=0
for i in liste:
    if i>max1:
        max1=i
print(max1)
#Méthode2 avec fonction max
print(max(liste))

#Méthode3
if a>=b and a>=c and a>=d:
    print(a)
elif b>=a and b>=c and b>=d:
    print(b)
elif c>=a and c>=b and c>=d:
    print(c)
elif d>=a and d>=b and d>=c:
    print(d)

#Méthode4
liste.sort()
print(liste[-1])


#Exercice 2

print("Exercice 2: condition d'âge")

age_user = input("Quel est votre âge? ")

if int(age_user) < 0:
    print("Merci de bien vouloir entrer votre âge réél!")

if int(age_user) >= 21:
    print("Accès autorisé.")

if int(age_user) % 2 == 0:
    print("Votre âge est pair.")

#if int(age_user) == math.sqrt(age_user) * math.sqrt(age_user):
#    print("Votre âge est un nombre carré.")

if len(age_user) == 0:
    print("Erreur! ")

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

# Exercice 4

print("Exercice 4 : des nombres en boucle")

for i in range(1,101):
    print(i)

# Exercice 5

print("Exercice 5: des nombres en boucle bis")

for i in range(2, 101, 2):
    print(i)

# Exercice 6

print("Exercice 6 : remplir la piscine")

def filling_time(length, width, depth, flow):
    Volume = length * width * depth
    filling_time = Volume/flow
    print("Le temps de remplissage pour une piscine de dimensions L= {0} l= {1}"\
     "p= {2} et de débit {3} m3/min est égal à {4} min".format(length, width, depth, flow, filling_time))


filling_time(50, 20, 2, 10)



# Exercice 7

print("Exercice 7: calcul de cercle")

radius = float(input("Saisir le rayon du cercle "))

#function area
def area_circle(radius):

    Area = round( radius **2 * math.pi , 2)

    print("L'aire d'un cercle de rayon", radius, "cm est de", Area, "cm carré")


area_circle(radius)

#function perimeter

def perimeter_circle(radius):

    perimeter = round( 2 * radius * math.pi , 2)
    print("Le périmètre d'un cercle de rayon", radius, "cm est de", perimeter, "cm")

perimeter_circle(radius)


#Exercice 8

print("Exercice 8: une pyramide")


star = "*"
line_star = range(6)

for i in line_star:
    print(i*star)
    i += 1


# Exercice 9

print("Exercice 9 : FIZZ BUZZ")

sequence = range(1,101)

for i in sequence:
    if i%3 == 0 :
        print("FIZZ")

    elif i%5 == 0:
        print("BUZZ")

    elif i%3 == 0 and i%5 ==0:
        print("FIZZBUZZ")
    else:
        print(i)
