#Braden Phetsarath
#12/3
# Cities.db Display
import sqlite3
def main(cur):
    print ("Contents cities.db/Cities table: ")
    cur.execute("SELECT * FROM cities")
    resultls = cur.fetchall()
    for row in resultls:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')
main()
