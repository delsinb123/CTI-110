# Delsin Barrett
# 10/7/2024
# P5LAB
# Create a game using AI

import random

def create_character():
    """Create a character and return its attributes in a dictionary."""
    name = input("Enter the character's name: ")
    health = int(input("Enter the character's health (e.g., 100): "))
    attack_points = int(input("Enter the character's attack points (e.g., 10): "))
    
    character = {
        'name': name,
        'health': health,
        'attack_points': attack_points
    }
    
    return character

def display_characters(character_list):
    """Display the attributes of all characters in the provided list."""
    if not character_list:
        print("No characters created yet.")
        return
    
    for character in character_list:
        print("Character Details:")
        for key, value in character.items():
            print(f"{key}: {value}")
        print()

def battle(character1, character2):
    """Simulate a battle between two characters."""
    print(f"{character1['name']} attacks {character2['name']}!")
    damage = random.randint(1, character1['attack_points'])
    character2['health'] -= damage
    
    print(f"{character1['name']} deals {damage} damage to {character2['name']}.")
    print(f"{character2['name']}'s health is now {character2['health']}.")
    
    if character2['health'] <= 0:
        print(f"{character2['name']} has been defeated!")

def main():
    characters = []
    
    while True:
        print("Choose an action:")
        print("1. Create a character")
        print("2. Display all characters")
        print("3. Battle characters")
        print("4. Exit game")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            character = create_character()
            characters.append(character)
        
        elif choice == '2':
            display_characters(characters)
        
        elif choice == '3':
            if len(characters) < 2:
                print("You need at least two characters to battle.")
            else:
                print("Choose the first character:")
                for i, char in enumerate(characters):
                    print(f"{i}: {char['name']}")
                char1_index = int(input("Enter index for the first character: "))
                
                print("Choose the second character:")
                for i, char in enumerate(characters):
                    print(f"{i}: {char['name']}")
                char2_index = int(input("Enter index for the second character: "))
                
                if char1_index != char2_index:
                    battle(characters[char1_index], characters[char2_index])
                else:
                    print("You cannot battle the same character!")
        
        elif choice == '4':
            print("Exiting game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

# Prompts for user input (to be included in a separate text file):
"""
1. Enter the character's name.
2. Enter the character's health (e.g., 100).
3. Enter the character's attack points (e.g., 10).
4. Choose an action:
   1. Create a character
   2. Display all characters
   3. Battle characters
   4. Exit game
5. Enter index for the first character.
6. Enter index for the second character.
"""
