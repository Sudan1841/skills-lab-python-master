# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: Reads a person’s name and computes the corresponding username (the user’s first initial followed by up to seven letters of the user’s last name)

first = input('first? ')
last = input('last? ')
username = first[0] + last[:7]
print(username)

