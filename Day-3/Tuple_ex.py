# print("We are going to discuss tuple here")
# subjects=('python','java','dotnet','sql','power bi')
# print('\n All subjects are:\n')
# for sub in subjects:
# print(sub,"\t") #menegak

# print("We are going to discuss tuple here")
# subjects=('python','java','dotnet','sql','power bi')
# print('\n All subjects are:\n')
# print('Number of subjects are:',len(subjects))
# for sub in subjects:
#     print(sub,end="\t") #melintang

# numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
# print('Total Number in tuple:',len(numbers))
# for num in numbers:
#     print(num,end="\t")

# #tupleName.index(item)will return the index of first occurrence of item in tupleName
# search_num=int(input('Enter Number to find out index'))
# if search_num in numbers:
#     print(f'Index of {search_num} is: \t',numbers.index(search_num))
# else:
#     print(f'No Such Number {search_num} in our tuple')

# names=('apple','orange','mango','grape','avocado','strawberry')
# print('Total Number in tuple:',len(names))
# for num in names:
#     print(num,end="\t")

# #tupleName.index(item)will return the index of first occurrence of item in tupleName
# search_num=(input('Enter Fruit to find out index'))
# if search_num in names:
#     print(f'Index of {search_num} is: \t',names.index(search_num))
# else:
#     print(f'No Such Fruit {search_num} in our tuple')

# numbers=(1,2,3,4,10,2,3,2,3,5,50,1)
# print('Total Number in tuple:',len(numbers))
# for num in numbers:
#     print(num,end="\t")
# #tupleName.count(item): tupleName count(item) will return number of times item occours in tuppleName.
# search_num=int(input('\nEnter Number to find out frequency:\t'))
# if search_num in numbers:
#     print(f'Number: {search_num} occurs: {numbers.count(search_num)} times')
# else:
#     print(f'No Such Number {search_num} in our tuple')

#Write a program to sum a list with 4 numbers
numbers=[10,20,30,50]
total=sum(numbers)
print('Sum of numbers is:',total)

numbers=[10,20,30,50]
total=sum(numbers)
print('Sum of numbers from tuple :',total)