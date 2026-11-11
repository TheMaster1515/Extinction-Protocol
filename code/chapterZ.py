# chapterZ.py
import time
import chapterX
import character_data



class CharacterManager:
    def save_character_data(self, name, age, colony, filepath):
        character_data.update_character(filepath, Name=name, Age=age, Colony=colony)

    def prepare_existing_character(self, filepath):
        data = character_data.read_character(filepath)
        has_character = all(field in data for field in ("Name", "Age", "Colony"))
        data = character_data.prepare_character(data)
        character_data.update_character(filepath, **data)
        return has_character



def chapterz():
    character_manager = CharacterManager()

    character_name = ""
    character_age = 0
    character_colony = ""

    
    print("Welcome to Extinction Protocol!\n")
    print("Would you like to pick a level to start at or design your character.\n")
    while True:
        print("1. Start at a level")
        print("2. Design your character")
        choice = input("Choose an option (1 or 2): ").strip()
        if choice == "1":
            if not character_manager.prepare_existing_character("files/character.txt"):
                print("\nNo saved character found. Missing details will be Unknown and age will be 0.")
            chapterX.chapterx()
            return True
        if choice == "2":
            break
        print("\nInvalid option. Please enter 1 or 2.\n")

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
    character_manager.save_character_data(character_name, character_age, character_colony, "files/character.txt")

    # Move to next chapter
    chapterX.chapterx()

    return True

if __name__ == "__main__":
    chapterz()