import cv2
import time
import chapter7

def drawEasterEgg6():
    print("\n             01001001 				")
    print("             01101101 				")
    print("         00100000 01110011 			")
    print("         01101111 01110010 			")
    print("    01110010 01111001 00100000 		")
    print("    01000100 01100001 01110110 		")
    print("01100101 00100000 01001001 01101101 ")
    print("00100000 01100001 01100110 01110010 ")
    print("01100001 01101001 01100100 00100000 ")
    print("    01001001 00100000 01100011 		")
    print("    01100001 01101110 01110100 		")
    print("    00100000 01100100 01101111 		")
    print("         00100000 01110100 			")
    print("         01101000 01100001 			")
    print("             01110100 				")
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
    def chapter6(self):
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

        imagePath = "images/Chapter_6.jpg"
        image = cv2.imread(imagePath)
        if image is not None:
            window_name = "Chapter 6"
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
        print("               _-o#&&*''''?d:>b\\_")
        print("          _o/`''  '', , dMF9MMMMMHo_")
        print("       .o&#'        `MbHMMMMMMMMMMMHo.")
        print("     .o\"\" '         vodM*$&&HMMMMMMMMMM?.")
        print("    ,'              $M&ood,~'`(&##MMMMMMH")
        print("   /               ,MMMMMMM#b?#bobMMMMHMMML")
        print("  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk")
        print(" ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L")
        print("|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,")
        print("$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?")
        print("]MMH#             \"\"*\"\"\"\"*#MMMMMMMMMMMMM'    -")
        print("MMMMMb_                   |MMMMMMMMMMMP'     :")
        print("HMMMMMMMHo                 `MMMMMMMMMT       .")
        print("?MMMMMMMMP                  9MMMMMMMM}       -")
        print("-?MMMMMMM                  |MMMMMMMMM?,d-    '")
        print(" :|MMMMMM-                 `MMMMMMMT .M|.   :")
        print("  .9MMM[                    &MMMMM*' `'    .")
        print("   :9MMk                    `MMM# - ")
        print("     &M}                     `          .-")
        print("      `&.                             .")
        print("        `~,   .                     ./")
        print("            . _                  .-")
        print("              '`--._,dd###pp=\"\"'")
        print("________________________________________________________________________________________________________________________")
        input("\n\n\nPress Enter to continue... ")

        while True:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 6**************************************************")
            print("\nYou just destroyed the second tau ceti outpostand you are ready for this trip to be over with")
            print("\nand back at home.You fly by the moon's base to inspect and make sure all targets are destroied.")
            print("\nWhen you pass by you look out the window and see the whole moon on fire!!The Polarians land")
            print("\non the moon base and radio over to " + recalledShip + " stating \"It appears they got a transmition out ")
            print("\nbefore being destroyed.\"")
            print("\n\t1.Inspect transmission")
            print("\n\t2.Continue with mission")
            print("\n\t3.Phone home")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou inspect the transmission and you find out it was sent back to Earth.You wonder why they")
                print("\nwould be communicating with earth ? So you ask the Polarian to play the transmission to you.")
                print("\nThe transmission says \"The final base has fallen...attack\" Attack??? What do they mean")
                print("\nattack. You phone home.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou choose to ignore the transmission and continue with the mission.You go back to your post")
                print("\nand you are making a course for the Tau Ceti homeworld when an alarm goes off!A missle hits")
                print("\n" + recalledShip + "and blows up!")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou get worriedand want to phone home.You go to the brige to make the call when you hear")
                print("\neverybody talking.You ask what is going on. \"Earth was just attacked\" The transmmision that")
                print("\nwas sent said \"The final base has fallen...attack\"")
                input("\nPress Enter to continue...")
                break

        while True:
            print("\n\n\n\n**************************************************Chapter 6***************************************************")
            print("\nYou are still wondering what that meant \"The Final Base Has Fallen\" you quickly phone home. When you try to phone")
            print("\nhome there is no answer it doesnt even ring. You ask if anybody has heard from earth? Nobody answers... You go to the")
            print("\nCaptian and ask him what is going on? He replies with \"We are in comms black out. After that transmision was sent")
            print("\nthere was another sent from this ship. It was warning the Tau Ceti homeworld we were coming. We have to find out")
            print("\nwho sent that transmision before we find out what is going on at home.\"")
            print("\n\t1.Work to find out who sent the transmision")
            print("\n\t2.Go talk with your friend")
            print("\n\t3.Help the Captian")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou try to find out who sent that transmision by scanning for the I.P. address that sent that message. You are")
                print("\nat the bridge when your station alerts you. You have found the I.P. address but it is hidden you cant view it.")
                print("\nIt needs clearance above yours so you ask the captian if he can help. He says thank you for your hard work")
                print("\nwe will take it from here.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou go look for " + recalledPerson + ". You find them in enginering working on some things. You ask him")
                print("\nif he heard what is going on? He says \"I have heard and it is above your paygrade. Let the Captian deal")
                print("\nwith it.\"")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou help the Captian to find out who sent that transmission. You start by scanning the outgoing I.P. addresses.")
                print("\nYou are scanning when all the sudden your computer alarms you that it has found the I.P. address. You look at")
                print("\nit but you cant read the I.P. address. You ask the Captian what is going on and he says \"Thank you for your")
                print("\nhard work. We will take it from here.\"")
                input("\nPress Enter to continue...")
                break

        while True:
            print("\n\n\n\n**************************************************Chapter 6***************************************************")
            print("\nWhy did they just say they will take it from here? They must know who sent that transmission but want to keep it")
            print("\nclassified. There is not much you can do about it right now except put it out of your mind. Your focus shifts to")
            print("\nEarth. Now that the traitor has been located the ship now will let you communicate outside of the ship. You call")
            print("\nback home and it finally rings this time! Somebody answers! All you hear is \"Earth is ours...\" Who was that?")
            print("\nThat was not your family and what do they mean Earth is ours? You tell everybody on the brige what happened and")
            print("\nthey respond by pointing at the view screen. On the screen there is a video of a Tau Ceti ship entering Earth's")
            print("\natmosphere. ")
            print("\n\t1.Go ask your friend what to do")
            print("\n\t2.Continue with mission")
            print("\n\t3.Ask the Captian if we are going home")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou go find " + recalledPerson + " and ask them what to do? You find them and ask them \"What should")
                print("\nwe do?\" He says \"We can only do one thing and that is continue the mission\"")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou decide to continue with the mission there is nothing you can do about Earth, you are very")
                print("\nfar away. You remind yourself why you are doing this. You need to defeat the Tau Ceties before")
                print("\nthey destroy Earth and the only way to do that is to destroy their home world!")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou ask the Captian if we are going to return home. He says \"No we can not go home now. That")
                print("\nwould be admiting defeat and the enemy would not stop untill we are all dead!\"")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n**************************************************Chapter 6***************************************************")
            print("\nYou have made up your mind. You are continueing on with the mission but your focus goes back on earth. You hear")
            print("\nsomebody talking about what happened on earth and you ask what happened. He says \"The Tau Ceties planned a first")
            print("\nstrike against Earth before their main fleat arrives. This must mean the main fleet must be close to Earth. They")
            print("\nentered the solar system when they were detected by the Europa base. Europa base launched their drones when")
            print("\nthe Tau Ceti's arrived. Europa put up a good fight but the Tau Ceti's wiped out the base. The moon was left on")
            print("\nfire and exploding ships orbiitting the small moon. They didn't stop there they made it all the way to Earth when")
            print("\nthey launched an attack on " + recalledColony + ". They only had one ship left after fighting the Europa base.")
            print("\nThe one ship got into orbit and launched missles and drones on the colony. The military and ISA responded by")
            print("\nlaunching Nuclear Weapons on the ship in orbit. When they did the ship exploded with a bright flash in the sky.")
            print("\nWhen the ship in orbit exploded all the drones fell from the sky. We still do not have a full account of everything")
            print("\nbut what we do know is that this was a devistating attack on Earth. If the main fleet of the Tau Cetie's are allowed")
            print("\nto reach Earth we may not have a home to go back to.\"")
            print("\n\t1.Continue with mission")
            print("\n\t2.Go back to bunk")
            print("\n\t3.Try calling home again")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 4:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou continue with the mission by getting back to your duties and making the ship ready to just to FTL for")
                print("\nthe final fight with the Tau Ceties. You are back into your routine getting all our tasks done. Then you hear")
                print("\n\"Make ready for FTL.\"")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nWhen you heard that news you needed a minute to yourself so you decide to go back to your bunk. When you")
                print("\nget there you fall into a deep depression. You cant stop thinking about what might have happned at home.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou try to call home one last time. It rings! You get no answer though only a voicemail. You dont")
                print("\nknow what to do next.")
                input("\nPress Enter to try again...")
                continue
            elif success == 4:
                drawEasterEgg6()
                print("You have just unlocked an Easter Egg!!!!")
                input("\n\nPress Enter to Continue...")
        while True:
            print("\n\n\n\n**************************************************Chapter 6***************************************************")
            print("\nThe ship jumps to FTL. You are now on your way to the final base of the Tau Ceti's. This makes you a little nervous.")
            print("\nIf this doesnt work then the human race will cease to exsist. You get back to your bunk and think about your ")
            print("\ntheory on the Tau Ceti's. Maybe they were attacked by us and the Polarians decades ago. Why would they attack ")
            print("\nEarth though? They already launched a first strike on Earth but maybe that was because we started attacking their")
            print("\nbases they felt that they had to respond. What if this war is just a big mistake and we have just been excelading the")
            print("\nviolence with every attack. Will one of us have to destroy the other to finally finish this? Your mind is running")
            print("\nwild and you cant stop it. What can you do to keep your mind busy?")
            print("\n\t1.Get back to your duties")
            print("\n\t2.Take a nap")
            print("\n\t3.Go to the gym")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou decided to get back to your duties. You go the bridge and take your station. While working your mind")
                print("\nstill will not calm down...")
                input("\nPress Enter to continue...")
                continue
            elif success == 2:
                print("\nYou go to your bunk to take a nap. When you get there you climp into bed and close your eyes. Your")
                print("\nmind still will not shut off and allow you to sleep...")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou go to the gym to help take your mind off what you just heard. You work your hardest at")
                print("\nthe gym but when you're done your mind goes right back to where it was...")
                input("\nPress Enter to continue...")
                break

        while True:
            print("\n\n\n\n**************************************************Chapter 6***************************************************")
            print("\nYou still have so many questions but now is not the time. You are on your way to what could be the biggest battle")
            print("\nyet. You need to focus on what to do to get ready for this fight. You are still traveling 24x the speed of light")
            print("\nbut you feel like this is taking forever. Once you get to the Tau Ceti homeworld there will be no time")
            print("\nto wait of think. You dont have much time untill you drop out of FTL. How should you prepare?")
            print("\n\t1.Get your armor ready")
            print("\n\t2.Get the drones ready")
            print("\n\t3.Go to the bridge and assist")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou go to get your armor ready for the fight. The ISA has given you this new lightweight armor that feels")
                print("\nlike you are wearing nothing but still can stop a bullet! You lay it out on your bed to make sure you")
                print("\ndont miss any piece. Once its laid you you put it on one piece at a time.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou go to make sure all the drones are ready and operational. You get to the hangar and the Polarians")
                print("\nare getting all the drones and pilots ready. You assist in helping.")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou go to the bridge to assist. Once you get there everybody is scrambling to get things ready. There")
                print("\nare light flashing and everybody is running around. Its chaos in there but you jump in and help.")
                input("\nPress Enter to continue...")
                break

        print("\n\n\n\n**************************************************Chapter 6***************************************************")
        print("\nYou are now almost to Tau Ceti... You get nervous... You know a big battle is about to happen and")
        print("\nyou do not know if you will walk away from this. Your thoughts go back to your loved ones")
        print("\non " + recalledColony + ". If you fail they may not make it. You may not make it...")
        print("\nThe ship drops out of FTL... You are at the Tau Ceti homeworld...")
        input("\nPress Enter to continue to Chapter 7...")
        chapter7.Game().chapter7()
        return True

if __name__ == "__main__":
    game = Game()
    game.chapter6()

