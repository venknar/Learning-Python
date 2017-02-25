f = open("scores.txt", "r")

participants = {}
for line in f:
    entry = line.strip().split(",")
    participants[entry[0]] = entry[1]
    
f.close()

print(participants)

    