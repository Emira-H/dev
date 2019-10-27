# Exercice 3
import math

print("Exercice 3: Nombre pair")

Number_user = math.ceil(int(input("Saisir un nombre")))

def test_pair(x):

    if x==0:
        print(True)
        return
    elif x % 2 == 0:
        print(True)
        return test_pair(math.ceil(int(input("Saisir un nombre"))))
    else:
        print(False)
        return test_pair(math.ceil(int(input("Saisir un nombre"))))
