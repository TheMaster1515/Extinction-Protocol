import cv2
import time
import chapter2Earth
import chapter2Moon

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


    def Chapter2Earth(self):
        game = chapter2Earth.Game()
        return game.Chapter2Earth()

    def Chapter2Moon(self):
        game = chapter2Moon.Game()
        return game.Chapter2Moon()

    def chapter2(self):
        recalledName, recalledAge, recalledColony = self.recallCharacterData("files/data.txt")
        recalledPerson, recalledShip = self.recallCharacterWork("files/character.txt")
        recalledJob = self.recallCharacterJob("files/job.txt")
        print("Here is your character's information")
        print(f"Name: {recalledName}")
        print(f"Age: {recalledAge}")
        print(f"Colony: {recalledColony}")
        print("Job: !!!Classified!!!")
        input("\nPress Enter To Continue...")
        imagePath = "images/Chapter_2.jpg"
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
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n        ****   ****")
        print("\n        ****   ****")
        print("\n       ****** ******")
        print("\n     *****************")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLANDING IN 5... ")
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
        print("\nLANDING IN 4...")
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
        print("\nLANDING IN 3...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n          | / \\ |")
        print("\n         _|_____|_")
        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n        ****   ****")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLANDING IN 2....")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n           / _ \\")
        print("\n          | / \\ |")
        print("\n         _|_____|_")
        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n        |  |   |  |")
        print("\n________________________________________________________________________________________________________________________")
        print("\nLANDING IN 1...")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________________________________________________________________________________________")
        print("\n            / \\")
        print("\n           / _ \\")
        print("\n          | / \\ |")
        print("\n         _|_____|_")

        print("\n       .' |     | '.")
        print("\n      /   |     |   \\ ")
        print("\n      |_____________| ")
        print("\n________________________________________________________________________________________________________________________")
        input("\nPress Enter to continue...")
        while True:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**************************************************Chapter 2***************************************************")
            print(f"\nYou are at MEPS and you and your friend get separated. They are doing all sorts of checks on you.")  # Enter the question here
            print("\nNow you are just about done and you wonder what job will they have you doing?")
            print(f"\nThey state you are from {recalledColony} so these are your choices of jobs.")
            print("\n\t1.Pilot")                                      #choice 13
            print("\n\t2.Commander")
            print("\n\t3.Recon")
            print("\n\t4.Engineer")
            try:
                success = int(input("\nChoose an option (1, 2, 3, or 4): "))
                if success < 1 or success > 4:
                    raise ValueError
            except ValueError:
                print("\n\tInvalid option. Please enter 1, 2, or 3.")
                time.sleep(3)
                continue
            if success == 1:
                print(f"\nCongrats on picking your job Pilot! Now that you have picked your job {recalledName} and now you have to ")  # Enter answer 1 here
                print("\ngo through basic training and be evaluated to see what is the best fit.")
                print("\nPress Enter to continue...")
                characterJob = "Pilot"
                # save to file
                with open("files/job.txt", "w") as f:
                    f.write(f"Job: {characterJob}\n")
                input()
                self.Chapter2Moon()
            elif success == 2:
                print(f"\nCongrats on picking your job Commander! Now that you have picked your job {recalledName} and now you have to ")  # Enter answer 1 here
                print("\ngo through basic training and be evaluated to see what is the best fit.")
                print("\nPress Enter to continue...")
                characterJob = "Commander"
                with open("files/job.txt", "w") as f:
                    f.write(f"Job: {characterJob}\n")
                input()
                self.Chapter2Moon()
            elif success == 3:
                print(f"\nCongrats on picking your job Recon! Now that you have picked your job {recalledName} and now you have to ")  # Enter answer 1 here
                print("\ngo through basic training and be evaluated to see what is the best fit.")
                print("\nPress Enter to continue...")
                characterJob = "Recon"
                with open("files/job.txt", "w") as f:
                    f.write(f"Job: {characterJob}\n")
                input()
                self.Chapter2Earth()
            elif success == 4:
                print(f"\nCongrats on picking your job Engineer! Now that you have picked your job {recalledName} and now you have to ")  # Enter answer 1 here
                print("\ngo through basic training and be evaluated to see what is the best fit.")
                print("\nPress Enter to continue...")
                characterJob = "Engineer"
                with open("files/job.txt", "w") as f:
                    f.write(f"Job: {characterJob}\n")
                input()
                self.Chapter2Earth()
            break


if __name__ == "__main__":
    game = Game()
    game.chapter2()