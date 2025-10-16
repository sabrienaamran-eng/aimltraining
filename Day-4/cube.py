# print('Write a function to find out the cube of given number')
# #5: 5*5*5 (e.g. cube of 5 is 5*5*5 means 125)

# def cube(num):
#     return num*num*num
# given_num=int(input('Enter Number to find out cube of number:\t'))
# print(f'Number is:{given_num} cube is', cube(given_num))

#write a function to calculate bonus of given salary
#function take salary as input and return bonus 10% of salary.
def calculate_bonus(salary):
    return salary*0.1
salary=float(input('Please enter your salary for the return bonus'))
print(f'salary is:{salary} bonus is:',calculate_bonus(salary))


    