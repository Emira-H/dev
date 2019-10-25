## Exercice 1: le nombre le plus grand
# définition des 4 variables
import math,random
a = random.randint(1,20)
b = random.randint(1,20)
c = random.randint(1,20)
d = random.randint(1,20)

liste = [a,b,c,d]
#Méthode1
print(liste)
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
