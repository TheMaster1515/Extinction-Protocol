import cv2
import time
import chapter6

def drawEasterEgg5():
    print("\n             01000101				")
    print("             01110110 				")
    print("         01100101 01101110 			")
    print("         00100000 01110100			")
    print("         01101000 01100101 			")
    print("    00100000 01110011 01101101 		")
    print("    01100001 01101100 01101100 		")
    print("01100101 01110011 01110100 00100000 ")
    print("01110000 01100101 01110010 01110011 ")
    print("01101111 01101110 00100000 01100011 ")
    print("01100001 01101110 00100000 01100011 ")
    print("01101000 01100001 01101110 01100111 ")
    print("01100101 00100000 01110100 01101000 ")
    print("01100101 00100000 01100011 01101111 ")
    print("01110101 01110010 01110011 01100101 ")
    print("00100000 01101111 01100110 00100000 ")
    print("    01110100 01101000 01100101		")
    print("    00100000 01100110 01110101		")
    print("         01110100 01110101			")
    print("             01110010				")
    print("             01100101 				")
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

    def chapter5(self):
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

        imagePath = "images/Chapter_5.jpg"
        image = cv2.imread(imagePath)
        if image is not None:
            window_name = "Chapter 5"
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
        print("\n\n      *******			")
        print("   *************		")
        print("  ***************		")
        print(" *****************		")
        print("*******************	")
        print(" *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nLEAVING GRAVITY IN 5...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n\n  ***************		")
        print(" *****************		")
        print("*******************	")
        print(" *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n")
        print("\n")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nLEAVING GRAVITY IN 4...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n\n*******************	")
        print(" *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n\n\n\n")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nLEAVING GRAVITY IN 3...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n \n *****************		")
        print("  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n\n\n\n\n")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nLEAVING GRAVITY IN 2...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n\n  ***************		")
        print("   *************		")
        print("      *******			")
        print("\n\n\n\n\n\n ")
        print("\n\n________________________________________________________________________________________________________________________")
        print("\nLEAVING GRAVITY IN 1...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n\n      			")
        print("\n\n\n\n\n\n\n\n")
        print("\n\n________________________________________________________________________________________________________________________")
        input("\nPress Enter to continue... ")

        while True:
            print("\n\n\n\n\n\n\n\n**************************************************Chapter 5***************************************************")
            print("\nYou are on your way to the next outpost of the Tau Ceti's and the earth just got attacked.")
            print("\nEarth got attacked by the Tau Ceti's. It wasnt a bad attack but it was a first strike.")
            print("\nOne mothership came into orbit and launched drones that went after colorado. Why colorado?")
            print("\nNORAD is there. Is ISA located there too? Your theory about the Tau Ceti's may not be true.")
            print("\nWhy would they attack Earth but not fire first when we attack them? An annoucment pops up and")
            print("\nsays \"The attack on Colorado was unsuccessful. NORAD and the ISA are still safe! Now we")
            print("\nare going to head to the next outpost.\"")
            print("\n\t1.Go to the next outpost")
            print("\n\t2.Call home")
            print("\n\t3.Talk with your friend")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 4:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print(f"\nYou are on your way to the next outpost while you think about what just happened on earth.")
                print(f"\nYou know that your family is safe but you are still worried. They are from {recalledColony} colony and you")
                print("\nknow that is far from the attack on Colorado.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou call home to check on your family. There is no answer. You know that they have to be safe")
                print(f"\nbut you still worry. You call a old friend from your colony {recalledColony} and ask how your family is doing?")
                print("\nHe says that your family was on vacation in colorado when the attack happened. They are all")
                print("\ngone.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou go talk with your friend. He is just as worried about his family as you are about your")
                print("\nfamily. He thinks about trying to call but you tell him that we need to focus on the mission.")
                print("\nWe have to be strong if we want to save the world!")
                input("\nPress Enter to continue...")
                break
            elif success == 4:
                drawEasterEgg5()
                print("You have just unlocked an Easter Egg!!!!")
                input("\n\nPress Enter to Continue...")

        while True:
            print("\n\n\n\n**************************************************Chapter 5***************************************************")
            print(f"\nYou are on the {recalledShip} on your way to the next outpost. Your thoughts are with your friends and family")
            print("\nthat are back on earth. Your ship is at 24x the speed of light when all the sudden there is an")
            print("\nannoucment \"We are dropping out of FTL\" The ship then slows down very abruptly. You look out the window")
            print("\nto see what is going on. You see a moon coming into view very fast! You wonder what is going on? You ask")
            print(f"\nyour friend what is going on? He says \"We are testing a brand new drone from the Polarians before we")
            print("\nget to the Tau Ceti outpost\"")
            print("\n\t1.Fly drone")
            print("\n\t2.Go watch the drone test")
            print("\n\t3.Continue with your duties")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou go to the hangar to test the new drone. You get to the hangar and there is a weird pod sitting")
                print("\nnext to a very high tech looking drone. There are crowds of people forming around the command")
                print("\nstation. You go to a polarian and ask \"Can I test the new drone?\" He replies with \"Are")
                print(f"\nyou certified to fly drones?\" You show him your pilots license and he notices your name.")
                print(f"\nHe says \"Are you {recalledName}?\" You nod your head and for some reason he lets you")
                print("\npilot the drone.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou are very excited about the new drone so you go to the hangar to watch the launch. In the hangar")
                print("\nthere is a weird pod sitting there with a very high tech looking drone next to it. You go over to")
                print("\nthe command center and notice a lot of polarians. More than usual. You go talk to one of them. ")
                print("\n\"I see you guys are testing the new drone. Can you tell me more about it?\" He replies with \"What is")
                print("\nyour clearance level?\" You show him your ID and he says \"Sorry your arent cleared for this.\"")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nThe new drone doesnt excite you very much so you just continue with your normal duties. You go")
                print("\nto the gym to work out, go get your breakfast, and then you start your day. As you are going about")
                print("\nyour day when all the sudden you hear an explosion outside of the ship! You look out the window ")
                print("\nand the new drone just blew up!")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n**************************************************Chapter 5***************************************************")
            print("\nThe drone flies out of the hangar very fast and supprisingly silent. There is a star outside with multiple planets")
            print("\norbiting. The drone flies to the closest planet. It is a rocky body that is about the size of earth. You are ")
            print("\namazed! You wonder if this planet is here then maybe the whole universe is full of life! The drone makes a")
            print("\nclose pass to the planet going very fast! There is red targets that show up on the HUD. The drone then")
            print("\nfires two missles at the planet then flies off very fast! Two explosions went off on the planet! Massive explosions")
            print("\ngo off and you wonder what kind of weaponary that Polarians have. You get back to the ship and hear over the intercom")
            print("\n\"Make ready for FTL\" ")
            print("\n\t1.Get ready for FTL")
            print("\n\t2.Go back to your bunk")
            print("\n\t3.Go to the bridge")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou help the ship get ready for FTL and shoot off into space at 24x the speed of light! You go into the engine room ")
                print("\nand they are all franticly moving around. You ask \"What can I do to help?\" You get a reply \"Get out of here\"")
                print(f"\nYou leave the engine room but as the ship spools the FTL drives an explosion happens. {recalledShip} blows up!")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou go back to your bunk. You are making your way to your room when you get stopped by a crew member and he says")
                print("\n\"Make ready for FTL!!\" You run to the engine room when an explosion goes off! " + recalledShip + " blows up!")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou make your way to the bridge. One of the crew yells \"RUN!!!\" So you run to the brige as fast as you can!")
                print("\nYou get to the brige and everybody is preparing for FTL. You get to your station and notice an odd fluctiation")
                print("\nin the power. You raise this concern with the Captian. He finds this very curious so he halts spooling up")
                print("\nthe FTL drives.")
                input("\nPress Enter to continue...")
                break

        while True:
            print("\n\n\n\n**************************************************Chapter 5***************************************************")
            print(f"\n{recalledShip} drops out of FTL and the captian says \"There may be a sabature on the ship...\"")
            print("\nYou look out the window to see a large moon. On the moon you see that it looks almost")
            print("\nexactly like the last base you attacked. There is a few large ships in orbit and a large")
            print("\npresence on the moon. You see a polarians ship drop out of FTL right next to you! You look at the ship")
            print(f"\nand it looks to be the same size as {recalledShip}. The side reads Delta Flyer. You take your station and make ready ")
            print("\nto fight the Tau Ceties on this last outpost. You realize this could be the last big battle before their")
            print("\nspecies is wiped out.")
            print("\n\t1.Group up with The Delta Flyer")
            print("\n\t2.Plan an attack ")
            print("\n\t3.Go to the drone hanger")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou decide to group up with The Delta Flyer. You bring your ship in formation with the Flyer and assume an")
                print("\nattack posture. You go over the coms and say \"Lets go after the big ships in orbit first.\" You both")
                print(f"\ngo after the ships in orbit. {recalledShip} accelerates very fast! You get the first ship in your")
                print("\nsights. The Flyer is matching your speed and going after a simalar ship.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou plan an attack with The Flyer. They want to attack the dark side of the moon first. You want to ")
                print("\nattack the ships in orbit first. You are now in a very long discussion on how to proceed. After")
                print("\nall the talking finally you come to an agreement. Just as everybody comes to an agreement you see")
                print("\nthat The Delta Flyer is taking fire!! Then it blows up! The shockwave shakes " + recalledShip + " and")
                print("\nthen your ship blows up.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou go to the drone hangar to pilot a drone and take care of The Tau Ceties yourself. You get there")
                print("\nand you see the new Polarian drone sitting alone in the hangar. You decide to pilot it. You get in")
                print("\nand power it up. The drone is powered up and ready to go. You pilot it out of the hangar and go ")
                print("\nto the moon to fight! Just as you are leaving the The Delta Flyer explodes! Then " + recalledShip + " explodes!")
                print("\nYou are left alone in the cold of space.")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n**************************************************Chapter 5***************************************************")
            print(f"\n{recalledShip} and The Flyer are heading to the moon to attack the orbiting ships. You are pointing the")
            print("\nship strait at the biggest carrier in orbit. The Flyer takes aim at the carrier right next to it! You ")
            print(f"\nboth fire at the same time taking straffing runs at the ships. The Flyer is doing an amazing amount")
            print(f"\nof damage to their ship. The ship {recalledShip} was firing on explodes!! This sets off a huge expolsion that")
            print("\nengulfs the ship you are targeting. Finally both of the ships explode with a huge shockwave heading to")
            print("\nyour ship.")
            print("\n\t1.Run from the shockwave")
            print("\n\t2.Hide on the far side of the moon")
            print("\n\t3.Target another ship")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print(f"\nYou attempt to run from the shockwave but the ship explodes faster than you expected.{recalledShip} and The Flyer")
                print("\nset a course for the sun away from the moon base. The shockwave is heading to your ")
                print(f"\nship and just as it is right behind you {recalledShip} and The Flyer give one more push to the engines. You")
                print("\nclear the shockwave!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou have the idea of hiding from the shockwave on the opposite side of the moon. You call over to ")
                print("\nThe Flyer and tell the Polarians \"Get to the other side of the moon as fast as possible!!!\"")
                print("\nThe ships explode with a huge flash! You push the engines as hard as you can and just as you ")
                print("\nmake it to the other side of the moon the shockwave blasts on all sides of the moon but misses")
                print("\nyour ship.")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou spot a smaller ship in orbit that is an easy target! You go after it alone with out The Flyer.")
                print("\nYou ignite the engines and power up your weapons. When you come into view you notice something")
                print("\nleave this small ship and find out its a drone! The drone comes after you and launches missles. ")
                print("\nOne missle hits your ship and you explode.")
                input("\nPress Enter to try again...")
                continue

        print("\n\n\n\n**************************************************Chapter 5***************************************************")
        print("\nYou have just blown up two huge ships and cleared the blast. You make your way back to the moon to see")
        print("\nwhat is left of the Tau Ceties. You notice that the explosions caused more damage to the base on the moon.")
        print("\nThe base appears to be one fire. You realize that the two exploding ships in orbit have blown up the base")
        print("\nas well. You now have one more target. Their home base...")
        input("\nPress Enter to continue to Chapter 6....")
        chapter6.Game().chapter6()
        return True

if __name__ == "__main__":
    game = Game()
    game.chapter5()

