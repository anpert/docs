#!/usr/bin/env python3

# Tämä ohjelma:
# 1. Avaa yhteyden SQLite-tietokantaan
# 2. Hakee kaikki käyttäjän luomat taulut
# 3. Lukee jokaisen taulun pandas DataFrameen
# 4. Tulostaa tiedot siististi taulukkomuodossa

import sqlite3
from sqlite3 import Error

# Yritetään tuoda pandas-kirjasto
try:
    import pandas as pd
except ImportError:
    print("Pandas ei ole asennettu. Asenna se komennolla: pip install pandas")
    raise


def create_connection(db_file):
    """
    Luo yhteys SQLite-tietokantaan.
    Palauttaa connection-olion tai None virhetilanteessa.
    """
    try:
        return sqlite3.connect(db_file)
    except Error as e:
        print(f"Yhteyden luominen epäonnistui: {e}")
        return None


def get_table_names(conn):
    """
    Hakee kaikki käyttäjän luomat taulut tietokannasta.
    Suodattaa pois SQLite:n sisäiset taulut (sqlite_%).
    """
    query = """
    SELECT name 
    FROM sqlite_master 
    WHERE type='table' AND name NOT LIKE 'sqlite_%';
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return [row[0] for row in cursor.fetchall()]


def read_table(conn, table_name):
    """
    Lukee yhden taulun pandas DataFrameen.
    """
    # HUOM: Tämä käyttää f-stringiä → teoriassa SQL-injektioriski,
    # mutta tässä turvallinen, koska taulujen nimet tulevat tietokannasta.
    sql = f"SELECT * FROM {table_name}"
    return pd.read_sql_query(sql, conn)


def main():
    # Tietokantatiedoston nimi
    database = r"pythonsqlite.db"

    # Asetetaan pandas näyttämään enemmän dataa (tarvittaessa)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # Käytetään context manageria → yhteys sulkeutuu automaattisesti
    conn = create_connection(database)
    if conn is None:
        print("Virhe! Yhteyttä ei voitu muodostaa.")
        return

    try:
        tables = get_table_names(conn)

        if not tables:
            print("Tietokannassa ei ole tauluja.")
            return

        # Käydään kaikki taulut läpi
        for table in tables:
            df = read_table(conn, table)

            # Tyhjän taulun käsittely
            if df.empty:
                print(f"\nTaulu: {table} (ei rivejä)")
            else:
                print(f"\nTaulu: {table}")
                print(df.to_string(index=False))

    except Error as e:
        print(f"Tietojen lukeminen epäonnistui: {e}")

    finally:
        conn.close()


if __name__ == '__main__':
    main()


# ==========================================================
# SQL-INJEKTIO (OPETUSOSIO – EI KÄYTÖSSÄ TÄSSÄ OHJELMASSA)
# ==========================================================
#
# Ongelma:
# Jos käyttäjä voisi syöttää taulun nimen, tämä olisi vaarallista:
#
#   table_name = input("Anna taulun nimi: ")
#   sql = f"SELECT * FROM {table_name}"
#
# Käyttäjä voisi syöttää:
#   users; DROP TABLE users;
#
# → Tämä voisi tuhota tietokannan.
#
# Ratkaisu:
# SQLite ei tue parametrisoituja taulun nimiä suoraan, joten:
#
# 1. Sallitut arvot whitelistataan:
#
#   allowed_tables = get_table_names(conn)
#   if table_name not in allowed_tables:
#       raise ValueError("Virheellinen taulu")
#
# 2. Käytetään vain luotettua dataa (kuten tässä ohjelmassa)
#
# 3. Parametrisoidaan aina arvot (EI taulun nimiä):
#
#   cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
#
# Yhteenveto:
# - Älä koskaan luota käyttäjän syötteeseen SQL:ssä
# - Käytä parametreja aina kun mahdollista
# - Taulujen ja sarakkeiden nimet: whitelist
#
# ==========================================================