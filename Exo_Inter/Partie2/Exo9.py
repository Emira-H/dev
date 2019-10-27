# Exercice 9

print("Exercice 9: Une to do List")

task = input("Saisir une tâche ")

task_list = []

while task != "fin":
    task_list.append(task)
    task = input("Saisir une tâche ")
print(task_list)
