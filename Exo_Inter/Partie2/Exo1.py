# Exercice 1

print(" Un échiquier ")

space_sharp = " #"
sharp_space = "# "

line = [1, 2, 3, 4, 5, 6, 7, 8]
nb = 8

i = 0
while i <= len(line):
    print(nb * space_sharp)
    print(nb * sharp_space)
    i += 2
