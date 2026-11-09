<span style="font-family:'cascadia code'">

# Python programming
- Python programs are written inside of files whose names end with ".py"
- For example, [first-python-file.py](python_files/first-python-file.py) is a python file

### Program execution
- Lines of code are executed one after the other, from `top to bottom`

## Printing "Hello world!"
- To write text to our screen/terminal, we can use the `print()` function
- The print function takes some text (a string) as its `argument`
- The arguments of functions are written between the parentheses
- To print "Hello world!" we can write the following:
```py
print("Hello world!")
```
## Comments
- Comments are written after "#"
- They can be used to `explain your code` to someone reading it
- This means comments are `ignored when your program is running`, they are only meant for humans to read
``` py
# This entire line is a comment :)
print("Hello") # Comments can also be written at the end of lines like this
```
## Creating & Using variables
- Variables are used to store different types of values
### Naming
- Variables have custom names
- Their names can be almost anything
- Names can consist of letters (and also "_") and numbers
- Variable names `must start with a letter` or "_"
``` py
valtozoNev2 = 1     # This is a valid variable name
ABCD_name = 1       # and so is this,
_ = 1               # and this
#------------------------------------------------------
2Valtozonev = 1     # But this >>is not valid<<
```
### Giving values to variables
- You can give a variable a value like this:
``` py
x = "Bob"
```
- Here, x is the variable name, and "bob" is the `value`
- The "=" sign is called the `assignment operator`, because it is used to `assign a value to something`
- We can also do this:
```py
x = 5
```
- With the above line, we changed the value of _x_ from "Bob" to 5
- This also changed the `type` of x from a `string` to an `integer`

### Data types
- Every variable has a data type
- Data type depends on the `value` --> It tells us what kind of value is stored inside the variable
- We can change x to a couple of different data types:
``` py
x = 5               # Integer (int)
x = 5.5             # Floating-point number (float)
x = 'A'             # Char (a single character)
x = "Bob"           # String --> A string of characters
x = True            # Boolean variable --> Can only have 2 values (True, False)
x = [1,2,3,4,5]     # List --> Can store multiple items of any data type
# Btw, there are many more data types, these are just the basic ones that are useful for now
```
- If we want to know the data type of a variable, we can use the `type()` function
- This function takes the `variable's name` as its argument
- So, for x it looks like this:
``` py
type(x)     # This checks the data type of x
```
- Right now, the type of x is `list`, because the last value we `assigned` to x was \[1,2,3,4,5\] (see the code above this)
### Printing types and variables
- _print()_ can take many types of arguments, not just text
- if we give _print()_ the name of a variable, it will print the `value` of that variable:
``` py
print(x)    # This will print '[1,2,3,4,5]' to the screen
x = "Hello World!"
print(x)    # This will print "Hello World!"
```
- We can also give `print()` the output of `type()`:
- We can do this in 2 ways
- 1:
    ```py
    x = "Hello World"
    y = type(x)
    print(y)
    ```
- 2:
    ```py
    x = "Hello World"
    print(type(x))
    ```
- These two pieces of code `do the same thing`

### Changing the type
- Sometimes, we want to convert a data type into another
- E.g: 
  - a string --> an integer
  - a float --> an integer
  - an integer --> a string
- Changing the data type is called `casting`
- Example:
  - Write a program