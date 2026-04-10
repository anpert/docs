import sqlite3

DB_NAME = 'esimerkki.db'

def luo_taulu():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS opiskelijat (
        id INTEGER PRIMARY KEY,
        nimi TEXT,
        ika INTEGER
    )
    ''')
    conn.commit()
    conn.close()

def lisaa_opiskelija():
    nimi = input("Anna nimi: ")
    ika = input("Anna ikä: ")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO opiskelijat (nimi, ika) VALUES (?, ?)", (nimi, ika))
    conn.commit()
    conn.close()
    print(f"{nimi} lisätty onnistuneesti!")

def nayta_opiskelijat():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM opiskelijat")
    rivit = cur.fetchall()
    if rivit:
        print("ID | Nimi | Ikä")
        print("----------------")
        for rivi in rivit:
            print(f"{rivi[0]} | {rivi[1]} | {rivi[2]}")
    else:
        print("Ei opiskelijoita tietokannassa.")
    conn.close()

def poista_opiskelija():
    id_poisto = input("Anna poistettavan opiskelijan ID: ")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM opiskelijat WHERE id = ?", (id_poisto,))
    conn.commit()
    conn.close()
    print(f"Opiskelija ID {id_poisto} poistettu (jos löytyi).")

def menu():
    while True:
        print("\nValitse toiminto:")
        print("1 - Lisää opiskelija")
        print("2 - Näytä kaikki opiskelijat")
        print("3 - Poista opiskelija")
        print("0 - Lopeta")
        valinta = input("Valintasi: ")

        if valinta == "1":
            lisaa_opiskelija()
        elif valinta == "2":
            nayta_opiskelijat()
        elif valinta == "3":
            poista_opiskelija()
        elif valinta == "0":
            print("Ohjelma suljetaan.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

if __name__ == "__main__":
    luo_taulu()
    menu()