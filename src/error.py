##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-202unsold-tom.hermann
## File description:
## error
##


from sys import argv, stderr
from src.constante import *

def usage():
    print("USAGE\n\t./202unsold a b")
    print("DESCRIPTION\n")
    print("\ta\tconstant computed from past results")
    print("\tb\tconstant computed from past results")
    exit(EXIT_SUCCESS)

def error_case(argc):
    if (argc == 2 and (argv[1] == "-h" or argv[1] == "--help")):
        usage()
    if (argc != 3):
        exit(84)
    try:
        float(argv[2])
    except ValueError:
        print("a must be an number", file = stderr)
        exit(EXIT_FAILURE)
    try:
        float(argv[1])
    except ValueError:
        print("b must be an number", file = stderr)
        exit(EXIT_FAILURE)
    if float(argv[1]) < 50 or float(argv[2]) < 50:
        print("b and a must be greater than 50", file = stderr)
        exit(EXIT_FAILURE)
