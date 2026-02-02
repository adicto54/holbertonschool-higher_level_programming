#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db_name)
    cur = db.cursor()
    
    # Execute query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch and print results
    for row in cur.fetchall():
        print(row)
    
    # Close cursor and connection
    cur.close()
    db.close()
