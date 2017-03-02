from matplotlib import pyplot
import random

xvalues = [0,4,7,20,22,25]
yvalues = [random.randint(0,30) for elt in xvalues]

#[0,2,4,8,16,32] 

pyplot.plot(xvalues,yvalues, "o-")
pyplot.ylabel("value")
pyplot.xlabel("Time")
pyplot.title("Test Plot")

pyplot.show()