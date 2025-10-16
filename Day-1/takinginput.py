# username=input("Enter User Name \t") #\t(for space)
# age=int(input("Enter Age"))
# salary=float(input("Enter Salary"))
# databaseKn=bool(input("Do You Know databases?")) #Kn (is knowledge),if didnt ans (turn out false)
# print("Your Name is Mr.\\Mrs.",username)
# print("Your Age is",age)
# print("Your Salary is",salary)
# print("Database the Databases?",databaseKn)

# #Adding Two Number
# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=num1+num2
# print(f"Result after adding {num1} and {num2} = \t {result}")

# #Multiple Two Number
# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=num1*num2
# print(f"Result after multiplication {num1} and {num2} = \t {result}")

# #Division Example
# num1=int(input("First Number"))
# num2=int(input("Second Number"))
# result=num1/num2
# print(f"Result after dividing {num1} and {num2} = \t {result}")

# # % finding Reminder Example
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1%num2
# print(f"Remainder after dividing {num1} and {num2} = \t {result}")

#taking more than one input using single line
num1,num2=input("Enter two numbers seprated by space").split()
result=int(num1)+int(num2)
print(f"Numbers Entered by you are {num1} and {num2} and addition of numbers {result}")