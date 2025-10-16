#NUMBER 1
# class Account:
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self,amount):
#         self.bal+=amount
#         print('Balane after deposit',self.bal)

#     def withdraw(self,amount):
#         if(self.bal>=amount):
#             self.bal-=amount
#             print('Balance after withdraw:',self.bal)
#         else:
#             print('Insufficient amount in account')
#             print('Transaction Failed!!!')
#     def show(self):
#         print(f'Account Holder Name: {self.ac_holder} Account Balance {self.bal}')

# # # #ac1=Account('Sameer',50000)
# # # #ac2=Account('Chang',14000)
# # # #ac1.show()
# # # #ac2.show()
# ac1=Account('Sameer',50000)
# ac1.show()
# wamount=float(input('Enter amount to withdraw \t'))
# ac1.withdraw(wamount)

# # class Account:
# #     def __init__(self, balance, ac_holder):
# #         self.balance = balance
# #         self.ac_holder=ac_holder

# #     def get_balance(self):
# #         return self.balance
    
# # acc = Account(1000,'Sam')
# # acc.balance=34000
# # print(acc.balance)

#NUMBER 2
class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self,amount):
        self.bal+=amount
        print('Balance after deposit',self.bal)

    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after withdraw:',self.bal)
        else:
            print('Insufficient amount in account')
            print('Transaction Failed!!!')
    def show(self):
        print(f'Account Holder Name: {self.ac_holder} Account Balance {self.bal}')


#CONTOH2: ni kalau nak enter nama dan amount manual
# name = input("Enter account holder name: ")
# balance = float(input("Enter initial balance: "))
# ac = Account(name, balance)
# ac.show()

# CONTOH3: ni kalau nak enter nama manual but amount is fixed, tapi boleh letak satu nama je
# name = input("Enter account holder name: ")
# balance = 15000
# ac = Account(name, balance)
# ac.show()


#CONTOH1: ni sir ajar auto nama dan amount
ac=Account('Sam',15000)
ac.show()
ac1=Account('Raj',50000)
ac1.show()

print('Please choose\n 1.Deposit 2.Withdraw 3.Balance Info')
op=int(input())

if(op==1):
    damount=float(input('Enter amount to deposit'))
    ac.deposit(damount)
if(op==2):
    damount=float(input('Enter amount to withdraw:'))
    ac.withdraw(damount)
if(op==3):
    ac.show()
else:
    print('Wrong Choice')