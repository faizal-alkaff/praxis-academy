print("=== memanggil fungsi ===")
def greeting():
	print("Hello World")
	
greeting()

print("\n=== menetapkan fungsi kedalam variable ===")
def square(x):
    return x * x
    
print(square(5))

foo = square
print(foo(6))

print("\n=== fungsi sebagai parameter ===")
def formalGreeting():
    print("How are you?")
    
def casualGreeting():
    print("What's up?")
    
def greet(type, greetFormal, greetCasual):
    if type == 'formal':
        greetFormal()
    elif type == 'casual':
        greetCasual()

greet('casual', formalGreeting, casualGreeting)

print("\n=== tanpa fungsi tingkat tinggi ===")
print("##contoh manipulasi list tanpa fungsi map 1##")
arr1 = [1, 2, 3, 4]
arr2 = []

for i in range(len(arr1)):
    arr2.append(arr1[i] * 2)
    
print(arr2)

print("\n##contoh manipulasi list tanpa fungsi map 2##")
birthYear = [1975, 1997, 2002, 1995, 1985, 1945]
ages = []

for i in birthYear:
    age = 2018 - i
    ages.append(age)
    
print(ages)

print("\n##contoh filter dict tanpa fungsi filter 1##")
persons = [
    { 'name': 'Peter', 'age': 16 },
    { 'name': 'Mark', 'age': 18 },
    { 'name': 'John', 'age': 27 },
    { 'name': 'Jane', 'age': 14 },
    { 'name': 'Tony', 'age': 24 },
    { 'name': 'Andi', 'age': 22 }]
fullAge = []

for person in persons:
    if person['age'] >= 18:
        fullAge.append(person)

print(fullAge)

print("\n##contoh sum list tanpa fungsi reduce 1##")
arr = [15, 17, 11, 18, 14]
sum = 0

for i in range(len(arr)):
    sum = sum + arr[i]

print(sum)

print("\n=== menggunakan fungsi built-in map ===")
print("##contoh list 1##")
arr1 = [1, 2, 3, 5]
arr2 = list(map(lambda x: x * 2, arr1))

print(arr2)

print("\n##contoh list 2##")
birthYear = [1975, 1997, 2002, 1995, 1985, 1990]
age = 2018
ages = list(map(lambda x: age - x, birthYear))

print(ages)

print("\n=== menggunakan fungsi built-in filter ===")
print("##contoh dict 1##")
persons = [
  { 'name': 'Peter', 'age': 16 },
  { 'name': 'Mark', 'age': 18 },
  { 'name': 'John', 'age': 27 },
  { 'name': 'Jane', 'age': 14 },
  { 'name': 'Tony', 'age': 24 },
  { 'name': 'Joko', 'age': 33 }]

fullAge = list(filter(lambda person: person['age'] >= 18, persons))
print(fullAge)

print("\n=== menggunakan fungsi built-in reduce ===")
print("##contoh reduce list 1##")
from functools import reduce
arr = [25, 27, 21, 28, 24]
sum = reduce(lambda x, y: x + y, arr)

print(sum)

print("\n=== membuat fungsi sendiri ===")
strArray = ['JavaScript', 'Python', 'PHP', 'Java', 'C']

def mapForEach(arr):
    newArray = []
    for i in arr:
        newArray.append(len(i))
    return newArray
    
lenArray = mapForEach(strArray)
print(lenArray)