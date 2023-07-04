print("Basics - primitive types")

myInt = 5
myFloat = 0.5
myString = "Hello"
myBoolean = True

# type casting
myVar1 = int("5")
myVar2 = str(myInt)
print(myVar2)

# string formatting
print("string {0} shoud contains {1}".format("AAA", "BBB"))
print("string {a} shoud contains {b}".format(a="AAA", b="BBB"))
print("result is {a}".format(
    a=myInt))
# formatted string literal
print(f"result is {myInt}")

# string functions
print(myString.replace("e", "i", -1))
print(myString.lower())
print(myString.upper())

# finding in string
if "l" in myString:
    print("'l' letter is in " + myString)

