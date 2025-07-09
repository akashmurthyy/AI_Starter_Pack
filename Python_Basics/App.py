
while True:
    user_input = input('>').upper()
    if user_input == 'HELP':
        print("""Start - to start the car
        Stop - to stop the car
        quit - to exit""")
    elif user_input == "START":
        print("Car has started")
    elif user_input == "STOP":
        print("Car has stopped")
    elif user_input == "QUIT":
        break
    else:
        print("I don't understand that")