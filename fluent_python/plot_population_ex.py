from matplotlib import pyplot
data = open("world_population.txt", "r").readlines()

dates = []
populations = []
for point in data:
    date, population = point.split()
    dates.append(date)
    populations.append(population)

pyplot.plot(dates, populations, "o-")
pyplot.xlabel("Year")
pyplot.ylabel("World population in millions")
pyplot.title("World population over time")
pyplot.show()