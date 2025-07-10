numbers = [2, 4, 5, 6, 2, 9, 4, 4, 6 ,6]
uniques = []

for i in numbers:
    if i not in uniques:
        uniques.append(i)
print(uniques)