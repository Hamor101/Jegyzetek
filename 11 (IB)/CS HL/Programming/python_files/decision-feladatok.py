def f1():
    x = int(input("Give me an integer:"))
    print(("Even" if x % 2 == 0 else "Odd"))

def f2():
    x = int(input("N1:"))
    y = int(input("N2:"))
    print(f"{x} is" + (" not " if x % y != 0 else " ") + f"divisible by {y}")

def f3():
    name = input("Name:")
    if name:
        print(f"Hello, {name}")
    else:
        print("You did not enter a name.")

def f4():
    x = int(input("N1:"))
    y = int(input("N2:"))
    print(("Equal" if x == y else (x if x > y else y)))

def f5():
    x = int(input("Positive integer:"))
    assert x > 0
    print("The number is" + (" not " if x < 20 or x > 30 else " ") + "between 20 and 30.")

def f6():
    x = input("Positive integer less than 1000000:")
    print(f"{len(x)} digits.")

def f7():
    x,y,z = input("Three numbers separated by spaces:").split(" ")
    x = int(x)
    y = int(y)
    z = int(z)
    print(f"{max(x,y,z)} is the biggest")

def f8():
    grade = 1
    l = [40, 55, 70, 85]
    p = int(input("Percentage on test:"))
    for i in l:
        if p >= i:
            grade += 1
        else:
            break
    print(grade)

import math

def f9():
    x,y,z = input("Three numbers in increasing order separated by spaces:").split(" ")
    expr = [x+y>z, x+z>y, y+z>x]
    x = int(x)
    y = int(y)
    z = int(z)
    if any(expr):
        if x**2 + y**2 == z**2:
            print("These are the sides of a right triangle.")
            return
        print("These are the sides of a triangle.")

def f10():
    string = input("Text:")
    print(f"String is" + (" not " if not string.isnumeric() else " ") + "numeric")

def f11():
    days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
    ordinal = int(input("Ordinal number of weekday:"))
    print(days[ordinal] if ordinal in days else "That is not a valid input.")

def f12():
    months31 = {3:"March", 5:"May", 7:"July", 8:"August", 10:"October", 12:"December"}
    ordinalMonth = int(input("Ordinal number of month:"))
    print(28 if ordinalMonth == 2 else (31 if ordinalMonth in months31 else 30))

def f13():
    x,y = input("x,y, separated by spaces:").split(" ")
    x = int(x)
    y = int(y)
    quad = {(x>0 and y>0):"First", (x>0 and y < 0): "Second", (x<0 and y<0):"Third", (x<0 and y>0): "Fourth"}
    for i in quad:
        if i == True:
            print(quad[i])
            return
    print("Point is on the" + (" origin" if x == 0 and y == 0 else (" y axis" if x == 0 else (" x axis" if y == 0 else " "))))

def f14():
    name = input("Name:")
    height = int(input("Height (cm):"))
    exp = int(input("Number of plays:"))
    if height > 200:
        print(f"{name} is Suitable.")
        return
    l = [height > 165, exp > 0]
    print(f"{name} is ", ("Suitable" if all(l) else "Not Suitable."))

def f15():
    month31 = [3, 5, 7, 8, 10, 12]
    monthNum = int(input("Ordinal number of month:"))
    dayNum = int(input("Date:"))
    v = (True if monthNum in month31 and dayNum <= 31 else (True if dayNum < 28 or (monthNum != 2 and dayNum <= 30) else False))
    print(("Valid date" if v else "Invalid date"))

if __name__ == "__main__":
    f1()
    f2()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()
    f9()
    f10()
    f11()
    f12()
    f13()
    f14()
    f15()