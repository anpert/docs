import sqlite3

DB_NAME = 'esimerkki.db'
DUMP_FILE = 'C:\\Users\\antti.perttunen\\OneDrive - Ammattiopisto Luovi\\Paikalliset tiedostot\\koodaus\\sqlite\\esimerkki_dump.sql'

conn = sqlite3.connect(DB_NAME)

with open(DUMP_FILE, 'w', encoding='utf-8') as f:
    for rivi in conn.iterdump():
        f.write(rivi + '\n')

conn.close()
print(f"SQL-dump luotu tiedostoon {DUMP_FILE}")