import time
import os
import subprocess
import chapter1
import chapter2
import chapter2Earth
import chapter2Moon
import chapter3
import chapter4
import chapter5
import chapter6
import chapter7
import chapter8

def pause(seconds):
    time.sleep(seconds)

def chapterx():
    while True:
        print("\n\n\n\n" + "*" * 120)
        print("\nChoose which chapter to start on")
        print("\nChoose from the following choices:")
        print("\n\t1.Chapter 1")
        print("\n\t2.Chapter 2")
        print("\n\t2.1.Chapter 2 Earth")
        print("\n\t2.2.Chapter 2 Moon")
        print("\n\t3.Chapter 3")
        print("\n\t4.Chapter 4")
        print("\n\t5.Chapter 5")
        print("\n\t6.Chapter 6")
        print("\n\t7.Chapter 7")
        chapter8_unlocked = os.path.exists("files/chapter8_complete.txt")
        if chapter8_unlocked:
            print("\n\t8.Chapter 8")

        try:
            success = int(input("\nChoose an option (1 through 7): "))
        except ValueError:
            print("\n\tInvalid option. Please enter 1 through 7.")
            pause(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            continue

        if success < 1 or success > 8:
            print("\n\tInvalid option. Please enter 1 through 7.")
            pause(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            continue

        if success == 1:
            game = chapter1.Game()
            game.chapter1()
        elif success == 2:
            game = chapter2.Game()
            game.chapter2()
        elif success == 2.1:
            game = chapter2Earth.Game()
            game.Chapter2Earth()
        elif success == 2.2:
            game = chapter2Moon.Game()
            game.Chapter2Moon()
        elif success == 3:
            game = chapter3.Game()
            game.chapter3()
        elif success == 4:
            game = chapter4.Game()
            game.chapter4()
        elif success == 5:
            game = chapter5.Game()
            game.chapter5()
        elif success == 6:
            game = chapter6.Game()
            game.chapter6()
        elif success == 7:
            game = chapter7.Game()
            game.chapter7()
        elif success == 8:
            if not os.path.exists("files/chapter8_complete.txt"):
                print("\n\tChapter 8 is locked. Complete the game first to unlock it.")
                pause(3)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                continue
            game = chapter8.Game()
            game.chapter8()


        else:
            print("\n\tInvalid option. Please enter 1 through 7.")
            pause(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            continue

if __name__ == "__main__":
    chapterx()