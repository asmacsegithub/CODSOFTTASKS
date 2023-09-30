print("************************************************************************************************************************************")
print("----------------------------------------PYTHON PROGRAMMING TASK BY CODSOFT----------------------------------------------------------")
print("************************************************************************************************************************************")
print(" ")

print("------------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------PYTHON QUIZ GAME----------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------------------")

questions=("1. A string is immutable in Python Every time when we modify the string, Python Always create a new String and assign a new string to that variable",
           "2. What is a correct syntax to output **Hello World** in Python?",
           "3. How do you insert COMMENTS in Python code?",
           "4. Which one is NOT a legal variable name?",
           "5. How do you create a variable with the numeric value 5?",
           "6. What is the correct file extension for Python files?",
           "7. In Python, 'Hello', is the same as **Hello**",
           "8. Which method can be used to remove any whitespace from both the beginning and the end of a string?",
           "9. Which method can be used to return a string in upper case letters?",
           "10. Which method can be used to replace parts of a string?")

options=(("A. True","B. False","C. BOT","D. NOT"),
         ("A. echo(**hello world**);","B. echo **hello world**","C. print (**hello world**)","D. p (**hello world**)"),
         ("A. /*this is comment*/","B. #this is comment","C. //this is comment","D. <--this is comment/-->"),
         ("A. Myvar","B. my-var","C. _myvar","D. my_var"),
         ("A. x=int(5)","B. x=5","C. both a and b","D. none"),
         ("A. .pyt","B. .pyth","C. .py","D. .pt"),
         ("A. True","B. False","C. BOT","D. NOT"),
         ("A. len()","B. strip()","C. trim()","D. ptrim()"),
         ("A. upperCase()","B. upper()","C. uppercase()","D. toUpperCase"),
         ("A. replace()","B. repl()","C. switch()","D. replaceString()"),)

answers=("A","C","B","B","C","C","A","B","B","A")
guesses=[]
score= 0
question_no =0

for question in questions:
    print("-------------------")
    print(question)

    for option in options[question_no]:
        print(option)

    guess= input("Enter A,B,C or D:").upper()
    guesses.append(guess)
    if guess==answers[question_no]:
        score+=1
        print(" ")
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_no]} is the correct answer")
    question_no+=1

print("---------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------Result----------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------------------------")

print("asnwers:",end="")


for answer in answers:
    print(answer,end=",")
print(" ")
print("guesses:",end="")
for guess in guesses:
    print(guess,end=",")
print(" ")

score = int(score/len(questions)*100)
print(f"Your Score is:{score}%")


