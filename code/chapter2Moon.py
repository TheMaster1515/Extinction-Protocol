import time
import chapter3

def drawEasterEggMoon():
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


    def Chapter2Moon(self):
        recalledName, recalledAge, recalledColony = self.recallCharacterData("files/data.txt")
        recalledPerson, recalledShip = self.recallCharacterWork("files/character.txt")
        recalledJob = self.recallCharacterJob("files/job.txt")
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print("\nYou get your job now and then the soldiers excort you to small crafts in an airfield. They herd dozens of")
            print("\npeople over to the airfield. You get on your craft with around a dozen other people. You try to ask what is")
            print("\ngoing on but the soldier yell \"STOP TALKING!! YOU WILL FIND OUT SOON!!!\" Now you have to choose how to react.")
            print("\n\t1.Yell at the soldier")
            print("\n\t2.Sit down and shut up")
            print("\n\t3.Attack soldier")
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
                print("\nYou chose to yell at the soldier. You yell \"TELL ME WHATS GOING ON!!!\" He responds by restraining you. You are")
                print("\nnow tied up to your seat. You then get gagged and have to sit on the craft for hours!!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou choose to sit down and shut up. After the soldier yelled you just sit down and look out your window.")
                print("\nYou see that you are leaving the atmosphere!!!")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou choose to attack the soldier. You run at him and throw him against the door! He hits the door hard")
                print("\nand there is a small leak! He throws you back at door and it busts open!!! You get flug into space!")
                input("\nPress Enter to try again...")
                continue
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\nYou arrive to a facility on the Dark side of the Moon and you check in with the person at the desk and he asks you")
            print(f"\n\"Do you have your ticket?\" You pull out your ticket and he scans it and tells you \"{recalledName} that code")
            print("\nwill unlock at the end of your enlistment\" Go to door number 4. Now you have to choose what to do next.")
            print("\n\t1.Run back to the shuttle")
            print("\n\t2.Say yes sir")
            print("\n\t3.Nod and walk by")
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
                print("\nYou have chosen to run back to the shuttle. You push the guy at the desk and run to the shuttle. When you")
                print("\nget there you get tackled by two other soldiers and get thrown in a small cell.")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou chose to say yes sir and keep on walking. You walk past the desk and see a huge dome structure. It")
                print("\nis amazing!! There is a line of people waiting to get into the door you were told to go to.")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou chose to nod and walk by. You enter a huge dome structure and it is amazing! There is a line of")
                print("\npeople waiting at the door you were told to go to.")
                input("\nPress Enter to continue...")
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\nYou get in line with everbody else and the soldier at the door says \"{recalledName} here is your bunk. This will be")
            print("\nwhere you will live for the next few months.\" You see a room with six bunk beds in it. You unpack all your stuff in a")
            print("\nsmall foot locker. Before you put your stuff in the foot locker there is a note on it... You read the note and it says")
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
            print(f"\nOne of your bunk mates asks \"Are you from {recalledColony}?\" You reply with yes, why?")
            print(f"\nHe says \"We are all from {recalledColony}\" Then a huge alarm goes off and a Drill Instructor shows up saying")
            print("\n\"You all will be here for the next few months learning how to be a soldier! We are on the Moon and you will learn how")
            print("\nto fight in space! We are called the Interglactic Space Agency I.S.A. for short. Now we train!!!!\"")
            print("\n\t1.Learn how to fight")
            print("\n\t2.Go to class")
            print("\n\t3.Go to the shooting range")
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
                print("\nYou want to learn how to fight. You ask the Drill Instructor to teach you how to fight. He escorts you to a building.")
                print("\nYou guys take of your shoes and get on the mats. He shows you a couple techniques to take down another human. After")
                print("\nshowing you how to grapple he shows you a very advanced technique to disarm a being. The \"Volcun Neck Pintch\" he takes")
                print("\nhis hand and puts it on your neck and pinches it. You fall to the ground. You say \"Wow!! That was amazing!!!\"")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou choose to go to class. You ask the soldier to take you to the classroom. You get to a room filled with computers.")
                print("\nYou sit down at an empty one and open up the training manual. There is a lot of information on how to fly in space and")
                print("\nhow to work in Zero G. You are amazed at some of the information they give you and wonder how they optained it?")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print(f"\nYou choose to go to the shooting range. You ask the soldier where it is. He takes you there and its an indoor range")
                print(f"\nthat is pretty long. The Drill Instructor give you a rifle and says \"Show me what you got {recalledName}!\"")
                print("\nYou shoot the targets with extreme acuracy! The Drill Instructor says \"Wow!! Have you shot before?\"")
                print("\nYou respond \"Never in real life!\"")
                input("\nPress Enter to continue...")
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print("\nYou just got done doing some training. Now you are stronger than ever! You get hearded into a large auditorium.")
            print("\nThere is a speaker that says \"You are all almost through your training. Now we tell you more about the situation.")
            print("\nThere is an alien race called The Tau Ceties that are coming to destroy the world in the future. The Polarians have")
            print("\nto help us get ready for this invasion. We have begun fitting our planes with pulse energy weapons, our communication")
            print("\nequiment has been upgraded to work on quantium technology, and our engines are faster than ever! You will all now")
            print("\nbe critical in winning this war. You guys will be sent deep out in space to fight on the front lines. With the training")
            print("\nyou have recieved you are now ready to fight!!!\"")
            print("\n\t1.Hear more from the speaker")
            print("\n\t2.Yell and scream")
            print("\n\t3.Run out the door")
            try:
                success = int(input("\nChoose an option (1, 2, 3, or 4): "))
                if success < 1 or success > 4:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, 3, or 4.")
                time.sleep(3)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
            elif success == 4:
                drawEasterEggMoon()
                print("You have just unlocked an Easter Egg!!!!")
                input("\n\nPress Enter to Continue...")
        while True:
            print("\n\n\n\n**************************************************Chapter 2***************************************************")
            print("\nYou hear all that was said. You feel empowered! You get up and go to the front to get your ship assignment and you")
            print("\nnotice somebody you know in line. You see your friend you met at the camp on earth! You say \"Hey! I remember you")
            print("\nfrom the camp on earth! I never got your name. What was your name?\"")
            characterPerson = input("\nEnter your friends name: ")
            if not characterPerson:
                print("\n\tNothing entered. Please enter some text.")
                continue
            with open("files/character.txt", "w") as f:
                f.write(f"Person: {characterPerson}\n")
                f.write(f"Ship: \n")
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
            characterShip = input("\nPlease type which ship you would like to be stationed on: ")
            if not characterShip:
                print("\n\tNothing entered. Please enter some text.")
                continue
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
            break
        chapter3.Game().chapter3()
        return True
if __name__ == "__main__":
    game = Game()
    game.Chapter2Moon()


