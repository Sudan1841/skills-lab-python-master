# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: A program that adds all the numbers entered by the user until the number entered is zero

x = eval(input("? "))
s = x
while x != 0:
    x = eval(input("? "))
    s = s + x
print("The sum of all numbers is %d" % s)
