#!/usr/bin/env python3

# GUI-ohjelma SQLite-tietokannan tarkasteluun
# - Valitse tietokantatiedosto
# - Näe taulut listassa
# - Klikkaa taulua → data näkyy taulukossa

import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

try:
    import pandas as pd
except ImportError:
    print("Pandas ei ole asennettu. Asenna: pip install pandas")
    raise


class DatabaseViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite-tietokannan selain")

        self.conn = None

        # --- Yläosan napit ---
        top_frame = tk.Frame(root)
        top_frame.pack(fill=tk.X, padx=5, pady=5)

        self.open_btn = tk.Button(top_frame, text="Avaa tietokanta", command=self.open_database)
        self.open_btn.pack(side=tk.LEFT)

        # --- Taululista ---
        left_frame = tk.Frame(root)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(left_frame, text="Taulut").pack()

        self.table_listbox = tk.Listbox(left_frame, width=25)
        self.table_listbox.pack(fill=tk.Y, expand=True)
        self.table_listbox.bind("<<ListboxSelect>>", self.on_table_select)

        # --- Data näkymä ---
        right_frame = tk.Frame(root)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.tree = ttk.Treeview(right_frame)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbarit
        vsb = ttk.Scrollbar(right_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(right_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscroll=vsb.set, xscroll=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)

    def create_connection(self, db_file):
        """Luo yhteys tietokantaan"""
        try:
            return sqlite3.connect(db_file)
        except Error as e:
            messagebox.showerror("Virhe", f"Yhteys epäonnistui:\n{e}")
            return None

    def get_table_names(self):
        """Hakee taulujen nimet"""
        query = """
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%';
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def read_table(self, table_name):
        """Lukee taulun DataFrameen"""

        # HUOM: SQL-injektioriski teoriassa, mutta tässä turvallinen:
        # - taulun nimet tulevat tietokannasta, ei käyttäjän syötteestä
        sql = f"SELECT * FROM {table_name}"
        return pd.read_sql_query(sql, self.conn)

    def open_database(self):
        """Avaa tiedostovalitsin"""
        file_path = filedialog.askopenfilename(
            filetypes=[("SQLite database", "*.db *.sqlite *.sqlite3"), ("All files", "*.*")]
        )

        if not file_path:
            return

        # Sulje vanha yhteys
        if self.conn:
            self.conn.close()

        self.conn = self.create_connection(file_path)
        if self.conn is None:
            return

        # Päivitä taululista
        self.table_listbox.delete(0, tk.END)

        tables = self.get_table_names()
        if not tables:
            messagebox.showinfo("Info", "Tietokannassa ei ole tauluja.")
            return

        for table in tables:
            self.table_listbox.insert(tk.END, table)

    def on_table_select(self, event):
        """Kun käyttäjä valitsee taulun"""
        if not self.conn:
            return

        selection = self.table_listbox.curselection()
        if not selection:
            return

        table_name = self.table_listbox.get(selection[0])

        try:
            df = self.read_table(table_name)
            self.show_dataframe(df)
        except Error as e:
            messagebox.showerror("Virhe", f"Taulun lukeminen epäonnistui:\n{e}")

    def show_dataframe(self, df):
        """Näyttää DataFramen Treeviewissä"""

        # Tyhjennä vanha sisältö
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        # Aseta sarakkeet
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="w", width=120)

        # Tyhjän taulun käsittely
        if df.empty:
            return

        # Lisää rivit
        for _, row in df.iterrows():
            self.tree.insert("", tk.END, values=list(row))


def main():
    root = tk.Tk()
    app = DatabaseViewer(root)
    root.geometry("800x500")
    root.mainloop()


if __name__ == "__main__":
    main()


# ==========================================================
# SQL-INJEKTIO (OPETUSHUOMIO)
# ==========================================================
#
# Jos käyttäjä saisi kirjoittaa taulun nimen itse:
#
#   table_name = input("Anna taulu: ")
#   sql = f"SELECT * FROM {table_name}"
#
# → vaarallista!
#
# Tässä ohjelmassa turvallisuus perustuu siihen, että:
# - taulujen nimet tulevat tietokannasta (ei käyttäjältä)
#
# Turvallisempi malli:
#
#   allowed = get_table_names()
#   if table_name not in allowed:
#       raise ValueError("Virheellinen taulu")
#
# Ja muistutus:
# - parametrisoidaan arvot aina:
#
#   cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
#
# ==========================================================