listOfNumbers = [2, 3, 4, 22, 99, 4, 33, 7, -5, 4, 0, 28]
largestNumber = 0
for i in listOfNumbers:
    if i > largestNumber:
        largestNumber = i
print(f'Largest Number {largestNumber}')
