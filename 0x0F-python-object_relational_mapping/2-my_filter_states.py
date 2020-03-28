#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
"""
    script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
"""
from sys import argv
""" module to use command line arguments """
import MySQLdb
""" module to connect to a MySQL database and execute SQL queries. """
if __name__ == "__main__":
    """ execute only if run as a sript """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    try:
        search = argv[4]
        stmt = """
        SELECT * FROM states WHERE name='{:s}' ORDER BY id ASC;
        """.format(search)
        cur.execute(stmt)
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
