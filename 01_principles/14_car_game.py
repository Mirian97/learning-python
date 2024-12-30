command = ''
started = False

while True:
    command = input("> ").lower()
    
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
            ''')
        
    elif command == 'start':
        if started:
            print("The car is already started!")
        else:
            started = True
            print('Car started... Ready to go!')
        
    elif command == 'stop':
        if not started:
            print("The car is already stopped!")
        else:
            started = False
            print('Car stopped.')
        
    elif command == 'quit':
        break
    
    else:
        print(f"I don't understand {command}...")