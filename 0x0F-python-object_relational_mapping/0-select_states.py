#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
""" module to connect to a MySQL database and execute SQL queries. """
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="admin",
    db="hbtn_0e_0_usa",
    charset="utf8"
)
cur = conn.cursor()
try:
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
except MySQLdb.Error:
    try:
        print ("MySQLdb Error")
    except IndexError:
        print ("MySQLdb Error - IndexError")
for row in query_rows:
    print(row)
cur.close()
""" Close all cursors """
conn.close()
""" Close all databases """
