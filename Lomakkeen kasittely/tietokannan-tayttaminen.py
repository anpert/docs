#!/usr/bin/env python3
"""
Ohjelma, joka täyttää tietokantaa tietueilla.
Lisää 10 työpaikkaa ja 15 käyttäjää tietokantaan.
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


def insert_tyopaikat(conn):
    """Insert 10 workplaces into tyopaikat table."""
    workplaces = [
        ("Acme Corp", "Helsingin katu 1, 00100 Helsinki"),
        ("Tech Solutions", "Teknologiakatu 5, 02150 Espoo"),
        ("Design Studio", "Taiteellinen tie 10, 02200 Espoo"),
        ("Logistics Plus", "Kuljetusvaaratie 3, 01510 Vantaa"),
        ("Marketing Agency", "Mainosväylä 7, 00200 Helsinki"),
        ("Finance & Co", "Rahaväylä 2, 00500 Helsinki"),
        ("Construction Ltd", "Rakennuspolku 12, 01200 Vantaa"),
        ("Software House", "Koodiväylä 8, 02100 Espoo"),
        ("Legal Services", "Lakimiehentie 4, 00600 Helsinki"),
        ("HR Solutions", "Henkilöstötalo 6, 02600 Espoo"),
    ]

    sql = "INSERT INTO tyopaikat (nimi, osoite) VALUES (?, ?)"
    cursor = conn.cursor()

    try:
        cursor.executemany(sql, workplaces)
        conn.commit()
        print(f"✓ Lisätty {cursor.rowcount} työpaikkaa tietokantaan")
    except Error as e:
        print(f"Virhe työpaikkojen lisäämisessä: {e}")
        conn.rollback()


def insert_users(conn):
    """Insert 15 users into users table."""
    users = [
        ("Matti Meikäläinen", "matti.meikalainen@email.com", 1),
        ("Liisa Virtanen", "liisa.virtanen@email.com", 1),
        ("Jukka Ahonen", "jukka.ahonen@email.com", 2),
        ("Anna Karvonen", "anna.karvonen@email.com", 2),
        ("Petteri Salo", "petteri.salo@email.com", 3),
        ("Katja Mäki", "katja.maki@email.com", 3),
        ("Mikko Lahtinen", "mikko.lahtinen@email.com", 4),
        ("Sanna Raitanen", "sanna.raitanen@email.com", 4),
        ("Timo Virtala", "timo.virtala@email.com", 5),
        ("Laura Nissinen", "laura.nissinen@email.com", 5),
        ("Jari Mäkelä", "jari.makela@email.com", 6),
        ("Emma Kaunisto", "emma.kaunisto@email.com", 6),
        ("Pekka Nikkinen", "pekka.nikkinen@email.com", 7),
        ("Riikka Peltonen", "riikka.peltonen@email.com", 8),
        ("Ville Koskinen", "ville.koskinen@email.com", 9),
    ]

    sql = "INSERT INTO users (name, email, tyopaikka) VALUES (?, ?, ?)"
    cursor = conn.cursor()

    try:
        cursor.executemany(sql, users)
        conn.commit()
        print(f"✓ Lisätty {cursor.rowcount} käyttäjää tietokantaan")
    except Error as e:
        print(f"Virhe käyttäjien lisäämisessä: {e}")
        conn.rollback()


def is_database_populated(conn):
    """Check if the database already contains data."""
    try:
        cursor = conn.cursor()
        
        # Check users table
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        # Check tyopaikat table
        cursor.execute("SELECT COUNT(*) FROM tyopaikat")
        workplace_count = cursor.fetchone()[0]
        
        return user_count > 0 and workplace_count > 0
    except Error as e:
        print(f"Virhe tietojen tarkistamisessa: {e}")
        return False


def main():
    database = r"pythonsqlite.db"

    conn = create_connection(database)
    if conn is None:
        print("Error! cannot create the database connection.")
        return

    try:
        # Check if database is already populated
        if is_database_populated(conn):
            print("⚠️  Tietokanta on jo täytetty!")
            print("Ohjelma pysäytettiin estämään duplikaattien luominen.")
            print("\nJos haluat uudet tiedot, poista pythonsqlite.db-tiedosto")
            print("ja aja ensin tietokannan_luominen.py uudelleen.")
            return
        
        print("Täytetään tietokantaa...\n")
        insert_tyopaikat(conn)
        insert_users(conn)
        print("\n✓ Tietokanta täytetty onnistuneesti!")
    finally:
        conn.close()


if __name__ == '__main__':
    main()

