'''
Introductory Topics to cover
- Variables: Initializing, storing values, and operations
- Data types: ints, strings, floats
	What they are and converting between data types
- Data Structures
	- Lists and indexing
		Creating, editing lists
	- Dictionaries, sets
- Comprehension
	- If else statements
		Applications to variables
	- For and While loops
		Reading and writing lists, doing complex operations
		Using range backwards, with skips, etc.
	- Try and except
- Functions to run different scripts
- Classes and intro to object oriented programming
- Working with strings
'''


#sort a list (with a for loop)
numbers = [20,3,4,6,1,8,30]
minIndex = None
SortedList =  []
lengthNeeded = len(numbers)
for number in range(lengthNeeded):
	min = 1000000000000
	for i in range(len(numbers)):
		if min >= numbers[i]:
			min = numbers[i]
			minIndex = i
	SortedList.append(numbers.pop(minIndex))
print(SortedList)

#sort a list with a while loop
numbers = [20,3,4,6,1,8,30]
minIndex = None
SortedList =  []
lengthNeeded = len(numbers)
while len(numbers) != 0:
	min = 1000000000000
	for i in range(len(numbers)):
		if min >= numbers[i]:
			min = numbers[i]
			minIndex = i
	SortedList.append(numbers.pop(minIndex))
print(SortedList)

#try and except
number = '5'
try:
	new_number = number % 2
	print(new_number)
except:
	new_number = int(number)
	new_number = new_number % 2
	print(new_number)


#functions
def hello_world():
	print("hello world")

hello_world()

#parameters/arguments - functions can take in certain specifications
def printText(text):
	print(text)

printText("kabir")

def human(name,wieght,hight):
	dict = {}
	dict["name"] = name
	dict["hight"] = hight
	dict["wieght"] = wieght
	return dict

newDict = human("kanir", 68, 23)
printText(newDict)

def sortList(numbers):
	minIndex = None
	SortedList =  []
	lengthNeeded = len(numbers)
	while len(numbers) != 0:
		min = 1000000000000
		for i in range(len(numbers)):
			if min >= numbers[i]:
				min = numbers[i]
				minIndex = i
		SortedList.append(numbers.pop(minIndex))
	print(SortedList)

sortList([3,23,4,32,3,2])
