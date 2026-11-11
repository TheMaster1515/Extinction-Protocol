import cv2
import time
import chapter8

def drawEasterEgg7():
    print("            01010100 				")
    print("            01101000 				")
    print("         01100101 00100000 		")
    print("         01101110 01100101 		")
    print("         01100101 01100100 		")
    print("   01110011 00100000 01101111 		")
    print("   01100110 00100000 01110100 		")
    print("   01101000 01100101 00100000 		")
    print("01101101 01100001 01101110 01111001 ")
    print("00100000 01101111 01110101 01110100 ")
    print("01110111 01100101 01101001 01100111 ")
    print("01101000 01110100 00100000 01110100 ")
    print("01101000 01100101 00100000 01101110 ")
    print("01100101 01100101 01100100 01110011 ")
    print("   01101111 01100110 00100000 		")
    print("   01110100 01101000 01100101 		")
    print("         01100110 01100101 		")
    print("            01110111 				")
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

    def chapter7(self):
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

        imagePath = "images/Chapter_7.jpg"
        image = cv2.imread(imagePath)
        if image is not None:
            window_name = "Chapter 7"
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

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n_________________________________________________________________________")
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
        print("_________________________________________________________________________")
        input("\n\n\n\n\nPress Enter to continue... ")

        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nYou just arrived to the Tau Ceti homeworld... when you drop out of FTL you see their planet")
            print("\nwith a large moon orbiting it.The planet looks a lot like Earth!It is much bigger though,")
            print("\na \"Super Earth\". There is a large blue ocean covering it with multiple continents all over.")
            print("\nThe moon is bigger than our moon but when you look at it closer you realize that the base that")
            print("\nis there is almost exactly like their forward operating bases just bigger! The Polarian's drop")
            print("\non out of FTL right next to your ship and they brought reinforcements.")
            print("\n\t1.Attack the moon")
            print("\n\t2.Attack the planet")
            print("\n\t3.Wait for the Tau Ceti's to fire")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 4:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou want to attack the moon.That would be the best option to take out the moon first before")
                print("\nfighting with the planet.The moon has a lot of defenses so you must strike quick and fast.")
                print("\nYou radio to the Polarians to group up and attack the moon first.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou want to attack the planet first.You radio to the Polarians to attack the Planet first.")
                print("\nThey agree and your ships form up to attack.Right when you are about to attack there is a")
                print("\nhuge explosion.The Polarian's ship just exploded. There is another missile heading for your")
                print("\nship.The moon base fired on you and your ship exploded.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou wait for the Tau Ceti's to fire. At first it seems to work. They dont fire on you as you")
                print("\nmove closer and closer to the planet.Maybe this will work ? Then the moon fires multiple missles")
                print("\non your ships.All the ships explode.")
                input("\nPress Enter to try again...")
                continue
            elif success == 4:
                drawEasterEgg7()
                print("You have just unlocked an Easter Egg!!!!")
                input("\n\nPress Enter to Continue...")
        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nYou group up with the polarians and they brought a lot of ships!!Compared to yours you feel")
            print("\nsmall... You agree to move in fast and flank from the other side.So the polarians flank from")
            print("\nthe back of the moon while you take their fleight head on!!!There ships start to make shape in")
            print("\nthe distance.They have large battle cruisers whill smaller fighter ships protecting them.")
            print("\nI am sure that there are more ships we cant see yet but they out number us by a lot!!!")
            print("\n\t1.Launch Drones")
            print("\n\t2.Launch Fighters")
            print("\n\t3.Launch Missles")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou choose to fire the drones this is the best option!This way the crew can stay safe in case")
                print("\nthey dont want a fight right now.The drones fly out of their baysand travel to the large")
                print("\nbatllships coming at us.They move fast!!!When they are within firing range they ask to fire,")
                print("\nthe captian does not give them permmision.They are in a stand still around the enemy!!!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou want to launch the fighters!They fly out of their bays very fast!The enemy fires their")
                print("\nfighters as well.This is not good... they could have seen this as aggression.When the")
                print("\ngroups of fighters get closer there is a dettination!!!Who fired ? ? ? All the sudden there")
                print("\nis a nuculear alarm... there is a nuke locked on your ship.The nuke fires and even with")
                print("\nall you can do you explode!!!!")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou launch missles!!They attacked youand you want to get back at them!You send your largest")
                print("\nnon nuclear missles at their battle ships.They launch a volly of missles as well.Your guns")
                print("\ntake out most of them but some hit damaging the ship.One lands in the magazine...with the")
                print("\nnuclear warheads... you explode.")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nYou wonder what is going on ? Why did the Captian not give them permission to fire ? Everybody")
            print("\nyells and screams!\"Why didnt you attack???\" The Captian says \"remember back on the base")
            print("\nI do no believe they wanted to fire first.I am testing my theory. \" So we are at a stand")
            print("\nstill with the enemy....minutes seem like hours... then out of nowhere an explosion!!")
            print("\nThe Captian yells \"Confirm who fired!!\" You yell back \"I cant figure it out!!!\"")
            print("\nHe says \"Hell, Fire!!!\" The drones fire on the battleships like the weren't even there.")
            print("\nThere is a huge explosion!!Where did it come from ?")
            print("\n\t1.The Polarians")
            print("\n\t2.Your fleet")
            print("\n\t3.Tau Ceti Moon")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nThe explosion came from the Polarians.One of their battleships just exploded!You are trying")
                print("\nto get more details about it when someobody shows you the video playback.Turns out The")
                print("\nPolarians did not wait to fire like we did.They went in guns blazing and it looks like")
                print("\nthe moon base fired a missle and destroied one of their battleships!They should have")
                print("\nwaited like we did.Now the fight is on!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou choose that one of your ships in the fleet exploded.The ship right next to you")
                print("\nexploded!Sending a massive explosion and your ships gets caught in it!.The whole")
                print("\nfleet blows up!")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou choose that the Tau Ceti Moon exploded.The base goes up in a huge explosion!There")
                print("\nis a massive shockwave heading to you.The Polarians get caught in it and explode!")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nNow that the Polarians fired first The Tau Ceti's are not holding back at all. They ")
            print("\nare firing from everywhere!The moon base is launching even more ships into orbit.")
            print("\nYour captian orders everybody to battle positions and to start firing on the Tau Ceti's.")
            print("\nYour fleet sets up an attack pattern to hit the moon base while the Polarians are dealing with")
            print("\nall the drones that were fired.A massive battle is going on around this moon!The Tau")
            print("\nCeti's have more than double the ships of the last moon base and the planet hasnt even")
            print("\nlaunched their drones yet.You are set up to attack the base once and for all.")
            print("\n\t1.Continue the attack on the Moon")
            print("\n\t2.Fight incoming drone")
            print("\n\t3.Get into better position")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou continue with the attack on the moon base.You lauch all your dronesand fire off")
                print("\na couple nukes at the base.All the nukes get shot out of the sky except for one.One nuke")
                print("\nmade it past their deffensivesand explodes on the base!There is a huge bright flast of light!")
                print("\nAfter the exposion you can see that half of the base is now gone!The drones are making")
                print("\nruns on the moon destoring all they can!")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nThere is an incoming droneand you decide to attack it first!You take control over one of")
                print("\nyour drones that you have to attack the Tau Ceti drone first.You have control over the drone")
                print("\nand you fire a missleand the droneand then fire the afterburners to get there quick!")
                print("\nThe missle doesnt hit your target but you are close enough for guns!You fire burst after")
                print("\nburst when finally it explodes!You just saved the fleet.Now you focus back on the attack of")
                print("\nthe moon.Your ship blew up half the base while you were taking care of that drone.The")
                print("\nbase is smokingand burning when your drones starting making runs on the base slowly")
                print("\ndetroying the base.")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou are looking at your postion going to the moon baseand you are off by a lot!If you")
                print("\ndont correct now you could get caught in the gravityand sucked into the moon!You yell")
                print("\n\"FULL REVERSE!!!\" The ship rumbles as it slows down but breaks apart and explodes!")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nThere is a massive battle going on right now!Your ship is sending volly after volly")
            print("\nof missles at the moon while The Polarians are fighting the drones with their drones.")
            print("\nJust as you get a warning that the planet has launched their drones you are focused on")
            print("\nthe moon when a huge explosion happens!!The last missle you sent made a dirrect hit")
            print("\nthat caused a huge explosion!The moon is crackingand breaking up into pieces!!!")
            print("\n\t1.Attack the drones from the planet")
            print("\n\t2.Finish off the drones around the moon")
            print("\n\t3.Radio the Polarians")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou want to attack the drones from the planet.You order to launch the more drones!")
                print("\nThey are about to intercept the drones from the planet when all the sudden the breaking")
                print("\nup moon hits your ship!Then more pieces hit.You got distracted and now the ship")
                print("\nexploded!")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou want to attack the drones around the moon.The moon is breaking up and the drones")
                print("\nare getting hit by the breaking up moon!They are all exploding!You didnt even have")
                print("\nto launch your drones but you got very close to the moon and one large piece breaking up")
                print("\nhits the ship and explodes!")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou radio The Polarians to find out their plan.They radio back saying that they are going to")
                print("\npull back to avoid the breaking up moon.You advise the Captian and the whole fleet takes")
                print("\nup orbit far from the planet.The breaking up moon is falling to the planet destroying")
                print("\nall the ships and drones in it's path. Then suddenly the planet starts to break apart!")
                print("\nThere is a huge explosion!")
                input("\nPress Enter to continue...")
                break

        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nThe planet just explodedand is now just a bunch of rubble with a cloud of gas surrounding it.")
            print("\nYou are finally taking a breath now that you have deffeated The Tau Ceti's. You take a look")
            print("\naround and see that you only have a few ships left and The Polarians only had a few")
            print("\nships as well.That was a huge battle that took the lives of a lot of people on both")
            print("\nsides.You are relieved that this battle is over with and you can finally go home!!!")
            print("\nJust as you are cheering and excited to get back home you pick up something on radar.")
            print("\nThere is a pod smaller than a ship on the radar.")
            print("\n\t1.Fire a missle at the pod")
            print("\n\t2.Go investigate")
            print("\n\t3.Ask The Polarians to check it out")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou want to fire a missle at the pod to finish off The Tau Ceti's for all! The missle")
                print("\nis shot at the pod and just as it is about to explode you get a message over the radio")
                print("\nsaying \"We are the last of The Tau Ceti's please do not fire we are the last hope...\"")
                print("\nYou try to disable the missle but it hits the pod and explodes...")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou want to go investigate the pod.You get closer and see that it is a pretty big pod!")
                print("\nAlmost the size of a battle ship but much different.No guns or missles on board.")
                print("\nYou are about to have the ship dock with your ship when you hear something over the")
                print("\nradio saying \"We are the last of The Tau Ceti's please do not fire we are the last hope...\"")
                print("\nYou dock with the ship...")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou ask The Polarians to check it out.They get closer to the pod when a radio signal")
                print("\ncomes over saying \"We are the last of The Tau Ceti's please do not fire we are the last")
                print("\nhope...\" You try to radio The Polarians to let them know when they fire a missle at the ")
                print("\npod and it explodes...")
                input("\nPress Enter to try again...")
                continue

        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nYou just docked with the pod and you make your way to on the pod to investigate more.")
            print("\nYou get on the podand you are greated by two Tau Ceti's. They are humonoid with")
            print("\nsome ridges around their noses.They tell you about how this ship was designed years")
            print("\nback as a last resort in case this battle wasnt wont but The Tau Ceti's. You go look ")
            print("\naround the pod and you find a huge cold storage room!Looking closer you see that they")
            print("\nhave embrio's in there! This was a population bomb! They will look for another habitable")
            print("\nworld and seed it with the embroys they have in artifical incubation that they have in a")
            print("\nanother huge room!It looks like these two Tau Ceti's were choosen to be their last hope.")
            print("\nAnd we have just captured them... their fate is now tied to the decisions of the human")
            print("\n and The Polarians... That will not end well...")
            print("\n\t1.Take control of the pod")
            print("\n\t2.Try to reason with your Captian")
            print("\n\t3.Talk with The Tau Ceti's")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou take control over the pod to make sure that they dont get hurt by anybody.You")
                print("\nrelease the pod from the ship and shoot it off far from here so The Tau Ceti's can")
                print("\ncomplete their mission of repopulating their species.They make it far from here")
                print("\nwhen the Captian catches you ask throws you in the brig.")
                input("\nPress Enter to try again...")
                continue
            elif success == 2:
                print("\nYou try to reason with your Captian by explaining they need to finish their mission and")
                print("\nwe cant let that fate be choosen by us or anybody from home.The Captian says \"This")
                print("\nchoice is above our heads and we have to take them back home with us.\" You cant take")
                print("\nthis and you get thrown in the brig so you dont do anything crazy.")
                input("\nPress Enter to try again...")
                continue
            elif success == 3:
                print("\nYou decide to go talk with The Tau Ceti's and they tell you a story about how they were")
                print("\nchoosen years ago to lead this mission and they knew they would be giving up everything")
                print("\nfor this mission.You continue to talk with them...")
                input("\nPress Enter to continue...")
                break

        while True:
            print("\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 7**************************************************")
            print("\nYou are talking with The Tau Ceti's and they knew they would be the last two living Tau Ceti's")
            print("\nif they failed. Now they are here and they have a planet in mind. A planet not to dissimalar from")
            print("\ntheir homeworld. They explain how they did not start this war. The Polarians fired first")
            print("\nand then brought in Earth decades ago. Ever since they have been at war... they did not ")
            print("\nwant to attack Earth they only wanted to fight The Polarians. They just confirmed what")
            print("\nyou have been thinking this whole time! They wanted the human race to make the decision ")
            print("\nfor themselves if they wanted to be brought in this war. You talk with them for what seems")
            print("\nlike hours! They ask you one simple question would you like to join us?")
            print("\n\t1.Join them")
            print("\n\t2.Return home")
            print("\n\t3.Ask your friends opinion")
            try:
                success = int(input("\nChoose an option (1, 2, or 3): "))
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success < 1 or success > 3:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                continue
            if success == 1:
                print("\nYou want to join them on this journey to repopulate their species. You go back to your ship to")
                print("\ngather your things and tell your Captian what you are about to do and why. Just as you ")
                print("\nget on the ship you are stoped by your friend " + recalledPerson + " and he says")
                print("\n\"What is going on? You are acting funny.\" You tell him to follow you. Both of you go to the brige")
                print("\nand ask the Captian to join you. You sit them down and explain to them what all The Tau Ceti's")
                print("\nhave told them about how they did not want to fight Earth. Your Captian looks shocked! ")
                print("\nYou explain to both of them that you need to join them to help them right this wrong of Earth.")
                print("\n" + recalledPerson + " is sitting there very quiet.Your Captian agrees you need to ")
                print("\ndo this and gives you the go ahead. You leave with your friend and they say " + recalledPerson)
                print("\n\"What are you thinking? You need to come home...\" You explain that you will come home once ")
                print("\nThe Tau Ceti's are thriving. They tell you \"Okay I understand. I will tell your family on ")
                print("\nEarth what you have done and why. They will understand. I am going to miss you. Maybe I will see you")
                print("\nin space before you know it...\" You give your friend a hug and say goodbye to them.")
                input("\nPress Enter to continue...")
                break
            elif success == 2:
                print("\nYou want to return home so you go back to the ship and go to your bunk. When you are")
                print("\nstopped by your friend " + recalledPerson + ". They say \"Whats going on?\" You ")
                print("\nexplain to them that The Tau Ceti's didnt want to fight with us they were just after")
                print("\nThe Polarians. This confirmes your theory. Your friend says \"You need to take this")
                print("\nmission. You need to go with them to help repopulate. This is the only way we can know")
                print("\nforsure that they will be okay\" You think this over very hard! Then you see the logic in")
                print("\nwhat your friend is saying. You need to go... You and your friend go the bridge to talk")
                print("\nwith the Captian. You sit him down and explain to him what all The Tau Ceti's have told")
                print("\nyou over the past few hours. The Captian is shocked! He thinks for awhile and then says")
                print("\n\"You need to go... I will aprove everything and relay this to Earth.\" You thank him and")
                print("\nwalk out of the room. " + recalledPerson + " says \"I understand what you are trying to")
                print("\ndo. You need to go. I will let your family know on Earth what happened and why you made")
                print("\nthis choice. They will understand. I am oging to miss you!\" You give your friend a hug")
                print("\nand say goodbye to them.")
                input("\nPress Enter to continue...")
                break
            elif success == 3:
                print("\nYou go ask your friend what you should do? You go back into the ship and find ")
                print("\n" + recalledPerson + " waiting to greet you! You ask tell them everything that just happened")
                print("\nand he is shocked! You ask what you should do? They reply with \"You need to do this.")
                print("\nThis will be an amazing journey and help undo a wrong that Earth did.\" You agree with")
                print("\nwhat they said. You say \"Okay you are right. Lets go to the bridge to inform the ")
                print("\nCaptian.\" You both make your way to the bridge and ask the Captian to join you in ")
                print("\na private room. You are all sitting down and you explain to the Captian everything that")
                print("\nthe Tau Ceti's just told you! He sits there in shock! He says \"I think this is a hard")
                print("\nchoice but I think that you should go. We need to undo this and I think that you can ")
                print("\nhelp a lot with this. I will clear it with Earth later. You should go...\" You agree and")
                print("\nboth you and your friend get up and leave. " + recalledPerson + " stops you as you ")
                print("\nabout to leave. and says \" I understand why you are doing this and I think it is the ")
                print("\nright choice. This will be hard on your family but I will explain to them everything that")
                print("\nhas happened and why you are doing this. They will understand. I am going to miss you")
                print("\nvery much!\" You give your friend a hug and say goodbye to them. ")
                input("\nPress Enter to continue...")
                break

        print("\n\n\n\n**************************************************Chapter 7***************************************************")
        print("\nYou set off into deep space with The Tau Ceti's on your way to repopulate another world! You miss home")
        print("\nbut you know this needs to be done and they will be proud in the end...")
        input("\nPress Enter to continue...")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*.    .      ..    .* .    .* . .* .*	 .* .*	.** .   .  ..** .   . ..** .   .  .    ..** .   .  .    ...** .")
        print("\n.* .** .   ..** .   .  .    . .* .*	   ..    .* .    .* . .* .*	 .* .*	.** .   ...** .   .  .    ...** .  ")
        print("\n.  .* .* ..** .   .  .    ...** .   .  .    .** .   ..** .   ...** .   .  .    ...** .    ...** .    ...** .  ")
        print("\n	.   .* .*	.   .* .* .* .*	.** .   ..** .   . ..** .   .  .    ..** .   .  .    ...** .    ...** .    ...*")
        print("\n.** .   .  .    ..** .   . ..** .   .  .      ..** .   . ..** .   .  .    ..** .   .  .    ...** .    ...** . ")
        print("\n.   .** . .* . .* . .* . .* ...** .   .  .      ..** .   . ..** .   .  .   ..** .   .  .    ...** .     .")
        print("\n* .    .* . .* . .* . .* ...** .   .  .      ..** .   . ..** .   .  .    ..** .   .  .    ...** .    ...** .  ")
        print("\n.    .* .    .* . .* . .* . .* .*	   ..    .* .    .* . .* .*	 .* .*	.** .   ...** .   .  .    ...** .    ..")
        print("\nThank you for playing this game. Hope you enjoyed it! There is more to come with this story... More games")
        print("\nto come! But... there is still more to this game! Please continue to the secret CHAPTER 8!!!")
        input("\nPress Enter to continue to Chapter 8...")
        chapter8.Game().chapter8()
        return True


if __name__ == "__main__":
    game = Game()
    game.chapter7()


