import matplotlib.pyplot as plt
import csv
year_data4_test = 1993
sumvars = 0
sumvars_list = []
num = 0
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
        year = float(line[0])
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
        else:
            print(sumvars)
            sumvars = 0
            sumvars += var_data4
            year_data4_test = year_data4
            num += 1
    print(sumvars)
        # years_data4.append(year_data4)
        # vars_data4.append(var_data4)

def demo1():
    x = years_data4
    y = vars_data4
    plt.plot(x ,y)
    plt.show()


#demo1()

def main():
    print(num)
    # print(sumvars_list)

main()