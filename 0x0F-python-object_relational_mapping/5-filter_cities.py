#!/usr/bin/python3
"""
    script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name=%s""", (sys.argv[4],))
    [print(city) for city in cur.fetchall()]



    cur.close()
    conn.close()
