import matplotlib.pyplot as plt
import csv
years = []
vars = []


with open('data.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year = float(line[0])
        var = float(line[1])
        years.append(year)
        vars.append(var)

def demo1():

    x = years
    y = vars
    plt.plot(x ,y)
    plt.show()


demo1()