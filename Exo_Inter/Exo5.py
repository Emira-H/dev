import math

# Exercice 5
print("Exercice 5: des nombres en boucle bis")

for i in range(2, 101, 2):
    print(i)

# Exercice 6

print("Exercice 6 : remplir la piscine")

measures = input([length, width, depth,])

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
