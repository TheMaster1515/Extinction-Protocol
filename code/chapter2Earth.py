import time
import chapter3

def drawEasterEggEarth():
    print("\n                       01001001 					\n")
    print("                   00100000 01100110 				\n")
    print("              01100101 01100101 01101100 			\n")
    print("              00100000 01110100 01101000 			\n")
    print("              01100101 00100000 01101110 			\n")
    print("          01100101 01100101 01100100 00100000 		\n")
    print("     01110100 01101000 01100101 00100000 01101110 	\n")
    print("          01100101 01100101 01100100 00100000 		\n")
    print("              01101111 01110010 00100000 			\n")
    print("              01110011 01110000 01100101 			\n")
    print("                   01100101 01100101 				\n")
    print("                       01100100 					\n")
    print("\nHINT: Binary Unlocks A Secret!!")

class Game:
    def recallCharacterData(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                name = lines[0].split(": ")[1]
                age = int(lines[1].split(": ")[1])
                colony = lines[2].split(": ")[1]
            return name, age, colony
        except (FileNotFoundError, IndexError, ValueError):
            return "Unknown", 0, "Unknown"

    def recallCharacterWork(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                person = lines[0].split(": ")[1]
                ship = lines[1].split(": ")[1]
            return person, ship
        except (FileNotFoundError, IndexError):
            return "Unknown", "Unknown"

    def recallCharacterJob(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                job = lines[0].split(": ")[1]
            return job
        except (FileNotFoundError, IndexError):
            return "Unknown"

    def Chapter2Earth(self):
        recalledName, recalledAge, recalledColony = self.recallCharacterData("files/data.txt")
        recalledPerson, recalledShip = self.recallCharacterWork("files/character.txt")
        recalledJob = self.recallCharacterJob("files/job.txt")
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\nNow that you have choosen your job you will have to go through basic training. Some soldiers come over and tell you")
            print(f"\n\"Hey {recalledName} come over here to get in processed.\" You walk over to a soldier that escorts you into a")
            print("\nshuttle. There are about a dozen other recruits there. You look out the window as you fly away. You see the ground")
            print(f"\nmove away very fast! You race over {recalledColony} really fast! Then you land in the middle of nowhere and")
            print("\nthe ground opens up. You land inside of an underground bunker!. The soldier stands up and says \"Okay you guys just")
            print("\nlanded to our ISA secret facility. This is whwere you will be trained.\" What do you do?")
            print("\n\t1.Get off the shuttle")
            print("\n\t2.Scream and yell")
            print("\n\t3.Try to get off the shuttle")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print("\nYou have chosen to get off the shuttle. You exit the shuttle with everybody else and the soldier escorts you to a")
                print("\ndesk. The soldier at the desk asks \"Let me scan your ticket. The code on your ticket will unlock when you are done")
                print("\nwith your enlistement.\"")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou chose to yell and scream. You yell and scream \"GET ME OFF OF HERE!!!!\" A soldier comes over and restrains you.")
                print("\nThey end up taking you to a cell.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou have choosen to try and get off the shuttle. A soldier sees you and comes over to restrain you. He hits you over the head")
                print("\nand you wake up in a cell.")
                input("\nPress Enter to try again...")
                continue
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\nYou choose {recalledJob}. Congrats!! You have just made a major decision that will choose the path of your life.")
            print("\nYou enter a very large room with multiple doors. A soldier at the desk says \"Go to door number 4\" You go over to")
            print(f"\ndoor number 4 and you find yourself in a room filled with bunks. Somebody asks you \"Hey are you from {recalledColony}?\"")
            print(f"\nYou reply \"Yes I am are you from {recalledColony}?\" He replies with yes. You are curious on why everybody")
            print("\nfrom your colony is in the same room. You realize this is very real and get scared. What do you do?")
            print("\n\t1.Try to talk to somebody")
            print("\n\t2.Run out the room")
            print("\n\t3.Keep to yourself")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print("\nYou choose to try and talk to somebody. You go find a soldier and talk with him. You express your concerns and he")
                print("\nsays \"Hey I know this is a big change but you must do this for the world.\"")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou choose to run out of the room. You push the guy who was talking to you and run out the door. A soldier stops you")
                print("\nand restrains you. Anoher soldier comes by and throws you in a cell.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou choose to keep to yourself. You go find your bunk and look at everything. You see a bunk that is made and a")
                print("\nfoot locker at the foot of the bed.")
                input("\nPress Enter to continue...")
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print("\nWhen you look at your foot locker you see a note on it. Very curious. You read the note and it says")
            print("\n\"What object has keys that open no lock, space but no room, and you can enter but not go in?\"")
            print("\n\t1.A computer keyboard")
            print("\n\t2.An easter egg")
            print("\n\t3.Phone")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print("\nYou choose a computer keyboard and you choose correctly!!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou choose an easter egg. Now this is a good answer it is not correct sorry...")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou choose a phone. Now this is a good answer it is not correct sorry...")
                input("\nPress Enter to try again...")
                continue
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print("\nYou leave the room and are filed into a line where a soldier says \"You are here for basic training along with all")
            print("\nthe other training you have had you will recieve special training. Please pick from the following options for your")
            print("\ntraining.\"")
            print("\n\t1.Work on a warp drive")
            print("\n\t2.Create gravity")
            print("\n\t3.Fix quantium communications")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 4:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            if success == 1:
                print("\nYou chose how to work on a warp drive. The soldier then files you into a classroom with a huge engine in it! You")
                print("\nare amazing on the fact you are looking at a real warp drive!! They give you a huge handbook filled with all sorts of")
                print("\ntechinal information. You learn all you can then they sit you in a classroom to take a test. You take this long")
                print("\nmultiple choice test about warp drives. The scores come back and you passed!! They take you over to the warp drive")
                print("\nand show you how it all works in real life. You learn all you can and feel ready to do anything with a warp engine.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou chose how to make gravity. The soldier then files you into a classroom with a mock bridge in it. You are very")
                print("\ncurious on how you are going to create gravity!! They sit you down at a desk and throw a big manual on the desk for")
                print("\nyou to study. You study all you can about gravity. Then there is a test that they ask everybody to take. It is a")
                print("\nvery long multiple choice question test. You take it and find out that you passed!! They take you over to the mock")
                print("\nbridge and show you how to create gravity! When you are in the bridge they turn off a switch and you float!! You")
                print("\nare amazed on how they are able to do this!")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou chose how to fix quantium communications. The soldier then files you into a classroom with this huge communication")
                print("\nequipment. There is are muliple desks. You go to sit down at one and they throw a huge manual on your desk. You look")
                print("\nthrough it and it is a lot of information! After reading through the manual they give you a test. This very long")
                print("\nmultiple choice test. You take the test and find out you passed!! Then you go over to the large communication equipment")
                print("\nthey explain you can talk real time with no delay anywhere in the universe!! They use the mic to talk to someobdy. You")
                print("\nhear a voice on the other end. You ask where the voice is from they say \"That is all the way from Pluto!\"")
                input("\nPress Enter to continue...")
                break
            elif success == 4:
                drawEasterEggEarth()
                print("You have just unlocked an Easter Egg!!!!")
                input("Press Enter to Continue...")
                input()
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print("\nYou just got done doing some training. Now you are stronger than ever! You get hearded into a large auditorium.")
            print("\nThere is a speaker that says \"You are all almost through your training. Now we tell you more about the situation.")
            print("\nThere is an alien race called The Tau Ceties that are coming to destroy the world in the future. The Polarians have")
            print("\nto help us get ready for this invasion. We have begun fitting out planes with pulse energy weapons, our communication")
            print("\nequiment has been upgraded to work on quantium technology, and our engines are faster than ever! You will all now")
            print("\nbe critical in winning this war. You guys will be sent deep out in space to fight on the front lines. With the training")
            print("\nyou have recieved you are now ready to fight!!!\"")
            print("\n\t1.Hear more from the speaker ")
            print("\n\t2.Yell and scream")
            print("\n\t3.Run out the door")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print("\nYou choose to hear more from the speaker. He continues \"Now that we are all ready we are going to assign you with")
                print("\nyour ship. Everybody come up to the desks up front and get your assignment. This will be the most important thing")
                print("\nin your life! Make all of us at the ISA proud!\"")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou choose to yell and scream. You get frightened by the incoming invasion and start to yell ans scream! The soldiers")
                print("\nrush to you and try to contain you. They end up throwing you in a small cell to rot away.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou choose to run to the door. You get frightened by the incoming invasion and start to run to the door. The")
                print("\nsoldiers intercept you and restrain you. They detain you and throw you in a small cell to rot away.")
                input("\nPress Enter to try again...")
                continue
        while True:    
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print("\nYou hear all that was said. You feel empowered! You get up and go to the front to get your ship assignment and you")
            print("\nnotice somebody you know in line. You see your friend you met at the camp on earth! You say \"Hey! I remember you")
            print("\nfrom the camp on earth! I never got your name. What was your name?\"")
            characterPerson = ""
            characterShip = ""
            while True:
                characterPerson = input("\nEnter your friends name: ")
                if not characterPerson.strip():
                    print("\n\tNothing entered. Please enter some text.")
                    continue
                break
            with open("files/character.txt", "w") as f:
                f.write(f"Person: {characterPerson}\n")
                f.write(f"Ship: {characterShip}\n")
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\n\"Hey {characterPerson} how have you been doing? This is all crazy isn't it? The Tau Ceties are coming? and")
            print(f"\nThe Polarians are here to help us? I am getting very overwhelmed.\" He replies \"Hey {recalledName} yes I")
            print("\nknow me too! They took me from my house and put me in that camp with no warning! I heard that the ISA is some super")
            print("\nsecret organization that has been around since Apollo! They have super advanced technology and with tech from the future")
            print("\nthey will be unstoppable! We have to win this war for the world!!!\"")
            input("\nPress Enter to continue...")
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\nYou and your friend {characterPerson} get done with all your training and now it is time for you to go to")
            print("\nyour ship. You get in a line of people and you see there are three desks with officer's at them. You get to the")
            print("\nend of the line and a soldier says \"Let me see your ticket\" You pull out your ticket and he scans the code.")
            print("\nHe says \"You can choose from these ships. The Stargazer, The Nostromo, and The Phoenix\"")
            while True:
                characterShip = input("\nPlease type which ship you would like to be stationed on: ")
                if not characterShip.strip():
                    print("\n\tNothing entered. Please enter some text.")
                    continue
                break
            with open("files/character.txt", "w") as f:
                f.write(f"Person: {characterPerson}\n")
                f.write(f"Ship: {characterShip}\n")
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\nYou have choosen {characterShip}. Congrats! Your friend {characterPerson} got assigned the exact same ship!")
            print("\nYou are led outside by a soldier. Before going out the airlock you are given a small device that he says \"This is your")
            print("\nspace suit. Place it on your chest and a thin film will cover your body allowing you to go in space\" You put the device")
            print("\non your chest and it activates. A thin film covers your body. You walk out the airlock with the other recruits and see a")
            print("\nlarge landing pad with multiple ships on it!")
            input("\nPress Enter to continue to Chapter 3...")
            chapter3.Game().chapter3()
            return True

if __name__ == "__main__":
    game = Game()
    game.Chapter2Earth()




