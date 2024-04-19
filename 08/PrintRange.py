# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: A program that asks the user to enter two integer numbers "a" and "b". The program should then display all the numbers from "a" to "b."

a = eval(input("a? "))
b = eval(input("b? "))
for x in range(a, b + 1):
    print(x)
