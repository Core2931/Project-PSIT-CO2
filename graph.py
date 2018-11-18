import matplotlib.pyplot as plt
import csv
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

def cal2senple():

    for i,j in row_list,sumvars_list:
        print(i,j)
    for i in range(1993, 2019):
        years_data4.append(i)
    print(years_data4)

def demo1():
    x1 = years_data1
    y1 = vars_data1
    x2 = years_data2
    y2 = vars_data2
    x3 = years_data3
    y3 = vars_data3
    
    plt.plot(x1 ,y1)
    plt.show()


#demo1()

def main():
    print(sumvars_list)
    print(row_list)


cal2senple()