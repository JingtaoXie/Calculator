import function

num1=''
num2=''
result=''
operation=''


print("Welcome to calculator")
ifcontinue=True

try:
 while ifcontinue:
    print("Please input what operation you want to do")
    print(" A.plus\n B.minus\n C.mutiple\n D.divide")
    operation=input().upper()
    if operation=="A":
        print("Please enter the first number")
        num1=input()
        print("Please enter the second number")
        num2=input()
        result=function.plus(num1,num2)
        function.printResult(result)
        ifcontinue=function.ask_continue()
    elif operation=="B":
        print("Please enter the first number")
        num1 = input()
        print("Please enter the second number")
        num2 = input()
        result = function.minus(num1,num2)
        function.printResult(result)
        ifcontinue = function.ask_continue()
    elif operation=="C":
        print("Please enter the first number")
        num1 = input()
        print("Please enter the second number")
        num2 = input()
        result = function.mutiple(num1,num2)
        function.printResult(result)
        ifcontinue = function.ask_continue()
    elif operation=="D":
        print("Please enter the first number")
        num1 = input()
        print("Please enter the second number")
        num2 = input()
        # if num2==0:
        #     print("Error: the divisor can not be zero, please input again")
        #     num2=input()
        result = function.divisor(num1, num2)
        function.printResult(result)
        ifcontinue = function.ask_continue()
 else:
     print("Thank you for your using, Bye Bye!")
except:
    print("Your input is not correct, please input again")
