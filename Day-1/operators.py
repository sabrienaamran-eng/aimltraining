# #Assignment operators: =, +=, -=
# price=float(input("Enter Product Price"))
# discount=price*0.10
# disPrice=price-discount
# print(f"price: {price} \n Discount: {discount} \n DiscountedPrice:{disPrice}")

# salary=50000.50
# bonus=5000.60
# print(f"salary {salary} and bonus {bonus}")
# salary+=bonus #salary=salary+bonus
# print("salary with bonus", salary)

# salary=50000.50
# tds=5000.60
# print(f"salary {salary} and TDS {tds}")
# salary-=tds #meaning of salary+=bonus => salary=salary-tds
# print("salary after tax", salary)

#Comparison operators: ==, >, >=, <. !=etc.
# #code
# else
# #code

# age=int(input("Enter your age"))
# if(age>=18):
#    print("You are eligible to cast your vote")
# else:
#    print("You are not eligible to cast your vote, You have to wait")
#    print("End of Program")

# marks=int(input("Enter marks percentage without '%' sign"))
# if(marks<30):
#     print("Fail in Exam")
# else:
#     print("Clear the exam")

# ! means not equal
# accessCode="wes12"
# accessCode=input("Enter Access Code:\t")
# if(accessCode!="wes12"):
#     print("Invalid Access Code")
# else:
#     print("Welcome to Your Course")

# 

# #Logical operators: and, or, not.
# phyMarks=int(input("Enter marks obtained in Physics"))
# cheMarks=int(input("Enter marks obtained in Chemistry"))
# mathMarks=int(input("Enter marks obtained in Mathematics"))

# if((mathMarks>=50) and (phyMarks>=55) and (cheMarks>=60)):
#     print("You are eligible to sit in pre exam of MBBS")
# else:
#     print("You have not got the required marks")

# idProof=input("Enter Id proof you have")
# if((idProof=="passport")or(idProof=="dl")or(idProof=="voter id")):
#     print(f"valid Id {idProof} we accept here")
# else:
#     print("Only passport, dl and voter id are accepted as Identity Proof")
#     print(f"{idProof}: is not valid ID here")

mathMarks=int(input("Enter marks obtained in Mathematics: \t"))
gapYear=int(input("Enter Year gap if any otherwise Zero: \t"))
if((mathMarks<=55) and (gapYear!=0)):
    print("Not Eligible for BTech")
else:
    print("Eligible for Btech")


