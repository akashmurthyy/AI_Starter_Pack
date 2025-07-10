try:
    denominator = int(input("Enter the denominator "))
    fraction = 20 / denominator
    print(f'Fraction {fraction}')
except ValueError:
    print('Enter valid number')
except ZeroDivisionError:
    print("Denominator cannot be 0")