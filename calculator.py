print("************************************************************************************************************************************")
print("----------------------------------------PYTHON PROGRAMMING TASK BY CODSOFT----------------------------------------------------------")
print("************************************************************************************************************************************")
print(" ")

print("-------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------")
print("------------BASIC CALCULATOR FOR ADDITION,SUBTRACTION,MULTIPLICATION,DIVISION,EXPONENT AND FLOOR DIVISION----------------")
print("-------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------")
print(" ")

while True:
    print(" ")
    a=int(input("Enter Your First Operand:-"))
    b=int(input("Enter Your Second Operand:-"))
    c=(input("Enter Your Operator:-"))

    if c=="+":
        print("Addition of",a,"and",b,"is",a+b)

        print(" ")
    elif c=="-":
        print("Addition of",a,"and",b,"is",a-b)

        print(" ")
    elif c=="*":
        print("Addition of",a,"and",b,"is",a*b)

        print(" ")
    elif c=="/":
        print("Addition of",a,"and",b,"is",a/b)

        print(" ")
    elif c=="**":
        print("Exponent of",a,"and",b,"is",a**b)

        print(" ")
    elif c=="//":
        print("Floor Division of",a,"and",b,"is",a//b)

        print(" ")

    else:
        print("invalid choice")
        print(" ")
    repeat=input("Do you want to calculate again?")
    if repeat=="no" or repeat=="NO":
        break

print("Thank You")
