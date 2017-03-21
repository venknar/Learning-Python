import sqlite3

connection = sqlite3.Connection("jeopardy.db")
cursor = connection.cursor()

cursor.execute("Select name from Category LIMIT 10")
results = cursor.fetchall()

print("Printing All Caegories: \n")

for category in results:
    print(category[0])

connection.close()