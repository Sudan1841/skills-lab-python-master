# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: A program that asks the user to enter a nonnegative number. The program should then display all the nonnegative numbers that are less than the given numbers. 

n = eval(input("n? "))
if n < 0:
    print("Negative number entered!")
    print("I quit!")
else:
    for x in range(n):
        print(x)
