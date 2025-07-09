started = False
while True:
    user_input = input('>').upper()
    if user_input == 'HELP':
        print("""Start - to start the car
        Stop - to stop the car
        quit - to exit""")
    elif user_input == "START":
        if started:
            print("Car has already started")
        else:
           print("Car has started")
           started = True
    elif user_input == "STOP":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car has stopped")
    elif user_input == "QUIT":
        break
    else:
        print("I don't understand that")