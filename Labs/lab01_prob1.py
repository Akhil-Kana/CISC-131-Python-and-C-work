"""
CISC 131 Problem 1 - Akhil Kanayinkal (kana9520) and Phat Nguyen (nguy4328)
"""
import cisc131lab1

x = cisc131lab1.getX()
y = cisc131lab1.getY()
z = cisc131lab1.getZ()

print("Original values: x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))

# Write your code to "rotate" values here
switch = 0
switch = x
x = y
y = z
z = switch

# Do NOT change code for the print statements
print("Rotated values: x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))
