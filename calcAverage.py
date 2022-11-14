# function to find average of ages

ages = [10, 20, 30, 140]
incomes = [100, 200, 600]

def calculateAverage(list):
    sum = 0;
    for i in list:
        sum = sum + i;

    return sum/len(list)

print(calculateAverage(incomes))

