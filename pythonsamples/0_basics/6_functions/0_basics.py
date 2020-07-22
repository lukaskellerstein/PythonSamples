

# method
def mymethod():
    print('doing nothing')


mymethod()


# method with input parameter
def mymethod2(text):
    print(f'oh i have input parameter - {text}')


mymethod2("WOOOOW")


# function
def myfunction() -> int:
    return 5


print(myfunction())


# function with input parameter
def myfunction2(val):
    '''
    DOCSTRING: 
    INPUT: val is displayed value
    OUTPUT: return 'ehm ehm' value
    '''
    return f"EHM EHM {val}"


print(myfunction2("HELLO WORLD"))

