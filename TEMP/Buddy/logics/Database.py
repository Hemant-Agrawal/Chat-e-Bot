import sqlite3
import os
current = os.getcwd()


def SQL(query):
    try:
        connection = sqlite3.connect(current + "/db.sqlite3")
        cursor = connection.cursor()
        cursor.execute(query)
        fetch_result = cursor.fetchall()
        result = ""
        for i in fetch_result:
            result = result + "   ".join(map(str, i)) + "\n"
        connection.close()
        return result
    except Exception as e:
        print("Can't execute the Query"+str(e))

