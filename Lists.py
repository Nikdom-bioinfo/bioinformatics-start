jbas = [567, 897, 8, 90]
print(jbas)
print('jb =', jbas[-3])

# a list containing strings, numbers and another list
student = ['Jack', 32, 'Computer Science', [2, 4]]
print(student)

# an empty list
empty_list = []
print(empty_list)

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list =", my_list)

# get a list with items from index 2 to index 4 (index 5 is not included)
print("my_list[2: 5] =", my_list[2: 5])    

# get a list with items from index 2 to index -3 (index -2 is not included)
print("my_list[2: -2] =", my_list[2: -2])  

# get a list with items from index 0 to index 2 (index 3 is not included)
print("my_list[0: 3] =", my_list[0: 3])

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list =", my_list)

# get a list with items from index 5 to last
print("my_list[5: ] =", my_list[5: ])

# get a list from the first item to index -5
print("my_list[: -4] =", my_list[: -4])

print("my_list[:] =", my_list[:])

sminars = [ 'sc', 'imm', 'phy']

print('phy'in sminars)

for seminar in sminars:
    print(seminar)

print('lenght: ' , len(sminars))
print('original_list: ' , sminars)
sminars.insert(2, 'path')
print('new: ' , sminars)
sminars[1:3] = ['huds', 'sdskam']
print(sminars)

sminars[0] = 'stem'
print(sminars)

sminars.remove('stem')
print(sminars)

del sminars[0]
print(sminars)

sminars1 = sminars.copy()
print(sminars1)

numbers = [1, 3, 5]
print('Numbers:', numbers)

even_numbers  = [2, 4, 6]
print('Even numbers:', numbers)

numbers.extend(even_numbers)

print('Updated Numbers:', numbers) 

languages = ["Python", "JavaScript", "C++", "Kotlin"]

# first to third element
print(languages[:0])

# second to last element
print(languages[3:])

lists = [4, 2, 7, 5, 9, 1]
lists.sort()
print(lists)
lists.reverse()
print(lists)

languages = ('Python', 'Swift', 'C++')

print(languages[0])   

print(languages[2])   # C++
fruits = ('apple','banana','orange')
for fruit in fruits:
    print(fruit)

greet = 'Hello'

# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"

# multiline string 
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)
str1 = '4rfwe'
str2 = 'haha'
str3 = 'haha'
print(str1 == str2)
print(str3 == str2)
geia = 'geia'
onoma = 'fogalo'
resut = geia + onoma
print(resut)
for gramma in onoma:
    print(gramma)

print('a' in 'program') 
print('at' not in 'battle') 
onomadio = onoma.upper()
print(onomadio)
name = 'fogalo'
place = 'spiti'
print(f'{name} is in {place}')

# escape double quotes
example = "He said, \"What's there?\""
print(example)
# escape single quotes
example1 = 'He said, "What\'s there?"'
print(example)

text1 = "Python"
text2 = "Programming"
result = text1 + " " + text2
print(result)

text1 = "Python "
text2 = "Programming"
result = text1 + text2
print(result)

text1 = "Python"
text2 = "Programming"
results = (text1 + text2) * 3
print(results)

text = "I no like Python 3"
result = text.find("Python")
print(result)

text = "I like Python 3"
result = text.replace("Python 3", "Java")
print(result)

quote = "Talk is cheap. Show me the code."

print("1.", quote[3])
print("2.", quote[-3])
print("3.", quote.replace("code", "program"))

result = range(1, 11)
# converting to list
result = list(result)
print(result)