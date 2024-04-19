# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: A program that asks the user for a temperature in Fahrenheit, converts it to Celsius, and displays the result back to the user.

fahrenheit = eval(input("Fahrenheit? "))
celsius = (fahrenheit - 32) * 5 / 9
print("%.2fF corresponds to %.2fC" % (fahrenheit, celsius))
