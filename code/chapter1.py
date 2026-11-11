import cv2
import time
import chapter2

def drawEasterEgg():
    print("\n             01101101              \n")
    print("         01100001 01111001          \n")
    print("     00100000 01110100 01101000    \n")
    print("     01100101 00100000 01100110     \n")
    print("  01101111 01110010 01100011 01100101\n")
    print("     00100000 01100010 01100101      \n")
    print("     00100000 01110111 01101001     \n")
    print("     01110100 01101000 00100000     \n")
    print("         01111001 01101111          \n")
    print("             01110101               \n")
    print("\nHINT: Binary Unlocks A Secret!!")
    #May the force be with you 
class Game:
    def recallCharacterData(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            name = lines[0].split(": ")[1].strip()
            age = int(lines[1].split(": ")[1].strip())
            colony = lines[2].split(": ")[1].strip()
        return name, age, colony

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

    def start(self):
        if self.chapterz():
            pass
        if self.chapterx():
            pass
        if self.chapter1():
            pass
        if self.chapter2():
            pass
        if self.Chapter2Earth():
            pass
        if self.Chapter2Moon():
            pass
        if self.chapter3():
            pass
        if self.chapter4():
            pass
        if self.chapter5():
            pass
        if self.chapter6():
            pass
        if self.chapter7():
            pass
        if self.chapter8():
            pass
        # Continue with more chapters or game logic

    def chapter1(self):
        recalledName, recalledAge, recalledColony = self.recallCharacterData("files/data.txt")
        recalledPerson, recalledShip = self.recallCharacterWork("files/character.txt")
        recalledJob = self.recallCharacterJob("files/job.txt")
        print("Here is your character's information")
        print(f"Name: {recalledName}")
        print(f"Age: {recalledAge}")
        print(f"Colony: {recalledColony}")
        input("\nPress Enter To Continue...")
        imagePath = "images/background.jpg"
        image = cv2.imread(imagePath)
        if image is not None:
            window_name = "Chapter 1"
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            cv2.imshow(window_name, image)
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
        print("\nGAME WILL START IN 5...")
        time.sleep(1)
        print("\nGAME WILL START IN 4...")
        time.sleep(1)
        print("\nGAME WILL START IN 3...")
        time.sleep(1)
        print("\nGAME WILL START IN 2...")
        time.sleep(1)
        print("\nGAME WILL START IN 1...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n*.    .      ..    .* .    .* . .* .*	 .* .*	.** .   .  ..** .   . ..** .   .  .    ..** .   .  .    ...** .")
        print("\n.* .** .   ..** .   .  .    . .* .*	   ..    .* .    .* . .* .*	 .* .*	.** .   ...** .   .  .    ...** .  ")
        print("\n.  .* .* ..** .   .  .    ...** .   .  .    .** .   ..** .   ...** .   .  .    ...** .    ...** .    ...** .  ")
        print("\n	.   .* .*	.   .* .* .* .*	.** .   ..** .   . ..** .   .  .    ..** .   .  .    ...** .    ...** .    ...*")
        print("\n.** .   .  .    ..** .   . ..** .   .  .      ..** .   . ..** .   .  .    ..** .   .  .    ...** .    ...** . ")
        print("\n.   .** . .* . .* . .* . .* . .* ...** .   .  .      ..** .   . ..** .   .  .   ..** .   .  .    ...** .     .")
        print("\n* .    .* . .* . .* . .* ...** .   .  .      ..** .   . ..** .   .  .    ..** .   .  .    ...** .    ...** .  ")
        print("\n.    .* .    .* . .* . .* . .* .*	   ..    .* .    .* . .* .*	 .* .*	.** .   ...** .   .  .    ...** .    ..")
        print(f"\n\tThis is the beggining of the adventure. Here is a little backstory to your character. You are {recalledAge},")
        print("\nyou are attending college. You are living in the present and there is a huge explosion while you are in class!!")
        print("\nYou run out of class pushing though crowds of people. When you get outside you see that a space ship has entered")
        print("\nthe upper atmosphere!! From here you will have to  take an adventure to find out what is going on!!!")
        input("\nPress Enter to continue...")
        while True:
            print("\n\n\n\n**************************************************Chapter 1***************************************************")
            print("\nA large silver concave disk-like ship is hovering over your school, everyones devices are sending Global Security")
            print("\nAlerts, advising the population to seek shelter in-doors \"Everybody please return to your dorms and shelter in")
            print("\nplace\" Your headmaster said while ushering people back in the dorms.")
            print("\nChoose from the following choices:")
            print("\n\t1.Go find your friend")
            print("\n\t2.Return to your dorm")
            print("\n\t3.Speak to your headmaster")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print("\nYou go look for your friend.")
                print("\nYou scan the crowd of people for your friend but the crowd is to thick so you return defeated to your dorm.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou go to return to your dorm")
                print("\nDeciding it is better to go with the crowd you return to your dorm.")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou choose to speak with your headmaster")
                print("\nYou run to your headmaster and he yells \"GET TO YOUR DORM AS FAST AS POSSIBLE!!!\"")
                input("\nPress Enter to continue...")
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 1***************************************************")
            print("\nYou get to your dorm. The large ship that entered the atmosphere is now hovering outside of your window! You turn on")
            print("\nyour T.V. and all broadcasts are about the ship!! You soon realize that there are multiple ships that are entering the")
            print("\natmosphere all across the globe!!\n\nNow you have to choose what to do next")
            print("\n\t1.Call your loved ones")
            print("\n\t2.Try to get back home")
            print("\n\t3.Go outside and look at the ship")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print("\nYou go to call your loved ones but you find out that all the wireless signals are down.")
                print("\nThis makes you very anxious and you dont know what to do next.")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou leave the dorm trying to get back home. You exit the dorm but they are guarding the doors. You go pull the")
                print("\nfire alarm! \"FIRE!! EVERYBODY GET OUT!!\" You sneek out with the crowd.")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou start to run outside to try and see the aircraft. The doors are guarded but you see a fire alarm")
                print("\nthat you pull. The fire alarm goes off \"FIRE!! EVERYBODY GET OUT!!\" You sneek out with the crowd")
                input("\nPress Enter to continue...")
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 1***************************************************")
            print("\nYou run outside the door!! When you get outside the door and the object is just hovering above the ground. Military vehicles")
            print(f"\nstart showing up left and right! One truck come up to you and yells. \"{recalledName} COME WITH ME!!\"")
            print("\nYou have to choose what to do next")
            print("\n\t1.Go with the soldier")
            print("\n\t2.Run the other way")
            print("\n\t3.Ask him what is going on")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print(f"\nYou choose to go with the soldier and he yells \"GET IN THE TRUCK QUICK {recalledName}!!!\" You get in the truck")
                print("\nand he explains that you were chosen in a lottery of gifted peoeple. You drive off with the soldier.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou run the other way because the soldier yelling at you scared you. You run off as fast as you can.")
                print("\nAs you run away you relize the soldiers are there to help")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print(f"\nYou ask the soldier whats going on? The soldier yells \"GET IN THE TRUCK QUICK {recalledName}!!!\"")
                print("\nYou get in the truck and he explains to you that you have been chosen in a lottery of gifted people.")
                input("\nPress Enter to continue...")
                break
        while True:
            print("\n\n\n\n**************************************************Chapter 1***************************************************")
            print(f"\nThe soldier tells you \"Don't worry we're going somewhere safe {recalledName}, your family has been move to a secure")
            print("\n\"location\" he looks around and leans in \"The location you're going to is a holding facility for bigger things.\"")
            print("\nHe hands you something its some sort of ticket with a cryptic code on it. Do you want to take it?")
            print("\n\t1.You take the ticket")
            print("\n\t2.You act like you see nothing")
            print("\n\t3.Throw it out the window")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print("\nYou take the ticket and put it in your pocket, you have other things to worry about. Time seems to pass very quick.")
                print("\nBefore you realize it you are at this \"Camp\".")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou act like you see nothing and he puts it in your pocket anyway. You stare out the window and time seems to")
                print("\npass very quick before you know it you are at this \"Camp\".")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou throw it out the window and the instant you throw it out the window you deaply regret it. You wonder what that")
                print("\ncryptic code was all about...")
                input("\nPress Enter to try again...")
                continue
        while True:
            print("\n\n\n\n**************************************************Chapter 1***************************************************")
            print("\nWhen you arrive to this camp, get out, and you see a bunch of people your age being led towards a")
            print("\nlong line. The soldier tells you \"Get in line and do what you know is right\". Just as he leaves you hear another")
            print("\nsoldier shout \"GET IN LINE AND DO AS YOU'RE TOLD\" What do you do?")
            print("\n\t1.You get in line and put your hands in your pocket.")
            print("\n\t2.Try to Escape")
            print("\n\t3.Yell and scream")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print("\nYou get in line and put your hands in your pocket. You feel the note in your pocket from earlier and decide to take")
                print("\na quick glance at it.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou try to escape by running the opposite way. You end up getting restrained, while you fight back you end up")
                print("\ngetting knocked out.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou try to escape by running the opposite way. You end up getting restrained, while you fight back you end up")
                print("\ngetting knocked out.")
                input("\nPress Enter to try again...")
                continue
        while True:
            print("\n\n\n\n**************************************************Chapter 1***************************************************")
            print("\n\t ____________________________________________________________________")
            print("\t|                01000001 01101100 01100101 01111000                 |")
            print("\t|                          THE TIME IS NOW                           |")
            print("\t|                                                                    |")
            print("\t|                                                                    |")
            print("\t|                         (202) 762 - 1401                           |")
            print("\t|                   Call to receive instructions                     |")
            print("\t|            Report to MEPS in 24 hours for a full breifing          |")
            print("\t|                    01001100 01100101 01100101                      |")
            print("\t|____________________________________________________________________|")
            print("\nYou reach in your pocket and look at your ticket. You pull it out and read it. You notice that it has a message in")
            print("\nbinary code. It also has a number on it to call. Then you see... \"Report to MEPS in 24 hours\". This makes")
            print("\nyou uneasy. You call the number and what does it say when you call?")
            print("\n\t1.Gives you details on what to do next")
            print("\n\t2.Gives you details on what is going on")
            print("\n\t3.Gives you the time")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print("\nYou choose that the prompt said what to do next. The prompt did not say that. Maybe you should try")
                print("\ncalling the number again.")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou choose that the promt gave you more information about whats going on. The prompt did not")
                print("\nsay that. Maybe you should try to call the number.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou choose that the prompt said what time it is and you are correct it did! Now that you have the time")
                print("\nyou proceed to the next part.")
                input("\nPress Enter to continue...")
                break
        while True:
            print("**************************************************Chapter 1***************************************************")
            print("\nYou look at the ticket in confusion. Why would they pick me? You think of any reason but try to put it out of your mind.")  # Enter the question here
            print("\nYou are in line and you notice a lot of diffrent people in line. You wonder what it is they are going to do with all")
            print("\nof these people. You get to the desk with a soldier he asks to see your ticket. He says that the code on the ticket")
            print("\nis your personal code to get into basic. He writes down the code and checks you off the list. You get into the camp and")
            print("\nyou have to choose what to do next")
            print("\n\t1.Go look for your friend")  # choice 7
            print("\n\t2.Try to find your bunk")
            print("\n\t3.Look for ways out")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print("\nYou go to look for your friend. He has to be here you guys have been friends for a long time and he is much smarter")  # Enter answer 1 here
                print("\nthan you. Maybe he has answers on what is going on here.")
                print("\nPress Enter to continue...")
                input()
                break
            elif success == 2:
                print("\nYou go to try and find your bunk but you cant find it. You decide it is best to go look for your friend for some")  # Enter answer 2 here
                print("\nanswers. He must know what is going on here.")
                print("\nPress Enter to continue...")
                input()
                break
            elif success == 3:
                print("\nYou try to look for a way out of here. You look around and there is a huge fence like they have been planning for")  # Enter answer 3 here
                print("\nthis. You raise suspicion and the gaurds see you! They throw you in jail...")
                print("\nPress Enter to try again...")
                input()
                continue
                break  # Exit the loop if the input is valid
    
        while True:
            print ("\n\n\n\n**************************************************Chapter 1***************************************************")
            print ("\nYou find your friend and ask \"Whats going on?\" he replies \"They rounded up all these people for some military") # Enter the question here
            print ("\nlottery. Once the space ships came in they triggered a protocol that creates a lottery for all the gifted")
            print ("\npeople on earth. We have to wait here until you get your name drawn. Everybody that has had their name drawn")
            print ("\nhas left this place and never come back. People say that they are going to some base to train for some war")
            print ("\nThis information scares you what should you do next?")
            print ("\n\t1.Talk more with your friend")										#choice 8
            print ("\n\t2.Go get food")
            print ("\n\t3.Try to ask a soldier for more information")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if (success == 1):
                print ("\nYou decide to go talk with your friend some more. He says \"It is just crazy how many people they have here")# Enter answer 1 here
                print ("\nand more keep coming. It has to do with some top secret mission that we aren't suppose to know about\"")
                print ("\nPress Enter to continue...")
                input ()
                break

            elif (success == 2):
                print ("\nYou try to shake off what you just heard and try to find some food. You go to look for food and soon") # Enter answer 2 here
                print ("\nrealize that its not chow time and you cant get food without money when its not chow time.")
                print ("\nPress Enter to try again...")
                input()
                continue
            
            elif (success == 3):
                print ("\nYou decide to go talk to a soldier. He says \"WHAT DO YOU WANT!\" You reply with \"Hey i just want to know") # Enter answer 3 here
                print ("\nmore about whats going on\" He replies with \"All these people are here for a reason. There is a secret")
                print ("\nmission that nobody will talk about\"")
                print ("\nPress Enter to continue...")
                input()
                break
            
        while True:
            print ("\n\n\n\n**************************************************Chapter 1***************************************************")
            print ("\nAfter learning a little about whats going on here you and your friend decide its best to stick with each other for now.") # Enter the question here
            print ("\nyou decide to wait around a bonfire for further intructions from the soldiers. You notice some people aruging")
            print ("\nthey start shoving eachother and before you know it theres a mob of sweaty brawling people, your friend says")
            print ("\n\"We should stay out of it, no matter how wild it gets\" What do you do?")
            print ("\n\t1.You and your friend move farther away and Alert the guards")										#choice 9
            print ("\n\t2.You try to rescue the person")
            print ("\n\t3.You say \"Are you kidding?! That looks fun\" and jump into the mix")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 4:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
            if (success == 1):
                print ("\nYou and your friend move to a safer distance and grab a guard, telling them that a person is being harrased and hurt.") # Enter answer 1 here
                print ("\nthey take action and break the scuffle, up removing unruly people. You see the person and she flashes a bloody smile")
                print ("\nyou friend pats your shoulder \"You did the right thing bud\"")
                print ("\nPress Enter to continue...")
                input()
                break
            
            elif (success == 2):
                print ("\nYou rush into the brawl pushing and squeezing before you grab on to the persons arm and yank her free running back to") # Enter answer 2 here
                print ("\nsafety. \"Thank you, i am sorry you got hurt, but you did the right thing\"")
                print ("\nPress Enter to continue...")
                input()
                break
            elif (success == 3):
                print ("\n\"Thats literally the worst idea you've EVER HAD\" you hear your friend warn. You dive into the brawl and trade blows") # Enter answer 3 here
                print ("\nwith other people with no regards to who was in the right or not. You feel a dull metallic pain on the back of your head")
                print ("\nand the world goes dark")
                print ("\nPress Enter to try again...")
                input()
                break
            elif (success == 4):
                drawEasterEgg()
                print ("You have just unlocked an Easter Egg!!!!")
                print ("\nPress Enter to Continue...")
                input()
                break # Exit the loop if the input is valid
        
        while True:
            print ("\n\n\n\n**************************************************Chapter 1***************************************************")
            print ("\nAfter everyone settles down, theres a lot less people now, you've been herded into a large auditorium.") 
            print ("\nA soldier comes onto the stage. \"I know you are scared\" the crowd agrees \"I know you are tired, but this is not just")
            print ("\nabout us individuals, it is about our planet, these inturders only want one thing! Our Destruction and I say \"WE")
            print ("\nSHALL NOT BACK DOWN, OR GO QUIETLY!!\" Choose what to do next. ")
            print ("\n\t1.Talk more with the soldier")										#choice 10
            print ("\n\t2.Listen to what they have to say")
            print ("\n\t3.Run out of the auditorium")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
            if (success == 1):
                print ("\nYou go to talk with the soldier and she explains \"There is a alien race invading the planet right now") # Enter answer 1 here
                print ("\nwith a message from the future!.\"")
                print ("\nPress Enter to continue...")
                input()
                break
            elif (success == 2):
                print ("\nYou stay in the auditorium and listen to what they have to say \"There is an alien race invading the planet") # Enter answer 2 here
                print ("\nright now with a message from the future!!\"")
                print ("\nPress Enter to continue...")
                input()
                break
            
            elif (success == 3):
                print ("\nYou run out of the auditorim in fear of what they are saying. They had an important message you needed") # Enter answer 3 here
                print ("\nto hear.")
                print ("\nPress Enter to try again...")
                input()
                continue
            break # Exit the loop if the input is valid
        while True:
            print ("\n\n\n\n**************************************************Chapter 1***************************************************")
            print ("\nThere is an important message from the future and you hear \"The aliens have come back from the future to give") # Enter the question here
            print ("\nus a message. There is an alien race from the future that plans to destroy earth! They are here to warn us about")
            print ("\nthis invasion of the species called The Tau Ceties.\" You hear about this new race from the future called The")
            print ("\nPolarians warning you about this race called The Tau Ceties coming to destroy the world in the future and you are")
            print ("\nshocked by this information. What do you do next?")
            print ("\n\t1.Continue talking to the soldier")										#choice 11
            print ("\n\t2.Leave auditorim")
            print ("\n\t3.Go back to your bunk")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
            if (success == 1):
                print ("\nYou continue talking with the soldier and she explains \"The Polarians are the good guys they are trying") # Enter answer 1 here
                print ("\nto warn us about this empending attack from The Tau Ceties. The government held this lottery to bring everybody")
                print ("\nwho could help to this location to build the equipment we will need to fight this war. The Polarian's have")
                print ("\nagreed to give us a massive amount of tech from the future.\"")
                print ("\nPress Enter to continue...");
                input()
                break
            elif (success == 2):
                print ("\nYou leave the auditorium in shock of what you heard. You think about going back because this may be your")# Enter answer 2 here
                print ("\ndestiny but, you cant take it and leave.")
                print ("\nPress Enter to try again...")
                input()
                break
            elif (success == 3):
                print ("\nYou go back to your bunk. You get there and all you can think about is why are The Polarians here? What")  #nter answer 3 here
                print ("\nis going to happen next? You realize you should have stayed.")
                print ("\nPress Enter to try again...")
                input()
                continue
            break # Exit the loop if the input is valid
        
        while True:
            print ("\n\n\n\n**************************************************Chapter 1***************************************************")
            print ("\nYou just heard why The Polarian's are here. You are shocked you think about why they chose you? Why did they need") # Enter the question here
            print ("\nyou? You think to yourself how long do we have? Will we be ready? What kind of tech are we getting? Just as all this")
            print ("\nis racing through your head you realize you dont have much time before you have to report. What do you do next?")
            print ("\n\t1.Try to find some way out")										#choice 12
            print ("\n\t2.Go see your friend")
            print ("\n\t3.Report to MEPS")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
                if success < 1 or success > 3:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
            if (success == 1):
                print ("\nYou try to find some way out. You look aroudn for weaknesses and talk to people to see if they can smuggle you.") # Enter answer 1 here
                print ("\nYou have no luck. Then a gaurd comes up to you and says \"YOU CANT GET OUT OF HERE!!!\"")
                print ("\nPress Enter to try again...")
                input()
                continue
            
            elif (success == 2):
                print ("\nYou go to see your friend. You guys talk about the information you just heard. He says \"This must be important\"")# Enter answer 2 here
                print ("\nto have got all of us together. I wonder what they plan to do with us here? We should get ready to report\"")
                print ("\nPress Enter to continue...")
                input()
                break
            
            elif (success == 3):
                print ("\nYou report to MEPS. You get there early but they still take you in. You cant help but wonder where your friend")# Enter answer 3 here
                print ("\nis at. Also, what they plan to do here?")
                print ("\nPress Enter to continue...")
                input()
                break
            break # Exit the loop if the input is valid
        
    

        print("\nPress Enter to continue to Chapter 2...\n")
        input()
        chapter2.Game().chapter2()


if __name__ == "__main__":
    game = Game()
    game.chapter1()

