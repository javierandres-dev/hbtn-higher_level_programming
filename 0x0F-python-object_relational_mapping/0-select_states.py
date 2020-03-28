#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
""" script that lists all states from the database hbtn_0e_0_usa """
from sys import argv
""" module to receive arguments """
import MySQLdb
""" module to connect to a MySQL database and execute SQL statements """
if __name__ == "__main__":
    """ execute only if run as a sript, not be executed when imported """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    stmt = """
    SELECT id, name FROM states ORDER BY states.id ASC ;
    """
    cur.execute(stmt)
    for i in cur:
        print(i)
    cur.close()
    """ Close all cursors """
    conn.close()
    """ Close all databases """
