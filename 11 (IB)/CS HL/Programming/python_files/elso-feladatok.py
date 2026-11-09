#1. Feladat:
# Read two _real_ numbers from user, then:
# Add, subtract, multiply, divide, integer divide them
a,b = (input("Give me two numbers, separated by a space:").split(" "))
a = float(a)
b = float(b)

abSum = a + b
abDifference = a - b
abProduct = a * b
abRatio = a / b
abRatioInteger = a // b

print(f"""
        Sum: {abSum}
        Difference: {abDifference}
        Product: {abProduct}
        Ratio: {abRatio}
        Integer ratio: {abRatioInteger}
""")


#2. Feladat:
# Create a program that asks the name of the user and then greets them
name = input("What is your name? ")
print(f"Hello, {name}!")

#3. Feladat:
# Create a program that asks the name of the user and their position in the school
name, position = input("Give the name and position of a person in the school separated by \':\' >>").split(":")
print(f"Name: {name} Position: {position}")

#4. Feladat:
# Create a progam that requests two decimal numbers and displays their sum, difference, product, ratio
a, b = input("Give me two decimal numbers separated by a space").split(" ")
a = float(a)
b = float(b)

abSum = a + b
abDifference = a - b
abProduct = a * b
abRatio = a / b
abRatioInteger = a // b

print(f"""
        Sum: {abSum}
        Difference: {abDifference}
        Product: {abProduct}
        Ratio: {abRatio}
        Integer ratio: {abRatioInteger}
""")

#5. Feladat:
# Create a program that requests the radius of a circle and calcuates and prints is perimeter and area
import math

r = int(input("Give me the radius of a circle:"))
area = math.pi*r**2     # Circle area: 𝝅*r*r
circumference = 2*math.pi*r
print(f"Its area: {area}, its circumference: {circumference}")

#6. Feladat
#Create a programa that requests the side of a square and calculates perimeter and area
a = int(input("Give me the side of a square:"))
area = a*a
circumference = 4*a
print(f"Its area: {area}, its circumference: {circumference}")

#7. Feladat
# Modify previous program to calculate area of rectangles as well
a,b = input("Give me the sides of a rectangle separated by space:").split(" ")
a = int(a)
b = int(b)
area = a*b
circumference = 2*(a+b)
print(f"Its area: {area}, its circumference: {circumference}")

#8. Feladat
# Create ap orgram the requests the three sides of a triangle and calculates perimeter and area
a,b,c = input("Give me the three sides of a triangle separated by spaces:").split(" ")
a = int(a)
b = int(b)
c = int(c)
s = (a+b+c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
circumference = (a+b+c)
print(f"Its area: {area}, its circumference: {circumference}")

#9. Feladat
# Create a program that request a number (0<=n<=255) and prints the ASCII character that number represents
n = int(input("Give me a number from 0 to 255:"))
if n < 0 or n > 255:
    print("Incorrect input.")
print(f"{n} represents: \'{chr(n)}\'")

#10. Feladat
# Create a program that requests a character and displays its ASCII code
c = input("Give me a character:")
print(f"The ascii number of \'{c}\' is {ord(c)}")

# 11. Feladat
# Create a program that requests a character and decides if it was an 'a'
c = input("Give me a character:")
try:
    assert type(c) == str() and len(c) == 1
except AssertionError:
    print("You didn't give me character :(")


if c == 'a':
    print("You wrote an \'a\'!")
else:
    print("You didn't write an \'a\'")
