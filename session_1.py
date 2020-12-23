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
- Functions to run different scripts
- Working with strings
- Classes and intro to object oriented programming
'''

'''
#Variables
	#initialize Variables
	hello = "Hello"
	hi = 3
	height = 4.2
	weight = 100
	#operations on Variables
	#+=/*
	L = 3
	W = 4
	A = L*W
	#% means finding the remainder


#Data types
	#strings, integers, floats, booleans, None
	S = "String"
	I = 3
	F = 7.33
	B = True
	Nothing = None
	#difference between a float and a integer
	number1 = 5.3
	number2 = 10
	#print(int(number1))
	#print(float(number2))
	#turning numbers into strings
	#print(S + " " +  str(F))
	#print(str(Nothing))

#Data Structures
#Lists
	#Lists with strings
	MyList = ["hello", "hello", "bye", "hi", "Kabir", "raghav"]
	#print(len(MyList))
	LastName = "Raghav"
	#adding things to lists
	MyList.append(LastName)
	#removing from a list by value (removes the first object with that value)
	MyList.remove('hello')
	#removing by index or slice (del vs pop) pop can store the variable
	del MyList[3]
	fourthObject = MyList.pop(3)
	#deleting the last object when you don't know the length of the list
	lastObject = MyList.pop(-1)

	#Lists with numbers
	MyList = []
	MyList = [0]*10 # a list of 5 0s
	MyList = list(range(10)) # a list from 0 to 4
	#changing values in lists/ indexing into lists
	MyList[-1] += 1
	print(MyList)
	#slicing lists (getting certain values)
	smallerList = MyList[0:5]
	#slicing when we don't know the length of our list
	smallerList = MyList[:5] #getting first 5 in the list
	smallerList = MyList[-5:] #getting last 5 in the list

	#list operations
	MyList = [1,3,6,2,4,1,7,9]
	MyList.sort()
	MyList.reverse()

	#inserting things into lists
	MyList.insert(1,4) #inserting a 4 at index 1
	print(MyList)


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

'''
