# tee ohjelma, joka lisää uusia henkilöitä tauluun
# kysyy etu- ja sukunimen sekä sähköpostiosoitteen
# tämän jälkeen annetaan numeroitu lista työpaikoista (pelkkä työpaikan nimi)
# tietojen täyttäjä valitsee työpaikan
# tietojen täyttäjä voi myös lisätä uuden työpaikan

#!/usr/bin/env python3
"""
Ohjelma uusien henkilöiden lisäämiseksi tietokantaan.
Käyttäjä voi valita olemassa olevan työpaikan tai lisätä uuden.
"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    try:
        return sqlite3.connect(db_file)
    except Error as e:
        print(f"Yhteyden luominen epäonnistui: {e}")
        return None


def get_workplaces(conn):
    """Get all workplaces from the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nimi FROM tyopaikat ORDER BY nimi")
        return cursor.fetchall()
    except Error as e:
        print(f"Virhe työpaikkojen hakemisessa: {e}")
        return []


def display_workplaces(workplaces):
    """Display numbered list of workplaces."""
    print("\nValitse työpaikka:")
    for i, (workplace_id, name) in enumerate(workplaces, 1):
        print(f"{i}. {name}")
    print(f"{len(workplaces) + 1}. Lisää uusi työpaikka")


def add_new_workplace(conn):
    """Add a new workplace to the database."""
    name = input("Anna uuden työpaikan nimi: ").strip()
    if not name:
        print("Työpaikan nimi ei voi olla tyhjä.")
        return None

    address = input("Anna työpaikan osoite: ").strip()
    if not address:
        print("Työpaikan osoite ei voi olla tyhjä.")
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tyopaikat (nimi, osoite) VALUES (?, ?)", (name, address))
        conn.commit()
        workplace_id = cursor.lastrowid
        print(f"✓ Uusi työpaikka '{name}' lisätty tietokantaan.")
        return workplace_id
    except Error as e:
        print(f"Virhe uuden työpaikan lisäämisessä: {e}")
        conn.rollback()
        return None


def add_new_user(conn, name, email, workplace_id):
    """Add a new user to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, tyopaikka) VALUES (?, ?, ?)",
                      (name, email, workplace_id))
        conn.commit()
        print(f"✓ Käyttäjä '{name}' lisätty tietokantaan.")
        return True
    except Error as e:
        print(f"Virhe käyttäjän lisäämisessä: {e}")
        conn.rollback()
        return False


def get_user_input():
    """Get user input for name and email."""
    while True:
        name = input("Anna henkilön koko nimi (etu- ja sukunimi): ").strip()
        if name:
            break
        print("Nimi ei voi olla tyhjä.")

    while True:
        email = input("Anna sähköpostiosoite: ").strip()
        if email and "@" in email:
            break
        print("Anna kelvollinen sähköpostiosoite.")

    return name, email


def main():
    database = r"pythonsqlite.db"

    conn = create_connection(database)
    if conn is None:
        print("Error! cannot create the database connection.")
        return

    try:
        # Get user input
        name, email = get_user_input()

        # Get and display workplaces
        workplaces = get_workplaces(conn)
        if not workplaces:
            print("Tietokannassa ei ole työpaikkoja. Lisätään ensimmäinen työpaikka.")
            workplace_id = add_new_workplace(conn)
            if workplace_id is None:
                return
        else:
            display_workplaces(workplaces)

            # Get user choice
            while True:
                try:
                    choice = int(input("\nValitse numero: "))
                    if 1 <= choice <= len(workplaces):
                        workplace_id = workplaces[choice - 1][0]
                        break
                    elif choice == len(workplaces) + 1:
                        workplace_id = add_new_workplace(conn)
                        if workplace_id is None:
                            return
                        break
                    else:
                        print(f"Valitse numero 1-{len(workplaces) + 1}.")
                except ValueError:
                    print("Anna numero.")

        # Add the user
        if add_new_user(conn, name, email, workplace_id):
            print("\n✓ Henkilö lisätty onnistuneesti!")

    finally:
        conn.close()


if __name__ == '__main__':
    main()

