#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database using command line arguments
    # argv[1] = username, argv[2] = password, argv[3] = database name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    
    cur = db.cursor()
    
    # Execute the query. Requirement: Sort by states.id
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    query_rows = cur.fetchall()
    
    for row in query_rows:
        print(row)
        
    cur.close()
    db.close()