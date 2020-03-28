#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
from sys import argv
import MySQLdb
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")
    cur = conn.cursor()
    stmt = "SELECT id, name FROM states ORDER BY states.id ASC"""
    cur.execute(stmt)
    for i in cur:
        print(i)
    conn.close()
