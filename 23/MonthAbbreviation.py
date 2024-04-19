# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: Prints the abbreviation of the month that corresponds to a given month number​

month = eval(input('month? '))
months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
index = (month - 1) * 3
print(months[index:index + 3])

