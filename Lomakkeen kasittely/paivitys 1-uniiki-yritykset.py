# päivityskoodi  1
# päivitä niin, että saman yrityksen palveluksessa olevilla on sama yritys-id . poista kaksoiskappaleet.

#!/usr/bin/env python3
"""
Päivityskoodi 1: Poistaa duplikaatit työpaikoista ja päivittää käyttäjien työpaikka-ID:t
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


def remove_duplicate_workplaces(conn):
    """Remove duplicate workplaces and update user references."""
    try:
        cursor = conn.cursor()

        # Find duplicate workplaces by name, keeping the first occurrence
        cursor.execute("""
            SELECT nimi, MIN(id) as keep_id, GROUP_CONCAT(id) as all_ids
            FROM tyopaikat
            GROUP BY nimi
            HAVING COUNT(*) > 1
        """)

        duplicates = cursor.fetchall()

        if not duplicates:
            print("Ei duplikaatteja työpaikoissa.")
            return

        print(f"Löytyi {len(duplicates)} duplikoitua työpaikkaa.")

        for workplace_name, keep_id, all_ids in duplicates:
            duplicate_ids = [int(x) for x in all_ids.split(',') if int(x) != keep_id]

            print(f"Työpaikka '{workplace_name}': säilytetään ID {keep_id}, poistetaan ID:t {duplicate_ids}")

            # Update user references to use the kept workplace ID
            for dup_id in duplicate_ids:
                cursor.execute("""
                    UPDATE users
                    SET tyopaikka = ?
                    WHERE tyopaikka = ?
                """, (keep_id, dup_id))

            # Delete duplicate workplaces
            cursor.execute("""
                DELETE FROM tyopaikat
                WHERE id IN ({})
            """.format(','.join('?' * len(duplicate_ids))), duplicate_ids)

        conn.commit()
        print(f"✓ Päivitetty {len(duplicates)} duplikoitua työpaikkaa.")

    except Error as e:
        print(f"Virhe työpaikkojen päivityksessä: {e}")
        conn.rollback()


def remove_duplicate_users(conn):
    """Remove duplicate users (same name, email, and workplace)."""
    try:
        cursor = conn.cursor()

        # Find duplicate users by name, email, and workplace, keeping the first occurrence
        cursor.execute("""
            SELECT name, email, tyopaikka, MIN(id) as keep_id, COUNT(*) as count
            FROM users
            GROUP BY name, email, tyopaikka
            HAVING COUNT(*) > 1
        """)

        duplicates = cursor.fetchall()

        if not duplicates:
            print("Ei duplikaatteja käyttäjissä.")
            return

        print(f"Löytyi {len(duplicates)} duplikoitua käyttäjää.")

        total_removed = 0
        for name, email, workplace_id, keep_id, count in duplicates:
            remove_count = count - 1
            total_removed += remove_count

            print(f"Käyttäjä '{name}' ({email}): säilytetään ID {keep_id}, poistetaan {remove_count} duplikaattia")

            # Delete duplicate users
            cursor.execute("""
                DELETE FROM users
                WHERE name = ? AND email = ? AND tyopaikka = ? AND id != ?
            """, (name, email, workplace_id, keep_id))

        conn.commit()
        print(f"✓ Poistettu {total_removed} duplikoitua käyttäjää.")

    except Error as e:
        print(f"Virhe käyttäjien päivityksessä: {e}")
        conn.rollback()


def reset_auto_increment(conn):
    """Reset auto-increment counters for clean IDs."""
    try:
        cursor = conn.cursor()

        # Reset users table auto-increment
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")
        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM users) WHERE name='users'")

        # Reset tyopaikat table auto-increment
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='tyopaikat'")
        cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM tyopaikat) WHERE name='tyopaikat'")

        conn.commit()
        print("✓ Auto-increment laskurit nollattu.")

    except Error as e:
        print(f"Virhe auto-increment nollauksessa: {e}")
        conn.rollback()


def main():
    database = r"pythonsqlite.db"

    conn = create_connection(database)
    if conn is None:
        print("Error! cannot create the database connection.")
        return

    try:
        print("Aloitetaan tietokannan päivitys...\n")

        remove_duplicate_workplaces(conn)
        remove_duplicate_users(conn)
        reset_auto_increment(conn)

        print("\n✓ Tietokanta päivitetty onnistuneesti!")

    finally:
        conn.close()


if __name__ == '__main__':
    main()