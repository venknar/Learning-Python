import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()
game_id = results[0][0]

print("Categories for Game #%d:" % (game_id,))

query = """SELECT name, round FROM category
WHERE game=%d ORDER BY round""" % (game_id)

cursor.execute(query)
results = cursor.fetchall()

for result in results:
    name, round = result
    print("Round %d: %s" % (round, name))


connection.close()
