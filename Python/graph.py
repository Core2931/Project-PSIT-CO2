import matplotlib.pyplot as plt
import csv
import numpy as np
year_data4_test = 1993
sumvars = 0
row_list = []
sumvars_list = []
row = 0
years_data1 = []
vars_data1 = []
years_data2 = []
vars_data2 = []
years_data3 = []
vars_data3 = []
years_data4 = []
vars_data4 = []

with open('carbon.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year = int(line[0])
        var = float(line[1])
        years_data1.append(year)
        vars_data1.append(var)

with open('temperature.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year_data2 = int(line[0])
        var_data2 = float(line[1])
        years_data2.append(year_data2)
        vars_data2.append(var_data2)

with open('arctic.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year_data3 = int(line[0])
        var_data3 = float(line[1])
        years_data3.append(year_data3)
        vars_data3.append(var_data3)

with open('sea.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year_data4 = int(line[0])
        var_data4 = float(line[1])
        if year_data4 == year_data4_test:
            sumvars += var_data4
            row += 1
        else:
            row_list.append(row+1)
            row = 0
            sumvars_list.append(sumvars)
            sumvars = 0
            sumvars += var_data4
            year_data4_test = year_data4
    row_list.append(row+1)
    sumvars_list.append(sumvars)

def cal2semple():
    for i in range(len(sumvars_list)):
        num_a = sumvars_list[i]
        num_b = row_list[i]
        vars_data4.append((int((num_a/num_b)*100))/100)
    for i in range(1993, 2019):
        years_data4.append(i)

def all_graph():
    fig = plt.figure()
    fig.add_subplot(221)
    plt.plot(years_data1, vars_data1)
    #plt.plot([2019, 2020],[420, 430], linestyle="--")
    #plt.xlabel("YEAR")
    plt.ylabel("CO2 (parts per million)")
    plt.title("Carbon")
    fig.add_subplot(222)
    plt.plot(years_data2, vars_data2)
    plt.title("Global Temperature")
    #plt.xlabel("YEAR")
    plt.ylabel("Temperature Anomaly (C)")
    fig.add_subplot(223)
    plt.plot(years_data3, vars_data3)
    plt.title("Arctic Sea Ice")
    plt.xlabel("YEAR")
    plt.ylabel("Square KM")
    fig.add_subplot(224)
    plt.plot(years_data4, vars_data4)
    plt.title("Sea Level")
    plt.xlabel("YEAR")
    plt.ylabel("Sea Height (mm)")
    plt.show()

def main():
    cal2semple()
    all_graph()
main()