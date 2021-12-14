# #Types of Function

# """
# Programming as 2 types of functions
# 1- Perform a task 
# 2- Calculate and return a value
# """
# #Greet Function
# def greet(name):
#     return f'Hi {name}'

# message = greet("Ebisintei Dennis")
# file = open('content.txt', "w")
# file.write(message)

# #Send Email File
# def send_email(email_address, mail_content):
#     return f"{email_address} {mail_content}"

# message = send_email("ebisinteidennis@gmail.com", "Hi this is my first Email address Function")
# file = open("mail.txt", "w")
# file.write(message)
# #End of Email function

# #keyword argument
# def increment(number, by):
#     return number + by
# print(increment(2,by=4)) # keyword argument


# #default argument
# def increment(number, by=2):
#     return number + by
# print(increment(2)) #Default Argument

# #Xargs
# def multiply(x,y):
#     return x * y
# print(multiply(2, 3))


#Iterate over the tuple
def multiply(*numbers):
    total = 1 
    for number in numbers:
        total *= number
    return total
print(multiply(2,3,4,5,6))
