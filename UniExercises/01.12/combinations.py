from itertools import combinations

# Примерен списък
lst = [1, 2, 3]

# Списък, в който ще пазим всички подсписъци
all_sublists = []

# Генерираме подсписъците с различна дължина
for r in range(1, len(lst)+1):
    for combo in combinations(lst, r):
        all_sublists.append(list(combo))

print("Всички подсписъци:", all_sublists)
