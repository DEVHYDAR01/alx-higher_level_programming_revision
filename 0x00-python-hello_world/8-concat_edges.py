#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str.split(", ")[2][:27] + " " + str.split(", ")[2].split(" ")[7] + " " + str.split(", ")[0][:6])