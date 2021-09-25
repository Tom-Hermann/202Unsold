#!/usr/bin/python3
##
## EPITECH PROJECT, 2020
## 106bombyx_2019
## File description:
## main
##

from sys import argv
from src.error import error_case
from src.display import displayArray, displayZLaw, displayLastSection

error_case(len(argv))
array = displayArray(float(argv[1]), float(argv[2]))
zLaw = displayZLaw(array)
displayLastSection(array, zLaw)
exit(0)