# This will print "What's your name? " to the terminal and then wait for user input
# The user's input will become the value of _name_
name = input("What's your name? ")
# Name's type will now be _string_



# Three different ways to do the same thing:
print("Hi, " + name)        # Adding (concatenating) strings together --> "hi" + "hello" = "hihello"
print("Hi,",name)           # Giving print() each element as a different argument
print(f"Hi, {name}")        # Using a formatted string (f-string)



# Converting inputs to numbers:


number1 = input("Enter a number:")
# _number1_ is a string right now --> We can't do math operations on it --> we want to convert it to an integer
# Let's check the type of _number_:
print(type(number1))
# This will print <class 'str'> --> This means it is a 'str' object --> a _string_
number = int(number1)        # int() converts its argument into an integer
# Now, the type of number is an _integer_:
print(type(number1))         # This will print: <class 'int'>
#--------------------------------------------------------------------------------------

# Let's ask for two numbers from the user then add them together:

number1 = input("Give me a number:")    # Here _number1_ is a string
number1 = int(number1)                  # Now it's an integer

number2 = input("Give me another number:")
number2 = int(number2)

print(number1 + number2)