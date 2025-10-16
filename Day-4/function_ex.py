# #def function_name(parameters):
# '''Docstring'''
# statement (s)

# function without parameters
def welcome():
    print("Welcome to Function")
    print("Our First Function")

welcome()
#function with a parameter
def welcome(name):
    print("Welcome to functions in python Mr.\\Ms",name)

username=input('Enter your name:\t')
#function call
welcome(username)

# function with parameter and return

def add(num1,num2):
    return num1+num2
fnum=int(input("Enter first Number"))
snum=int(input("Enter second Number"))
print(f'Result after adding{fnum} and {snum} is =\t',add(fnum,snum))