import cv2
import time
import chapter5

def drawEasterEgg4():
    print("                  01010100 					")
    print("                  01101000 					")
    print("              01101001 01110011 				")
    print("              00100000 01101101 				")
    print("              01101001 01110011 				")
    print("         01110011 01101001 01101111 			")
    print("         01101110 00100000 01101001 			")
    print("     01110011 00100000 01110100 01101111 		")
    print("     01101111 00100000 01101001 01101101 		")
    print("01110000 01101111 01110010 01110100 01100001 	")
    print("01101110 01110100 00100000 01100110 01101111 	")
    print("01110010 00100000 01101101 01100101 00100000 	")
    print("     01110100 01101111 00100000 01100001		")
    print("     01101100 01101100 01101111 01110111		")
    print("     00100000 01111001 01101111 01110101 		")
    print("     00100000 01110100 01101111 00100000 		")
    print("         01101010 01100101 01101111			")
    print("         01110000 01100001 01110010			")
    print("              01100100 01101001				")
    print("              01111010 01100101				")
    print("              00100000 01101001				")
    print("                  01110100 					")
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
    def chapter4(self):
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

        imagePath = "images/Chapter_4.jpg"
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
        print("\n      *******			")
        print("\n\n\n\n\n\n\n\n")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nENTERING GRAVITY IN 5...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n\n\n\n\n\n ")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nENTERING GRAVITY IN 4...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print(" \n *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n\n\n\n\n\n")
        print("\n________________________________________________________________________________________________________________________")
        print("\nENTERING GRAVITY IN 3...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n*******************	")
        print(" *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n\n\n\n\n")
        print("\n________________________________________________________________________________________________________________________")
        print("\nENTERING GRAVITY IN 2...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n  ***************		")
        print(" *****************		")
        print("*******************	")
        print(" *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n")
        print("\n")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nENTERING GRAVITY IN 1...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n\n      *******			")
        print("   *************		")
        print("  ***************		")
        print(" *****************		")
        print("*******************	")
        print(" *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n________________________________________________________________________________________________________________________")
        input("\nPress Enter to continue... ")

        while True:
            print("\n\n\n\n**************************************************Chapter 4**************************************************")
            print(f"\nYou are leaving the Solar System now in your the {recalledShip}. You are just now finally getting the hang")
            print(f"\nof your job of being a {recalledJob}. There is an anoucement that comes over the speakers saying \"We will be")
            print("\nlanding soon. Please prepare.\" You wonder why you are landing? Why are you landing so soon? It seems like you")
            print("\njust left the solar system. What do you need to do to prepare for landing?")
            print(f"\n\t1.Ask your friend {recalledPerson}")
            print("\n\t2.Go to the bridge")
            print("\n\t3.Look out the window")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print(f"\nYou ask your friend {recalledPerson} what they think is going on? He replies with \"I think that we")
                print("\nare landing on a base that looks like it is a moon\"")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou get to the bridge to see what is going on. You look out the large window and see a moon! You notice")
                print("\nthat there is a base on that moon...")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou look out the window and you see a moon!! You notice a base on the moon that you are landing on.")
                input("\nPress Enter to continue...")
                break

        while True:
            print("\n\n\n\n**************************************************Chapter 4***************************************************")
            print(f"\nYou ask a higher ranking soldier what is going on? He tells you \"{recalledName} we are landing on")
            print("\na forward operating base of the Polarians.\" You finally land and are docked with the base. When you get on")
            print("\nthe base you realize that it is very simaliar to the base on Europa! You wonder why the Polarians would")
            print("\nhave a base that looks just like a base made by humans.")
            print("\n\t1.Go explore")
            print("\n\t2.Talk to a Polarian")
            print("\n\t3.Ask your Commander")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 4:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou go explore trying to see how big the base is. You find a hatch that looks like it takes you to the hangar.")
                print("\nYou open up the hatch and all the air rushes out!! You are vented into space!!")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou go find a Polarian that is willing to talk with you. You find one willing to talk and you are amazed!")
                print("\nThey look just like humans but they have ridges on their nose. The Polarian says \"This is our base that was")
                print("\nset up decades ago. We have been fighting the Tau Ceties for decades with the humans.\"")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou talk with your commander and he tells you \"The Polarians and humans have been fighting for decades")
                print("\nand the time has come to come out of hiding and have the whole world help us destroy the Tau Ceties")
                print("\nonce and for all!!!\"")
                input("\nPress Enter to continue...")
                break
            elif success == 4:
                drawEasterEgg4()
                print("You have just unlocked an Easter Egg!!!!")
                input("\n\nPress Enter to Continue...")


        while True:
            print("\n\n\n\n**************************************************Chapter 4***************************************************")
            print(f"\nYou are on the base when it comes under attack!! You race to find your ship. Finally you find {recalledShip}.")
            print("\nYou get on to your ship and take your station. The FTL drive starts to spin up. You take off and the stars start")
            print("\nto pass very quickly. Then before you know it you are back at sub light speed. Then a moon shows up out the")
            print("\nwindow. It is a Tau Ceti base! The base is on a moon with very large ships orbiting it. You wonder what you are")
            print("\ndoing here?")
            print("\n\t1.Attack the base")
            print("\n\t2.Spin up FTL drives")
            print("\n\t3.Regroup with the Polarians")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou are going to attack the base. You start by getting or orbit with the very large ships. You notice that the")
                print("\nships dont open fire. You wonder why? Just as you are thinking about it your ship opens fire!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou turn around to spin up your FTL drives to get out of there! While you are turning and spinning up your")
                print("\nFTL drives a drone comes in and opens fire! Your ship blows up!!")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou try to regroup with the Polarians. This means you need to get back to their base. So you try to do")
                print("\na slingshot around the moon. As you are speeding up and spinning up FTL drives you get to the far side of")
                print("\nmoon. Then a drone opens fire on your ship and you explode!")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n**************************************************Chapter 4***************************************************")
            print("\nYou are firing on the large ships in orbit. With an exchange of fire between all of the ships you finally are making")
            print("\nsome headway! You make one final push and destroy all the ships in orbit. You notice that the fight was a little")
            print("\nto easy. Durring the attack you loose a couple of your ships. Then the base finally comes into view. You lanch all")
            print("\nthe remaining warheads you have. The base blows up! You are now in orbit with the whole moon burning and the large")
            print("\nships are floating in space orbiting the moon.")
            print("\n\t1.Leave orbit")
            print("\n\t2.Land on planet")
            print("\n\t3.Remain in orbit")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou are in orbit and you decide to wait for everything to calm down before leaing orbit. While waiting a")
                print("\nrandom drone gets very close to you and fires on you! You take enemy fire and the weapon magazine blows up!")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou land on the planet and help everybody else that is rounding up the rest of the Tau Ceties. While")
                print("\na Tau Ceti is being interegated you over hear that there is another base just like this one on the way")
                print("\nto the Tau Ceti home world")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou stay in orbit while another ship lands on the moon to deal with the rest of the Tau Ceties. Your")
                print("\ncommander tells you that while they were interegating a Tau Ceti they said that there is another")
                print("\nbase just like this one on the way to the Tau Ceti homeworld")
                input("\nPress Enter to try again...")
                continue

        print(f"\n{recalledShip} is leaving orbit on their way to another Tau Ceti outpost. The fleet leaves orbit when")
        print("\na broadcast comes over saying \"Earth has just been attacked...\"")
        input("\nPress Enter to continue to Chapter 5....")
        chapter5.Game().chapter5()
        return True
if __name__ == "__main__":
    game = Game()
    game.chapter4()

