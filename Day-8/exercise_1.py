# Take user marks from user with 0 to 50
# if user enter outside [0-50] raise Error InvalidMarks using Custum Exception
# Give chance to the user till, he/she entered valid marks

# class InvalidMarks(Exception):
#     pass
# def check_marks(marks):
#     if(marks<0):
#         raise InvalidMarks('Marks should not be negative')
#     elif(marks>50):
#         raise InvalidMarks('Marks should be lesser than 50')
#     else:
#         print(f'Marks {marks} is accepted')

# from ourpack import mark #ni kalau import dari folder ourpack, kalau tak import pakai yang atas
# while True:
#     try:
#         usermarks=int(input('Enter your mark:'))
#         mark.check_marks(usermarks)
#     except mark.InvalidMarks as e:
#         print('Invalid Marks:',e)
#     except Exception as ex:
#         print('Error !!!',ex)
#     else:
#         print('Recorded')
#         break
#     choice=input('Do you wanna re-enter marks? if yes press y:\t').lower()
#     if(choice!='y'):
#         print('Bye')
#         break

#CONTOH SURUH RE-ENTER JUGA MARKS TANPA TANYA
from ourpack import mark #ni kalau import dari folder ourpack, kalau tak import pakai yang atas
while True:
    try:
        usermarks=int(input('Enter your mark:'))
        mark.check_marks(usermarks)
    except mark.InvalidMarks as e:
        print('Invalid Marks:',e)
    except Exception as ex:
        print('Error !!!',ex)
    else:
        print('Recorded')
        break
    choice=input('Please re-enter your marks by press +\t')
    if(choice!='+'):
        print('Bye')
        break