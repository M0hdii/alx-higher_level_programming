#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is provided below
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to select all states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all the rows using fetchall() method
        rows = cursor.fetchall()

        # Print the fetched rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
