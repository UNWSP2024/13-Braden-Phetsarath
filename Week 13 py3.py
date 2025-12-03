#Braden Phetsarath
#12/3
# Phonebook.db

import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    create_table(cur)

    add_entries(cur)

    conn.commit()
    display_entries(cur)
    conn.close()

def create_table(cur):
    cur.execute('DROP TABLE IF EXISTS Entries')

    cur.execute('''CREATE TABLE Entries (Name TEXT, NUMBER TEXT)''')

def add_entries(cur):
    people = [("Shinji Ikari", "333-3333"),
              ("Ayanami Rei", "333-3334"),
              ("Asuka Soryu Langly", "333-3335"),
              ("Ritsuko Katsuragi", "333-3336")
              ]
    cur.executemany('INSERT INTO Entries (Name, Number) VALUES (?, ?)', people)

def display_entries(cur):
    entries = cur.execute('SELECT * FROM Entries')

    rows = cur.fetchall()

    print("-----------Entries-----------")
    for row in rows:
        print(f"Name: {row[0]}, Number: {row[1]}")


if __name__ == '__main__':
    main()
