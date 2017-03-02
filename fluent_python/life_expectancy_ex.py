from matplotlib import pyplot

data = open("life_expectancies_usa.txt", "r").readlines()

dates = []
women_lifespan = []
men_lifespan = []

for line in data:
    d,m,w = line.split(",")
    dates.append(d)
    men_lifespan.append(m)
    women_lifespan.append(w)

pyplot.plot(dates, men_lifespan, "bo-", label="Men")
pyplot.plot(dates, women_lifespan, "mo-", label="Female")

pyplot.legend(loc="upper left")
pyplot.xlabel("Year")
pyplot.ylabel("Aget")
pyplot.title("Life expectancies for women and men in the USA over time")

pyplot.show()