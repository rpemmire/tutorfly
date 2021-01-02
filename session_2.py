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
- Working with strings
- Classes and intro to object oriented programming
'''

'''
#Dictionaries
#A list of key-value pairs
#example: key is Name, value is Kabir
KabirDict = {"name": "Kabir", 'gender': 'Boy'}
print(KabirDict['name'])
print(KabirDict["gender"])
#modifying a dictionary key
KabirDict["name"] = "Raghav"
#adding a key value pair
KabirDict["height"] = 4.2
print(KabirDict)


#sets
#a group of unordered data that does not have duplicates
mylist = ['kabir','Raghav','hello']
print(mylist)
myset = set(mylist)
print(myset)

#If else statements
number = 6
if number % 2 == 0:
	print("even")
else:
	print("odd")

variable = True
if type(variable) == str:
	print("string")
elif type(variable) == int:
	print("int")
else:
	if type(variable) == float:
		print("float")
	elif type(variable) == bool:
		print("bool")
	else:
		print("other")


#loops
#running a same function or set of lines multiple times
#while loop vs. for loop: while loop runs when a condition is true, for loop runs until there's nothing left
list = []

for i in range(10):
	list.append(i+1)
print(list)

i = 1
while i <= 10:
	list.append(i)
	i = i + 1
print(list)

#while loops that go on forever

q = 0
while q >=0:
	q+=1
print('done')

#while true (also goes on forever)
g = 0
while True:
	if g > 10:
		print(g)
		#use break to stop an infinite while loop
		break
	g+=1


#complex exercises with for and while loops
numbers = [3,2,6,'hi',4,7,9,23,'hello',45,46]
odd = []
even = []
string = []
for number in numbers:
	if type(number) == str:
		string.append(number)
	elif number % 2 != 0:
		odd.append(number)
	else:
		even.append(number)
print(odd)
print(even)
print(string)

#quick lesson on booleans

2 == 2 -> True
3 == 2 -> False
True == True -> True
False == False -> True
3 != 2 -> True


#finding the minimum value in a list
numbers = [20,3,4,6,1,8,30]
min = 1000000000000
for number in numbers:
	if number < min:
		min = number

#sorting a list
numbers = [20,3,4,6,1,8,30]
length_needed = len(numbers)
sortedList = []
while len(sortedList) < length_needed:
	min = 1000000000000
	minIndex = None
	for i in range(len(numbers)):
		if numbers[i] < min:
			min = numbers[i]
			minIndex = i
	numbers.pop(minIndex)
	sortedList.append(min)
print(sortedList)
'''
