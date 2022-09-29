from tkinter import *
from tkinter import ttk


class FeetToMeters:
    def __init__(self, root):
        root.title("Feet to Meters")

        # A frame widget, which holds the contents of our user interface
        mainframe = ttk.Frame(root, padding="10 10 20 20")
        mainframe.grid(column=0, row=0, sticky=N + W + E + S)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # The entry widget to input the number of feet to convert
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=W + E)

        # Display the resulting number of meters that we calculate
        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=W + E)

        # Our 'Calculate' button is here
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        # The remaining labels
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # Polishing
        # Adds a bit of padding around each widget, so they aren't so scrunched together
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Puts the focus on our entry widget
        feet_entry.focus()
        # Program will react when the "Enter" key has been pressed
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(str(int(0.3048 * value * 10000.0 + 0.5) / 10000.0))
        except ValueError:
            self.meters.set("Invalid input!")


if __name__ == '__main__':
    main = Tk()
    FeetToMeters(main)
    main.mainloop()
