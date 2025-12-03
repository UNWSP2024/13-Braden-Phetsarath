import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    question = int(input("Type 1 to add an entry \nType 2 to remove an entry \nType 3 to change an entry\n--------------\n"))

    if question == 1:
        add_entry(cur)
    if question == 2:
        remove_entry(cur)
    if question == 3:
        modify_entry(cur)


    conn.commit()
    conn.close()
def add_entry(cur):
    more = 'y'
    while more.lower() == 'y':
        name = input('Enter name: ')
        number = input('Enter phone number: ')

        cur.execute("INSERT INTO Entries (name, number) VALUES (?, ?)", (name, number))

        more = input('Do you want to add another entry? y/n')

def remove_entry(cur):
    more = "y"
    while more.lower() == 'y':
        name = input('Enter the name to delete: ')
        cur.execute("DELETE FROM Entries WHERE name = ?", (name, ))

        more = input('Do you want to remove another entry? y/n')

def modify_entry(cur):
    more = "y"
    while more.lower() == 'y':
        name = input('Enter the name to modify: ')
        new_phone = input('Enter the new phone number: ')

        cur.execute(
            "UPDATE Entries SET number = ? WHERE name = ?",
            (new_phone, name))

        more = input('Do you want to modify another entry? y/n: ')
if __name__ == '__main__':
    main()






