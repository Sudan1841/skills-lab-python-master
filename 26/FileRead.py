# MSU Denver - Skills Lab - 2020
# student: Abdulmajid Hasssan
# Description: Reads a CSV file containing students

f_in = open("students.csv", "rt")
for line in f_in:
    line = line.strip()
    id, name = line.split(",")
    print(id, name)
f_in.close()

