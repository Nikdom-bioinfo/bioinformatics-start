def greet(name):
    print('Hello World', name)
greet('fot')
print('bla')

def add_numbers(num1, num2):
    sum = num1 +num2
    print('Sum: ', sum)
add_numbers(43, 42)

def find_square(num1, num2):
    result = num1 * num2
    return result

square = find_square(3, 5)

print('Square:', square)

def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)

number1 = 5.4
number2 = 6.7
add_numbers(number1, number2)

def find_average_mark(marks):
    average_mark = sum(marks)/ len(marks)
    return average_mark
def find_grade(average_mark):
    if average_mark >= 80:
        grade = 'A'
    elif average_mark >= 60:
        grade = 'B'
    elif average_mark >= 50:
        grade = 'C'
    else:
        grade = 'F' 
    return grade
marks = [55, 64, 75, 80, 65]
average_mark = find_average_mark(marks)
grade = find_grade(average_mark)
print('Your average maek is:', average_mark)
print('Your grade is:', grade)

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum
def multiply_numbers(num1, num2):
    product = num1 * num2
    return product

sum = add_numbers(32, 22)
product = multiply_numbers(32,22)
print('product', product)
print('SUm', sum)