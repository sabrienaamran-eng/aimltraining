# def factorial(num):
#     if((num==0)or(num==1)):
#         return 1
#     else:
#         return num*factorial(num-1)
    
# num=int(input('Enter a number to find out factorial:'))
# print(f'Factorial of{num} is:', factorial(num))

# #write a python function which converts inches to cms
# #1 inch =2.5cm
# option 1
# def cms(inches):
#     return inches*2.54
# inches=float(input('Enter the inches size:'))
# print(f'inches:{inches} cms:',cms(inches))

# # option 2
# def cms(inches):
#     return inches*2.54
# inches=float(input('Enter the inches size:'))
# print(f'cms:',cms(inches))

#write a function to find out the table of given number
def gen_table(num):
    for 1 in range(1,11):
        print(f'{num}*{i}=\t{(num*i)}')

number=int(input('Enter Number to findout tbale'))
gen_table(number)