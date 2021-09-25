##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-202unsold-tom.hermann
## File description:
## calcul
##

from statistics import pvariance

def calculProba(a, b, x, y):
    res = (a - x) * (b - y)
    res /= (5 * a - 150) * (5 * b - 150)
    return res

def calculLineLaw(line):
    sum = 0
    for i in range(0, len(line)):
        sum += line[i]
    return sum


def calculColumnLaw(array, x):
    sum = 0
    for y in range(0, 5):
        sum += array[y][x]
    return sum

def calculArray(a, b):
    arrayOfValue = []
    x_value = 10
    y_value = 10
    for y in range(0, 5):
        arrayOfValue.append([])
        x_value = 10
        for x in range(0, 5):
            arrayOfValue[y].append(calculProba(a, b, x_value, y_value))
            x_value += 10
        y_value += 10
    for i in range(len(arrayOfValue)):
        arrayOfValue[i].append(calculLineLaw(arrayOfValue[i]))
    arrayOfValue.append([])
    for i in range(0, 6):
        arrayOfValue[5].append(calculColumnLaw(arrayOfValue, i))
    return arrayOfValue

def calculZLaw(array):
    zLaw = []
    zSum = 0
    z = 20
    for i in range(0, 9):
        for y in range(0, 5):
            for x in range(0, 5):
                if ((((y + 1) * 10) + ((x + 1) * 10)) == z):
                    zSum += array[y][x]
        zLaw.append(zSum)
        zSum = 0
        z += 10
    return zLaw

def calculExpectedValue(value, proba):
    res = 0
    for x in range(0, len(value)):
        res += value[x] * proba[x]
    return res

def calculVairance(value, proba):
    variance = 0
    expected = calculExpectedValue(value, proba)
    for i in range(0, len(value)):
        variance += (value[i] - expected)**2 * proba[i]
    return variance
