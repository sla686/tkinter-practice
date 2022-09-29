from tkinter import *

from calculator import Calculator
from feet_to_meters import FeetToMeters


def main():
    while True:
        print("Choose the app to launch:")
        print("1. Calculator")
        print("2. Feet to Meters")
        print("Type q or quit to exit the program")
        print("Your input: ", end='')
        x = input().lower()
        print()

        if x == '1':
            root = Tk()
            Calculator(root)
            root.mainloop()

        elif x == '2':
            root = Tk()
            FeetToMeters(root)
            root.mainloop()

        elif x == 'q' or x == 'quit':
            break

        else:
            print("Incorrect option!\n")


if __name__ == "__main__":
    main()
