import math
import inspect
# num=int(input('Enter Number to find out Square root \t'))
# print(f'Square root of {num} \t',round (math.sqrt (num),2))

functions=inspect.getmembers(math,inspect.isbuiltin)
print('All Function in math module')
for n, func in functions:
    print(n,end="\t")
