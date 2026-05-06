# Käyttää tkinter-graafista käyttöliittymää
# Näyttää numeronäytön, numeropainikkeet, +, =, ja C
# Tekee yhteenlaskun
# Rakenne on laajennettavissa myöhemmille laskutoiminnoille

# käynnistä python .\laskin_1.py

import tkinter as tk
from tkinter import ttk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yksinkertainen laskin")
        self.root.resizable(False, False)

        self.expression = ""
        self.total = 0
        self.operator = None

        self.display_var = tk.StringVar(value="0")
        self._create_widgets()

    def _create_widgets(self):
        display = ttk.Entry(self.root, textvariable=self.display_var, justify="right", font=("Segoe UI", 20), state="readonly")
        display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=8, pady=8)

        # näppäimet ladotaan vasemmalta oikealle, ylhäältä alas.
        # neljä saraketta (colmunspan)
        buttons = [
            ("7", self._append_digit),
            ("8", self._append_digit),
            ("9", self._append_digit),
            ("C", self._clear),
            ("4", self._append_digit),
            ("5", self._append_digit),
            ("6", self._append_digit),
            ("+", self._set_operator),
            ("-", self._set_operator),          # lisä
            ("1", self._append_digit),
            ("2", self._append_digit),
            ("3", self._append_digit),
            ("=", self._calculate),
            ("0", self._append_digit),
        ]

        row = 1
        col = 0
        for text, command in buttons:
            button = ttk.Button(self.root, text=text, command=lambda t=text, c=command: c(t))
            # button.grid(row=row, column=col, sticky="nsew", padx=4, pady=4, ipadx=10, ipady=10)   # seur. pady vaihdettu 4->5
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=4, ipadx=10, ipady=10)
            col += 1
            if col > 3:                     # 3, jolloin 4 nappeja rinnakkain
                col = 0
                row += 1

        for i in range(5):                  # lisä, oli 4
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(row + 1):
            self.root.grid_rowconfigure(i, weight=1)

    def _append_digit(self, digit):
        if self.expression == "0":
            self.expression = digit
        else:
            self.expression += digit
        self.display_var.set(self.expression)

    def _set_operator(self, operator):
        if not self.expression:
            return

        current_value = int(self.expression)
        if self.operator is None:
            self.total = current_value
        else:
            self.total += current_value

        self.operator = operator
        self.expression = ""
        self.display_var.set(str(self.total))

    def _calculate(self, _=None):
        if not self.expression:
            return

        current_value = int(self.expression)
        if self.operator == "+":
            self.total += current_value
        elif self.operator == "-":                  # lisä
            self.total -= current_value             # lisä
        else:
            self.total = current_value

        self.expression = str(self.total)
        self.operator = None
        self.display_var.set(self.expression)

    def _clear(self, _=None):
        self.expression = ""
        self.total = 0
        self.operator = None
        self.display_var.set("0")


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

