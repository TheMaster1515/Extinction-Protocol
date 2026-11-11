import cv2
import time
import chapter4

def drawEasterEgg3():
    print("\n             01010010 				\n")
    print("        01101111 01100001 				\n")
    print("        01100100 01110011 				\n")
    print("    00111111 00100000 01010111 		\n")
    print("    01101000 01100101 01110010 		\n")
    print("01100101 00100000 01110111 01100101 	\n")
    print("01110010 01100101 00100000 01100111 	\n")
    print("01101111 01101001 01101110 01100111 	\n")
    print("00100000 01110111 01100101 00100000 	\n")
    print("    01100100 01101111 01101110 		\n")
    print("    01110100 00100000 01101110 		\n")
    print("    01100101 01100101 01100100 		\n")
    print("        00100000 01110010 				\n")
    print("        01101111 01100001 				\n")
    print("        01100100 01110011 				\n")
    print("\nHINT: Binary Unlocks A Secret!!")

class Game:
    def recallCharacterData(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                name = lines[0].split(": ")[1].strip()
                age = int(lines[1].split(": ")[1].strip())
                colony = lines[2].split(": ")[1].strip()
            return name, age, colony
        except (FileNotFoundError, IndexError, ValueError):
            return "Unknown", 0, "Unknown"

    def recallCharacterWork(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                person = lines[0].split(": ")[1].strip()
                ship = lines[1].split(": ")[1].strip()
            return person, ship
        except (FileNotFoundError, IndexError):
            return "Unknown", "Unknown"

    def recallCharacterJob(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                job = lines[0].split(": ")[1].strip()
            return job
        except (FileNotFoundError, IndexError):
            return "Unknown"

    def chapter3(self):
        recalledName, recalledAge, recalledColony = self.recallCharacterData("files/data.txt")
        recalledPerson, recalledShip = self.recallCharacterWork("files/character.txt")
        recalledJob = self.recallCharacterJob("files/job.txt")
        print("Here is your character's information")
        print(f"Name: {recalledName}")
        print(f"Age: {recalledAge}")
        print(f"Colony: {recalledColony}")
        print(f"Job: {recalledJob}")
        print(f"Friend: {recalledPerson}")
        print(f"Ship: {recalledShip}")
        input("\nPress Enter To Continue...")
        imagePath = "images/Chapter_3.jpg"
        image = cv2.imread(imagePath)
        if image is not None:
            window_name = "Chapter 2"
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.imshow(window_name, image)
            # Request topmost/focus so the window is not hidden behind terminal.
            try:
                cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
            except Exception:
                pass
            cv2.waitKey(50)
            start_time = time.time()
            while True:
                if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                    break
                current_time = time.time()
                elapsed_seconds = current_time - start_time
                if elapsed_seconds > 5.0:
                    break
                key = cv2.waitKey(1)
                if key != -1 or key == 27:
                    break
            cv2.destroyAllWindows()
        else:
            print("Error: Could not open or find the image.")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n    	    / \\")
        print("\n    	   / _ \\")
        print("\n    	  | / \\ |")
        print("\n         _|_____|_")
        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLIFT OFF IN 5...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n    	   / _ \\")
        print("\n    	  | / \\ |")
        print("\n         _|_____|_")
        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLIFT OFF IN 4...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n    	  | / \\ |")
        print("\n         _|_____|_")
        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n        ****   ****")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLIFT OFF IN 3...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n         _|_____|_")
        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n        ****   ****")
        print("\n        ****   ****")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLIFT OFF IN 2...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n        ****   ****")
        print("\n        ****   ****")
        print("\n       ****** ******")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLIFT OFF IN 1...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n        ****   ****")
        print("\n        ****   ****")
        print("\n       ****** ******")
        print("\n     *****************")
        print("\n________________________________________________________________________________________________________________________")
        input("\nPress Enter to continue... ")
        print("\n\n\n\n**************************************************Chapter 3**************************************************")
        print(f"\nYou have arrived at your ship {recalledShip}. Once you get to your ship there is a broadcast over all channels.")
        print("\nYou see the leader of the ISA on the screen talking in a press conference. He says \"Hello new recruits! Welcome to")
        print("\nthe ISA. You guys probably are wondering what is going on? This all seemed very rushed and last minute but, here")
        print("\nis an explination. The ISA has been around since the Apollo missions and its sole purpose is to save the world in")
        print("\nthe event that there is an alien invasion and you guessed it, there is an alien invasion. The Polarians have come")
        print("\nfrom the future to warn us about an impendeing invasion. The Tau Ceties are going to come to earth in the near future")
        print("\nto destroy the world. We must stop them!! We have all sorts of tech that is more advanced than anything you have seen.")
        print("\nWe have faster than light drives FTL for short, quantum computers, energy beams, artificial gravity, and much more!")
        print("\nWe have got a lot more designs from The Polarians to put into production. Our plan is daring! We are going to take it")
        print("\nstraight to the enemy home world! We will travel at 24x the speed of light to make the 12 light year journey in 6 months")
        print("\nNow what would you like to do?\"")
        while True:
            print("\n\t1.Go on this journey")
            print("\n\t2.Go home")
            print("\n\t3.Find another ship")
            try:
                success = int(input("\nChoose an option (1, 2, 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, 3")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success < 1 or success > 4:
                print("\n\tInvalid option. Please enter 1, 2, 3")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print("\nYou chose to start the long journey to The Tau Ceties's home world. Stopping by every single forward operating base")
                print("\nthat they have and destroying them!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print(f"\nYou chose to go home. You try to find an escape ship in your ship {recalledShip} . But you are having a hard")
                print("\ntime finding an escape ship. While looking around a soldier spots you and asks what your doing. You tell him and he")
                print("\nthrows you in the brig.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou choose to try and find another ship. You talk with your commander but he says that this is the ship you were assigned")
                print("\nand you can not switch. He questions your loyalty and throws you in the brig for deserting.")
                input("\nPress Enter to try again...")
                continue
            elif success == 4:
                drawEasterEgg3()
                print("You have just unlocked an Easter Egg!!!!")
                
                input("\n\nPress Enter to Continue...")
        while True:
            print("\n\n\n\n**************************************************Chapter 3***************************************************")
            print("\nYou have started your journey to Tau Ceti to destroy the Tau Ceit's but on your way you have to stop and get fuel. They")
            print("\nmake an announcement \"Prepare for landing\" You are wondering where you are landing!! You look out the window and see a")
            print("\nmoon like object covered in ice but you see this small base that has the words ISA on it. You ask your friend")
            print(f"\nwhere are we? {recalledPerson} says \"We are on Europa!!!\" What do you want to do?")
            print("\n\t1.Land on Europa")
            print("\n\t2.Check for enemy")
            print("\n\t3.Try to assist with the landing")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print(f"\nYou chose to land on Europa. You land on Europa safetly and exit your ship {recalledShip} and go out")
                print("\nto the base on Europa. The base is very large and there are other ships that landed there to refuel. You go inside")
                print("\nthe base's hanger and see that the hanger is full of drones! You wonder why they have so many drones on")
                print("\nEuropa.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou check for enemy and see a fighter circling the base. You go to the bridge and let them know. The captian")
                print("\nyells \"SET CONDITION RED!!!!\" You go after the enemy fighter and they resemble something from Battlestar")
                print("\nGalactia. The enemy banks turning to the ship and fires!! The ship blows up and you die.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print(f"\nYou chose to try and help land the ship. You go up to the bridge and request to help landing. A soldier")
                print(f"\nsays \"Your job is {recalledJob} so take your station!\" You take your station and try to help.")
                print("\nWhen you are trying to land the ship starts falling very fast!! You ask what you should do? Nobody")
                print("\nanswers. The ship crashes in the base and blows up.")
                input("\nPress Enter to try again...")
                continue
        while True:
            print("\n\n\n\n**************************************************Chapter 3***************************************************")
            print(f"\nYou are in the hanger and you ask your friend \"Hey {recalledPerson} why do they have so many drones?\" He")
            print("\nreplies with \"They have been preparing for a battle like this for decades!\" You realize that this war just got")
            print("\nvery real. You get a little scared knowing if you fail the world with be destroyed. Now what do you want to do?")
            print("\n\t1.See if you can stay on Europa")
            print("\n\t2.Try to hide on a ship back to earth")
            print("\n\t3.Continue with mission")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print(f"\nYou try to see if you can stay on Europa. You ask a the captian \"Can I just stay on Europa?\" He states")
                print(f"\n{recalledName} you want to stay here? You have to join us in the battle or we may not win! If you stay here")
                print("\nthe world may be destoyed\" One year passes on Europa and the Tau Ceties show up! They go strait for Earth. You")
                print("\nwatch a video feed of the world being destroyed!! You deeply regret staying on Europa.")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou try to hide on a ship that is going back to Earth. You end up getting on a ship and making your way")
                print("\nback to Earth. Mid flight they realize that you should have been going to Tau Ceti. They label you as")
                print("\na deserter and you are court martialed.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou choose to continue with the mission. You guys finish up refueling and take off of Europa fully")
                print("\nstocked and ready to go! Now you are on your way to Tau Ceti!!")
                input("\nPress Enter to continue...")
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 3***************************************************")
            print(f"\nYou and {recalledPerson} are on your ship {recalledShip} and you guys are starting to get a routine")
            print("\ndown. You get up in the morning and excerise, get ready for the day, get breakfast, and then start your shift for the")
            print("\nday. When you get done you usually spend time gaming and making new games. You look out your window and see the Oort")
            print("\nCloud!! You realize that you are the farthest person ever to go this far from Earth. What should you do?")
            print("\n\t1.Stop and explore")
            print("\n\t2.Continue with the mission")
            print("\n\t3.Find a ship fully stocked with drones and fight alone")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print("\nYou stop and explore the Oort Cloud. Nobody has ever seen this before! As you explore you see an object out")
                print("\nthere. You scan it and realize that you just found an object bigger than Pluto! You wonder what else")
                print("\ncould be out there!")
                input("\nPress Enter to continue...")
                continue
            elif success == 2:
                print("\nYou continue with your mission and make the ship ready for 24x the speed of light!! As the view gets darker")
                print("\nyou see a bright light forming outside and then the starts started to move really fast!! You realize that you")
                print("\njust broke light speed!")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou try to take a ship and go alone. You go to the hanger and find a mid size ship that is full fuel and full")
                print("\nof drones!! You jump in the ship and take it out of the ship alone. You speed off and then engage the")
                print("\nFTL. You see a bright light and then you suddenly explode!!")
                input("\nPress Enter to try again...")
                continue
            print("\n\n\n\n**************************************************Chapter 3***************************************************")
            print("\nYou leave the solar system at 24x the speed of light! As you leave you reflect on your life and realize")
            print("\nyou may not come back from this. You remind yourself that you need to stay strong to help the world.")
            print("\nPress Enter to continue to Chapter 4...")
            input()

    
        chapter4.Game().chapter4()
        return True

if __name__ == "__main__":
    game = Game()
    game.chapter3()
