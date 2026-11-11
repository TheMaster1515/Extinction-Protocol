# chapterZ.py
import os
import time
import chapterX



class CharacterManager:
    def save_character_data(self, name, age, colony, filepath):
        # Ensure the folder exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, "w") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Age: {age}\n")
            f.write(f"Colony: {colony}\n")



def chapterz():
    character_manager = CharacterManager()

    character_name = ""
    character_age = 0
    character_colony = ""

    
    print("Welcome to the Text-Based Game!\n")
    print("This will be where you design your character. Choose the following:\n")

    # Character name input
    while True:
        character_name = input("Enter your character's name: ")
        if not character_name.strip():
            print("\n\tNothing entered. Please enter some text.\n")
            continue
        break

    # Character age input
    while True:
        age_input = input("Enter your character's age: ")
        if not age_input.isdigit():
            print("\n\tInvalid age. Please enter a number between 1 and 150.\n")
            continue
        character_age = int(age_input)
        if character_age < 1 or character_age > 150:
            print("\n\tInvalid age. Please enter a number between 1 and 150.\n")
            continue
        break

    # Character colony input
    while True:
        print("Enter your character's colony:")
        print("\tAmerica")
        print("\tChina")
        print("\tRussia")
        print("\tAntartica")
        character_colony = input()
        if not character_colony.strip():
            print("\n\tNothing entered. Please enter some text.\n")
            continue
        break

    print("\nPress Enter to continue...")
    input()

    # Save character data
    character_manager.save_character_data(character_name, character_age, character_colony, "files/data.txt")

    # Move to next chapter
    chapterX.chapterx()

    return True

if __name__ == "__main__":
    chapterz()