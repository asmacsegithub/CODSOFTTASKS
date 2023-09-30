print("************************************************************************************************************************************")
print("----------------------------------------PYTHON PROGRAMMING TASK BY CODSOFT----------------------------------------------------------")
print("************************************************************************************************************************************")
print(" ")

print("------------------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------RANDOM PASSOWARD GENERATOR----------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------------")

import random

charcters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_"
while True:
    pass_length=int(input("Enter the Length Required for Passoward:-"))
    pass_count=int(input("Enter the no of Passoward:-"))

    for i in range(0,pass_count):
        passoward=""
        for j in range(0,pass_length):
            pass_char=random.choice(charcters)
            passoward=passoward+pass_char
        print("The Generated Passoward is:-",passoward)
    repeat=input("Do you want to generate more passoward?")
    if repeat=="no" or repeat=="NO":
        break

print("Thank You")
