##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## Exercice3
##

def calculate(list_arg):
    if (isinstance(list_arg, list) == False):
        return "False"
    result = 0
    for i in list_arg:
        if (isinstance(i, str) == True):
            if (i.isdigit() == True):
                result += int(i)
    return result
