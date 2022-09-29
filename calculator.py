from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys


class Calculator:
    def __init__(self, root):
        self.root = root
        self.button_list = [
            "%", "C", "Backspace", "Exit",
            "1/x", "xⁿ", "sin", "cos",
            "2√x", "|x|", "e", "π",
            "(", ")", "n!", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "±", "0", ".", "=", ]

        self.root.geometry("364x312")  # this is for the size of the window
        self.root.resizable(False, False)  # this is to prevent from resizing the window
        self.root.title("Calculator")

        # First Label
        self.greeting = ttk.Label(self.root, text="Supports keyboard input!")
        self.greeting.pack(side=TOP)

        # Main Frame for our Input
        self.input_frame = Frame(self.root, width=312, height=50, bd=0, highlightbackground="black",
                                 highlightcolor="black",
                                 highlightthickness=2)
        self.input_frame.pack(side=TOP)

        # Second Label
        self.warning = ttk.Label(self.root, text="Only one operation per time!")
        self.warning.pack(side=TOP)

        # Input
        self.calc_entry = Entry(self.input_frame, width=33)
        self.calc_entry.grid(row=0, column=0, columnspan=5)
        self.calc_entry.pack(ipady=10, ipadx=10)
        self.calc_entry.focus()
        self.root.bind("<Return>", self.calc)

        # Buttons
        self.btn_frame = Frame(self.root, width=312, height=272.5, bg="grey")
        self.btn_frame.pack()

        self.layout()

    # Logic
    def calc(self, key):
        try:
            if key == "=" or key.type == '2':
                # Check spelling
                str1 = "-+0123456789.*/)("
                for char in self.calc_entry.get():
                    if char not in str1:
                        messagebox.showerror("Error!", "Only numbers and basic mathematical symbols are accepted!")
                        break
                else:
                    # Calculations
                    try:
                        result = eval(self.calc_entry.get())
                        self.calc_entry.insert(END, "=" + str(result))
                    except ZeroDivisionError:
                        messagebox.showerror("Error!", "Unable to divide by zero!")
                    except:
                        messagebox.showerror("Error!", "Check the correctness of data!")

            elif key == "C":
                self.calc_entry.delete(0, END)

            elif key == "±":
                if "=" in self.calc_entry.get():
                    self.calc_entry.delete(0, END)
                try:
                    if self.calc_entry.get()[0] == "-":
                        self.calc_entry.delete(0)
                    else:
                        self.calc_entry.insert(0, "-")
                except IndexError:
                    pass

            elif key == "π":
                self.calc_entry.insert(END, str(math.pi))

            elif key == "e":
                self.calc_entry.insert(END, str(math.e))

            elif key == "Exit":
                self.root.after(1, self.root.destroy)
                sys.exit()

            elif key == "Backspace":
                temp = len(self.calc_entry.get())
                self.calc_entry.delete(temp - 1, END)

            elif key == "xⁿ":
                self.calc_entry.insert(END, "**")

            elif key == "sin":
                self.calc_entry.insert(END, "=" + str(math.sin(int(self.calc_entry.get()))))

            elif key == "cos":
                self.calc_entry.insert(END, "=" + str(math.cos(int(self.calc_entry.get()))))

            elif key == "(":
                self.calc_entry.insert(END, "(")

            elif key == ")":
                self.calc_entry.insert(END, ")")

            elif key == "n!":
                self.calc_entry.insert(END, "=" + str(math.factorial(int(self.calc_entry.get()))))

            elif key == "2√x":
                self.calc_entry.insert(END, "=" + str(math.sqrt(int(self.calc_entry.get()))))

            elif key == "|x|":
                self.calc_entry.insert(END, "=" + str(math.fabs(int(self.calc_entry.get()))))

            elif key == "%":
                temp = self.calc_entry.get()
                total = ""

                for char in reversed(temp):
                    print(char)
                    try:
                        int(char)
                        total = char + total

                    except:
                        length = len(temp) - len(total)
                        temp = temp[:length]
                        self.calc_entry.delete(0, END)
                        self.calc_entry.insert(END, temp + str(int(total) / 100))
                        break

                    else:
                        self.calc_entry.delete(0, END)
                        self.calc_entry.insert(END, str(int(total) / 100))

            elif key == "1/x":
                temp = self.calc_entry.get()
                self.calc_entry.delete(0, END)
                self.calc_entry.insert(END, "1/" + temp + "=" + str(1 / int(temp)))

            else:
                if "=" in self.calc_entry.get():
                    self.calc_entry.delete(0, END)
                self.calc_entry.insert(END, key)

        except ZeroDivisionError:
            messagebox.showerror("Error!", "Unable to divide by zero!")

        except ValueError:
            messagebox.showerror("Error!", "Only numbers and basic mathematical symbols are accepted!")

        except:
            messagebox.showerror("Error!", "Check the correctness of data!")

    # Layout for the buttons
    def layout(self):
        row = 1
        col = 0
        for i in self.button_list:
            ttk.Button(self.btn_frame, text=i, command=lambda x=i: self.calc(x), width=10).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1


if __name__ == '__main__':
    main = Tk()
    Calculator(main)
    main.mainloop()
