def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')

def greet(name):
    print("Hello", name)

greet("Fogalo")

def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

add_numbers(4, 5)

def find_square(num):
    result = num * num
    return result
square = find_square(3)
print("Square: ", square)

def find_again(num1, num2):
    result = num1 * num2
    print("Result of this way is", result)
find_again(3, 3)

#Example: Marks

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)

    average_marks = sum_of_marks / number_of_subjects
    return average_marks

def compute_grade(average_marks):
    if average_marks >= 80:
        grade = "A"
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "F"

    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
grade = compute_grade(average_marks)

print("You're average mark is", average_marks)
print("You're grade is", grade)

def add_numbers(num1,num2):
    return num1 + num2
def multiply_numbers(num1, num2):
    return num1 * num2
number_1 = 5
number_2 = 37

sum_result = add_numbers(number_1, number_2)
print("Sum is: ", sum_result)
product_result = multiply_numbers(number_1, number_2)
print("Product is: ", multiply_numbers)

#Task

def add_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

number_1 = 7.4
number_2 = 20.3

sum_result = add_numbers(number_1, number_2)
print("The Sum is", sum_result)

product_result = multiply_numbers(number_1, number_2)
print("The Product is", product_result)

def multiply(*numbers):
    total =  1
    for number in numbers:
        total *= number
    return total
print(multiply(3, 4, 5, 6, 7))

def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)

# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers()

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Domenikioti', first_name = 'Fogalo')


def find_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    print("Sum: ", result)
find_sum(4, 5, 8)

x = 187
def test():
    x = 2
    print(x)

test()
print(x)

message = "hgywsau"

def greet():

    # local variable
    global message
    message = "gjcfh"
    
    print('Local', message)

greet()

print("Global", message)

# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocalbitches'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

def greet():
    global message
    message = "How are you?"
    print("Message inside function", message)

greet()
print("Message outside function:", message)

# global variable
d = 1 

def add():

    global d
    d = d + 2 

    print(d)

add()



# outside function 
def outer():
    po = 2

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal po

        po = 23
        print("inner:", po)

    inner()
    print("outer:", po)

outer()