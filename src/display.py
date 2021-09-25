##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-202unsold-tom.hermann
## File description:
## display
##

from src.calcul import calculArray, calculZLaw, calculExpectedValue, calculVairance

def separator():
    print("--------------------------------------------------------------------------------")


def displayArray(a, b):
    array = calculArray(a, b)
    separator()
    print("    X=10    X=20    X=30    X=40    X=50    Y law")
    Y = 10
    for y in range(0, 6):
        if (y != 5):
            print("Y={}" .format(Y), end='    ')
        else:
            print("X law", end='    ')
        for x in range(0, 6):
            print('{:.3f}'.format(array[y][x]), end='')
            if (x != 5):
                print('    ', end='')
        print('')
        Y += 10
    separator()
    return array

def displayZLaw(array):
    zLaw = calculZLaw(array)
    print("z    20    30    40    50    60    70    80    90    100")
    print("p(Z=z)", end="    ")
    for i in range(0, 9):
        if (i != 8):
            print("{:.3f}" .format(zLaw[i]), end="    ")
        else :
            print("{:.3f}" .format(zLaw[i]))
    return zLaw

def displayLastSection(array, zLaw):
    separator()
    valueZLaw = [20, 30, 40, 50, 60, 70, 80, 90, 100]
    valueXY = [10, 20, 30, 40, 50]
    Yvalue = []
    for i in range(0, len(array)):
        Yvalue.append(array[i][5])
    print("expected value of X:    {:.1f}" .format(calculExpectedValue(valueXY, array[5])))
    print("variance of X:        {:.1f}" .format(calculVairance(valueXY, array[5])))
    print("expected value of Y:    {:.1f}" .format(calculExpectedValue(valueXY, Yvalue)))
    print("variance of Y:        {:.1f}" .format(calculVairance(valueXY, Yvalue)))
    print("expected value of Z:    {:.1f}" .format(calculExpectedValue(valueZLaw, zLaw)))
    print("variance of Z:        {:.1f}" .format(calculVairance(valueZLaw, zLaw)))
    separator()
