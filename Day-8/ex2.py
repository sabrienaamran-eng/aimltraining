from ourpack import calc

# try:
#     fnum=float(input('Enter first number:'))
#     snum=float(input('Enter second number:'))
#     op=input('Choose operation +,-,*,/:\t')
#     if(op=='+'):
#         print('Result:\t',calc.add(fnum,snum))
#     elif(op=='-'):
#         print('Result:\t',calc.add(fnum,snum))
#     elif(op=='*'):
#         print('Result:\t',calc.multi(fnum,snum))
#     elif(op=='/'):
#         print('Result:\t',calc.div(fnum,snum))
#     else:
#         raise ValueError
    
# except ZeroDivisionError as ze:
#     print('Division by 0 not allowed',ze)
# except ValueError as ve:
#     print('Error in values',ve)
# except Exception as ex:
#     print('Error!!!',ex)
# finally:
#     print('End of Program')

#UNTUK CONTINUE
while True:
    try:
        fnum=float(input('Enter first number:'))
        snum=float(input('Enter second number:'))
        op=input('Choose operation +,-,*,/:\t')
        if(op=='+'):
            print('Result:\t',calc.add(fnum,snum))
        elif(op=='-'):
            print('Result:\t',calc.add(fnum,snum))
        elif(op=='*'):
            print('Result:\t',calc.multi(fnum,snum))
        elif(op=='/'):
            print('Result:\t',calc.div(fnum,snum))
        else:
            raise ValueError
    
    except ZeroDivisionError as ze:
        print('Division by 0 not allowed',ze)
    except ValueError as ve:
        print('Error in values',ve)
    except Exception as ex:
        print('Error!!!',ex)
    choice=input('Do you wanna continue if yes press y:\t').lower()
    if(choice!='y'):
        print('Bye')
        break