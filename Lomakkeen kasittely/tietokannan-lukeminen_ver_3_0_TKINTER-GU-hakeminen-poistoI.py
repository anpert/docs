#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import pandas as pd


# ==========================================================
# TIETOKANTALOGIIKKA
# ==========================================================

class DatabaseManager:
    def __init__(self):
        self.conn = None

    def connect(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            messagebox.showerror("Virhe", str(e))

    def get_tables(self):
        query = """
        SELECT name FROM sqlite_master
        WHERE type='table' AND name NOT LIKE 'sqlite_%';
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def read_table(self, table_name):
        # turvallinen tässä kontekstissa
        return pd.read_sql_query(f"SELECT * FROM {table_name}", self.conn)

    def search_table(self, table_name, column, value):
        """
        Haku LIKE-operaattorilla
        """
        query = f"SELECT * FROM {table_name} WHERE {column} LIKE ?"
        return pd.read_sql_query(query, self.conn, params=(f"%{value}%",))

    def update_row(self, table, columns, values, where_col, where_val):
        """
        Päivittää yhden rivin
        """
        set_clause = ", ".join([f"{col}=?" for col in columns])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_col}=?"

        cursor = self.conn.cursor()
        cursor.execute(query, values + [where_val])
        self.conn.commit()


# ==========================================================
# GUI
# ==========================================================

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite selain")

        self.db = DatabaseManager()
        self.current_table = None
        self.current_df = None

        self.build_ui()

    # ---------------- UI RAKENNE ----------------

    def build_ui(self):

        # Yläpalkki
        top = tk.Frame(self.root)
        top.pack(fill=tk.X)

        tk.Button(top, text="Avaa tietokanta", command=self.open_db).pack(side=tk.LEFT)

        # Hakukenttä
        self.search_entry = tk.Entry(top)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(top, text="Hae", command=self.search).pack(side=tk.LEFT)

        # Vasen: taulut
        left = tk.Frame(self.root)
        left.pack(side=tk.LEFT, fill=tk.Y)

        self.tables = tk.Listbox(left, width=25)
        self.tables.pack(fill=tk.Y)
        self.tables.bind("<<ListboxSelect>>", self.select_table)

        # Oikea: data
        right = tk.Frame(self.root)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(right)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<Double-1>", self.edit_row)

    # ---------------- TOIMINNOT ----------------

    def open_db(self):
        file = filedialog.askopenfilename(filetypes=[("DB", "*.db *.sqlite")])
        if not file:
            return

        self.db.connect(file)

        self.tables.delete(0, tk.END)
        for t in self.db.get_tables():
            self.tables.insert(tk.END, t)

    def select_table(self, event):
        selection = self.tables.curselection()
        if not selection:
            return

        self.current_table = self.tables.get(selection[0])
        self.current_df = self.db.read_table(self.current_table)

        self.show_df(self.current_df)

    def show_df(self, df):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)
        self.tree["show"] = "headings"

        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for _, row in df.iterrows():
            self.tree.insert("", tk.END, values=list(row))

    # ---------------- HAKU ----------------

    def search(self):
        if self.current_df is None:
            return

        text = self.search_entry.get()
        if not text:
            self.show_df(self.current_df)
            return

        # yksinkertainen: haetaan kaikista sarakkeista
        df = self.current_df[
            self.current_df.apply(lambda row: row.astype(str).str.contains(text, case=False).any(), axis=1)
        ]

        self.show_df(df)

    # ---------------- MUOKKAUS ----------------

    def edit_row(self, event):
        item = self.tree.selection()
        if not item:
            return

        values = self.tree.item(item)["values"]
        columns = self.current_df.columns

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Muokkaa riviä")

        entries = {}

        for i, col in enumerate(columns):
            tk.Label(edit_window, text=col).grid(row=i, column=0)
            e = tk.Entry(edit_window)
            e.insert(0, values[i])
            e.grid(row=i, column=1)
            entries[col] = e

        def save():
            new_values = [entries[col].get() for col in columns]

            # oletetaan ensimmäinen sarake ID:ksi
            id_col = columns[0]
            id_val = values[0]

            try:
                self.db.update_row(
                    self.current_table,
                    columns,
                    new_values,
                    id_col,
                    id_val
                )
                messagebox.showinfo("OK", "Tallennettu")
                edit_window.destroy()

                # päivitä näkymä
                self.current_df = self.db.read_table(self.current_table)
                self.show_df(self.current_df)

            except Exception as e:
                messagebox.showerror("Virhe", str(e))

        tk.Button(edit_window, text="Tallenna", command=save).grid(row=len(columns), column=0, columnspan=2)


# ==========================================================
# MAIN
# ==========================================================

def main():
    root = tk.Tk()
    root.geometry("900x500")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()


# ==========================================================
# TURVALLISUUSHUOMIO (OPETUS)
# ==========================================================
#
# - WHERE-arvot parametrisoitu → OK:
#     WHERE name LIKE ?
#
# - Taulun ja sarakkeen nimet:
#     → pitäisi whitelistata tuotannossa
#
# - UPDATE käyttää parametreja → turvallinen arvojen osalta
#
# ==========================================================