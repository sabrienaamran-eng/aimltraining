# import random

# print('Random Number from 1 to 1000')
# print(random. randint(1,1000))

import random
def findwinner():
    name=input('Enter Your Name \t')
    luckyNumber=random.randint(1,10)
    print(f'Welcome Mr.\\Mrs. {name} Coupon Number:{luckyNumber}🔥')
    if(luckyNumber==1):
        print('You Have Won Proton XL-65 Car')
    elif(luckyNumber==3):
        print('You Have Won a IPad')
    elif(luckyNumber==9):
        print('You Have Won a IPhone')
    else:
        print('Better Luck Next Time')
