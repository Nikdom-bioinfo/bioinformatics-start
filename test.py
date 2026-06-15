
for i in range(5):
    print(i)

languages = ["Python", "Java", "Swift", "C", "C++"]

for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)

languages = ['Swift', 'Python', 'Go', 'C++']

for lang in languages:
    if lang == 'Go':
        continue
    print(lang)

    # outer loop 
attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']

for attribute in attributes:
    for car in cars:
        print(attribute, car)
    
    # this statement is outside the inner loop
    print("-----")


for count in range(1, 5):
    print(count)



result = range(11)

result = list(result)
print(result)

result = list(range(1, 11, 3))
print(result)

result = list(range(5, -6, -1))
print(result)

result = list(range(3, 31, 3))
print(result)

print("This is \"good\"")

import re
seq = 'tagctagcggagctatcgatcg' # Der String, in dem gesucht werden soll 
r = re.search(r'gg[gtac]gc[gcat]', seq) # Der Suchausdruck wird als "raw"-String formuliert
print('Treffer von ' + str(r.start()) + ' bis ' + str(r.end()) + ' ist ' + r.group()) 

print("banana".split("a"))

a = 'tagctagtcgatgc'
b = 'nnnnnnnnnnnnnn'

print(a + b)
print(a, b, sep='')
gatcrn = '\r\natgctagcta\r\ntcgatgctactactagc\r\ntagctactagcatc'
print(gatcrn.replace('\r', ''))

gatc = 'ATCGTAGCTAGCTAGCTAGCTAGCGGAATGCTAGCTGATCGATCGCCTTATCGATCTACTATCTC'
intron= "TGCTAGCTGATCGATCG"
print(gatc.replace(intron, intron.lower()))

gatc = 'gatcgatgctactaAGCATGCTAGCgcgtagagtctaggagctgctgtctagagtaTAGCTAGCTATCcctgagcatcgtctgtgagattctcgtagagctgat'
gatc.lower()
print("A: ", gatc.count('a'))

gauc = 'gatcgatgctactaAGCATGCTAGCgcgtagagtctaggagctgctgtctagagtaTAGCTAGCTATCcctgagcatcgtctgtgagattctcgtagagctgat'
gauc = gauc.replace('T', 'U')
gauc = gauc.replace('t', 'u')
print(gauc)

mittel = 'gcguagagucuaggagcugcugucuagagua'
gauc = gauc.replace(mittel, 'n' * len(mittel))
print(gauc)
gatc = 'gatcgatgctactanAGCATGCTAGCngcgtagagtctaggagctgctgtctagagtanTAGCTAGCTATCncctgagcatcgtctgtgagattctcgtag' # Die kleinen n sind Trenner.
teile = gatc.split('n')
for i in range(len(teile)):
    print(f'>seq{i+1}')
    print(teile[i])
gatc = 'gatcggatgctacggtanAGCATGGCTAGCngcggtagagtctaggagctgctgtctagagtanTAGCTAGGGGACTATCncctgagcatcggtctgtgagattctcgtag'
import re
print(re.sub(r'GG[ACGT]', 'GGG', gatc))

gatc = 'CTACGGTANAGCATGGCTAGCNGCGGTAGAGTCTAGGAGCTGCTGTCTAGAGTANTAGCTAGGGGACTATCNCCTGAGCATCGGTCTGTGAGATTCTCGTAG'
neu = ''

for i in range(0, len(gatc), 3):
    neu += gatc[i:i+3][::-1]

print(neu)

alphabet = list('abcdefgh')
print(alphabet[4])

alfa = []
for i in range(65, 78):
    alfa.append(chr(i))
print(alfa)
zeichen = alfa[7]
print(ord(zeichen), zeichen)
text = ''.join(alfa)
print(alfa)
elemente_vorhanden = ['C', 'F', 'X']
for element in elemente_vorhanden:
    print(element in alfa)

gatc = 'gatcggatgctacggtanAGCATGGCTAGCngcggtagagtctaggagctgctgtctagagtanTAGCTAGGGGACTATCncctgagcatcggtctgtgagattctcgtag'
import re
print(re.sub(r'gg[acgt]', 'GGG', gatc))