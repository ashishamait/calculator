import math
print ("Are you having an error message? \nPlease read instructions in the code for help \n*************************")
firstNumber = float(input())
op = input().lower()
secondNumber = float(input())

if op == "+":
    print (firstNumber, "+", secondNumber, "=", firstNumber + secondNumber )
elif op == "-": 
    print (firstNumber, "-", secondNumber, "=", firstNumber - secondNumber )
elif op == "*":
    print (firstNumber, "*", secondNumber, "=", firstNumber * secondNumber )
elif op == "/":
    print (firstNumber, "/", secondNumber, "=", firstNumber / secondNumber )
elif op == "^":
    print (firstNumber, "^", secondNumber, "=", firstNumber ** secondNumber )
elif op == "r":
    print (firstNumber, "root", secondNumber, "=", secondNumber ** (1 / firstNumber) )
elif op == "%":
    print (firstNumber, "%", secondNumber, "=", firstNumber % secondNumber )
#factorial
elif op == "!":
    theNumber = firstNumber = secondNumber 
    secondNumber = 1
    while firstNumber > 1:
        secondNumber *= firstNumber 
        firstNumber = firstNumber - 1  
    print ("n!(", theNumber, ")=", secondNumber )
elif op == "sin":
    print ("sin(", secondNumber, ")=", math.sin(secondNumber ))
elif op == "cos":
    print ("cos(", secondNumber, ")=", math.cos
    (secondNumber ))
elif op == "tan":
    print ("tan(", secondNumber, ")=", math.tan(secondNumber ))
elif op == "pie" or op == "pi":
    print ("Pie =", math.pi)
elif op == "e":
    print = ("E =", math.e)
elif op == "ln":
    print ("ln(", secondNumber , ")= ", math.log(secondNumber))
else:
    print ("incorrect operator") 
