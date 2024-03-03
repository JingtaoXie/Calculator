
def printResult(result):
    print(result)

def plus(num1,num2):
    sumvalue=float(num1)+float(num2)
    return sumvalue

def minus(num1,num2):
    differencevalue=float(num1)-float(num2)
    return differencevalue

def mutiple(num1,num2):
    mutiplevalue=float(num1)*float(num2)
    return mutiplevalue

def divisor(num1,num2):
    if(num2!=0):
     dividevalue=float(num1)/float(num2)
     return dividevalue


def ask_continue():
        print("Continue? Y/N")
        cancontinue = input().upper()
        if cancontinue == "Y":
            return True
        else:
            return False

