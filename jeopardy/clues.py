import sqlite3

connection = sqlite3.Connection("jeopardy.db")
cursor = connection.cursor()

cursor.execute("Select text, answer, value from Clue LIMIT 10")
results = cursor.fetchall()

print("Printing All Clues: \n")

for clue in results:
    text,answer,value = clue

    print("[$%s]" % (value,))
    print("Question: %s" % (text))
    print("Answer : What is '%s' ?" % (answer,))

connection.close()