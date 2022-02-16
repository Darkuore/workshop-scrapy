##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## Exercice4
##

def anagrams(name, list_name):
    list_result = list()
    for i in list_name:
        if(sorted(name) == sorted(i)):
            list_result.append(i)
    return list_result
