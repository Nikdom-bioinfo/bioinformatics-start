# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}
print(country_capitals)
print(country_capitals["England"])

country_capitals["Italy"] = "Rome"
print(country_capitals)

del country_capitals["Germany"]
print(country_capitals)

country_capitals.clear()
print(country_capitals)

country_capitals1 = {
    "Germany" : "Heidelberg",
    "Italy" : "Rome",
    "England" : "London"
}
print(country_capitals1)

country_capitals1["Germany"] = "Berlin"
print(country_capitals1)

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

numbers = {5 : "five", 10 : "ten", 20 : "twenty"}
print(len(numbers))

file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}
print(".pdf" in file_types)       
print(".mp3" in file_types)       
print(".mp3" not in file_types)   

person1 = {"name": "Linus", "age": 21}
print(person1["name"])
print(person1["age"])

person1 = {"name": "Linus", "age": 21}
print(person1.get("name"))
print(person1.get("hobbies"))

person1 = {"name": "Linus", "age": 21}
print(person1.get("hobbies", ["dancing", "fishing"]))

person1["hobbies"] = ["dancing", "fishing"]
print(person1)

person1 = {"name": "Linus", "age": 21}
print(person1.pop("name"))
print(person1)

print(country_capitals.pop("Italy"))
print(country_capitals)

oiko = {"pateras" : "Dimitrakis", "mitera" : "vaso", "ader" : "fogalo"}
print(oiko)
for melos in oiko:
    print(melos)
for melos in oiko:
    print(oiko[melos])

synonyms = {"mountain": "peak", "forest": "jungle"}
print("1.", synonyms["mountain"])

synonyms["terrain"] = "land"
print("2.", synonyms)

print(synonyms.pop("forest"))
print(synonyms)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

dic1.update(dic2)
print(dic1)
dic1.update(dic3)
print(dic1)