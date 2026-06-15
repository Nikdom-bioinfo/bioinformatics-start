# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }
print('Data type of empty_set:', type(empty_set))
print('Data type of empty_dictionary:', type(empty_dictionary))

numbers = {1,2,4,5,2,5,8,7,8}
print(numbers)
numbers.add(23)
print(numbers)

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)
print(companies)

companies.discard('Lacoste')
print(companies)

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
tyvgh = languages.discard('Java')

print('Set after remove():', languages)

for company in companies:
    print(company)
print(len(companies))

A = {1, 3, 5}
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B)) 

A = {1, 3, 5}
B = {1, 2, 3}

print('Intersection using &:', A & B)
print('Intersection using intersection():', A.intersection(B)) 

A = {2, 3, 5}
B = {1, 2, 6}
print('Difference using -:', A - B)
print('Difference using difference():', A.difference(B)) 
print('sameb', B.difference(A))

A = {2, 3, 5}
B = {1, 2, 6}
print('using ^:', A ^ B)
print('using symmetric_difference():', A.symmetric_difference(B)) 

A = {3, 5, 9}
B = {3, 4, 9}
if A == B:
    print('they are equal')
else:
    print('they are not equal dymmy')

companies.add("fogalo")
print(companies)

animals = {"dog", "tiger", "elephant"}
wild_animals = ["tiger", "leopard", "elephant"]

animals.update(wild_animals)
print(animals)

animals.update(wild_animals, {"lion"})
print(animals)

animals = {"tiger", "cat", "elephant", "dog"}
animals.discard("ferret")
print(animals)

animals = {"tiger", "cat", "elephant", "dog"}
animals.clear()

print(animals)

animals = {"tiger", "cat", "elephant", "dog"}
print("tiger" in animals)
print("ferret" in animals)

domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}

animals1 = domestic_animals.union(wild_animals)
print(animals1)
animals2 = domestic_animals | wild_animals
print(animals2)

common_animals = domestic_animals.intersection(wild_animals)
print(common_animals)
common_animals1 = domestic_animals & wild_animals
print(common_animals1)

animals = {"dog", "cat", "tiger", "elephant", "dog"}
print("1.", animals)

animals.remove("cat")
animals.remove("dog")
print("2.", animals)

animals.add("snake")
print("3.", animals)

result = {1, 5, 10} & {100, 10, 3, 5}
print("4.", result)