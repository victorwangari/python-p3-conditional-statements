#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "ADMIN"and password == "12345":
        return "Access granted"
    elif username == "sudo" and password == "12345":
        return "Access denied"
    elif username == "admin" and password =="12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
   if temperature < 40:
    return "It's brisk out there!"
   elif temperature >40 and temperature < 65:
    return "It's a little chilly out there!"
   elif temperature > 85 :
    return "It's too dang hot out there!"
   else:
    return "It's perfect out there!"
   
    # your code here
    pass

def fizzbuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    
    return num
def calculator(operation, num1, num2):
    if operation == "+":
       return num1 + num2
    elif operation == "-":
       return num1 - num2
    elif operation == "*":
       return num1 * num2
    elif operation == "/":
       return num1 / num2
    else:
       print("Invalid operation!")
    
    
    # your code here
    pass
