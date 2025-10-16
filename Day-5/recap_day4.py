def display():
    print('Welcome to recap of functions')
display()

username=input('Enter User Name:\t')
print(f'Welcome to function Mr.\\Mrs.',(username))

my_num=int(input('Enter number to find out cube and square:\t'))

def cube(num):
    cube_num=num*num*num
    print(f'Cube of given Number:{num} is =\t{cube_num}')

def square(num):
    return num*num

cube(my_num)
sq=square(my_num)
print(f'Square of{my_num} is:{sq}')
print(f'Number:{my_num} square:{sq}')

# bagi keterangan salary dan bonus
# def salBonus(salary):
#     return salary*0.10
# mySalary=float(input('Enter Salary:\t'))
# bonus=salBonus(mySalary)
# print(f'Salary:{mySalary} Bonus:',(bonus))
# print(f'Salary after bonus=\t',(mySalary+bonus))

#bagi keterangan salary + bonus terus
def salBonus(salary):
    return salary*0.10
mySalary=float(input('Enter Salary:\t'))
bonus=salBonus(mySalary)
print(f'Salary after bonus=\t',(mySalary+bonus))


# welcome('Rin')
# display()
# my_num=int(input('Enter Number to find out Cube:\t'))
# cube(my_num)

# my_num=int(input('Enter number to find out cube and square:\t'))

# cube(my_num)
# sq=square(my_num)
# print(f'Square of{my_num} is:{sq}')
# print(f'Number:{my_num} square:{sq}')



#  def cms(inches):
#     return inches*2.54
# inches=float(input('Enter the inches size:'))
# print(f'inches:{inches} cms:',cms(inches))

def add(a,b)
total=a+b
return total

result=add(12,15)
print(result)

add=lambda a,b: a+b

print(add(2,3))