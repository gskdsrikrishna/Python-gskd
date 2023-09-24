#Text-Basec Adventure Games
def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You wake up in a mysterious room. Your goal is to find the treasure and escape.")
    print("Be careful, danger lurks around every corner!")

    while True:
        print("\nWhat do you want to do?")
        print("1. Open the door")
        print("2. Look under the bed")
        print("3. Search the desk")
        print("4. Quit the game")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            explore_room()
        elif choice == '2':
            print("You find nothing under the bed. Keep looking!")
        elif choice == '3':
            print("You search the desk and find a key. It might be useful!")
        elif choice == '4':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def explore_room():
    print("You open the door and enter the next room.")
    print("In front of you, there are two paths.")
    print("Choose your path wisely!")

    while True:
        print("\nWhich path do you choose?")
        print("1. The dark corridor")
        print("2. The secret tunnel")
        print("3. Go back to the previous room")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("You enter the dark corridor...")
            encounter_enemy()
        elif choice == '2':
            print("You take the secret tunnel...")
            find_treasure()
        elif choice == '3':
            print("You go back to the previous room.")
            break
        else:
            print("Invalid choice. Please try again.")

def encounter_enemy():
    print("As you walk through the dark corridor, a fierce enemy appears!")
    print("Prepare yourself for a battle.")

    # Implement your own battle mechanics here

    print("You defeated the enemy and continue your journey.")

def find_treasure():
    print("You enter the secret tunnel and discover a hidden treasure!")
    print("Congratulations! You have successfully completed the game.")

start_game()