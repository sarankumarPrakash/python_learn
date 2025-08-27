# Primitive Data Types

#num=45
#mark=98.6

# print(type(num),type(mark))

# non-primitive data types

# collection of multiple value nan single varibable 

# List     []   => Orderedand changeable Duplicates OK
# set      {}   => unOrdered and imutable , but Remove /Add Ok. No duplicates.
# Tuples   ()   => Ordered and Unchangeable . Duplicate Ok . Faster 


# List :
# fruits = ["apple","orange","grapes","banana","orange","banana"]

#print(fruits[2])
#print(dir(fruits))  # shows what are the attributes and methods
#print(help(fruits))  # shows what are the methods withusage
#print(len(fruits)) # shws how may data contains 
#print("apple" in fruits)  # boolean=> wheather present / not .

#fruits[0]="pinrapple" # change value at index 0
#print(fruits)
#fruits.insert(0,"kiwi") # add at specific index
#fruits.append("mango")  # add at end 
#fruits.sort()  # sort in ascending order
#fruits.remove("banana") # remove specific item  
#fruits.pop() # remove last item
#fruits.clear() # remove all items
#fruits.reverse() # reverse the order
#fruits.extend(["papaya","chikoo"]) # add multiple items at end
#print(fruits.index('banana')) # gives index of specific item
#print(fruits.count("banana")) # count how many times item present

#print(fruits)


# set

#fruits = {"apple","orange","grapes","banana","orange","banana"}
#print(dir(fruits))  # shows what are the attributes and methods
#fruits.add("mabgo")
#fruits.remove("banana") # remove specific item
#fruits.pop() # remove random item
#fruits.clear() # remove all items
#print("banana" in fruits)  # boolean=> wheather present / not .


#print(fruits)

# frozenset => it is same as set but immutable
#fruits = frozenset({"apple","orange","grapes","banana","orange","banana"})
#vegitables = frozenset({"carrot","potato","tomato"})
#allItems = fruits.union(vegitables) # combine two frozenset

#print(dir(allItems))  # shows what are the attributes and methods
#print(allItems)
#print( fruits | vegitables) # combine two frozenset
#print( fruits & vegitables) # common items in two frozenset
#print( fruits - vegitables) # items in first but not in second frozenset
#print( fruits ^ vegitables) # items in first and second but not in both frozenset
#print(len(fruits)) # shws how may data contains 
#print("banana" in fruits)  # boolean=> wheather present / not .
#print(fruits.isdisjoint(vegitables)) # boolean => wheather two frozenset have no items in common
#print(fruits.issubset(allItems)) # boolean => wheather frozenset is subset of another frozenset
#print(fruits.issuperset(vegitables)) # boolean => wheather frozenset is superset of another frozenset


# Tuples : 

#fruits = ("apple","orange","grapes","banana","orange","banana")
#print(dir(fruits))  # shows what are the attributes and methods
#print(len(fruits)) # shws how may data contains 
#print(fruits.count("banana")) # count how many times item present
#print(fruits.index('banana')) # gives index of specific item

#Dictionary : { key : value , key : value }

#student ={
#   "name":'john',
#    "age":25, 
#    "courses":['math','compSci']
#}

#print(student)
#print(dir(student))  # shows what are the attributes and methods
#print(student['name'])  # access value by key
#print(student.get('age'))  # access value by key
#student.update({'age':26,'phone':'555-5555'}) # update existing key or add new key value pair
#student['email']='admin@gmail.com' # add new key value pair
#print(student)
#student.pop('courses') # remove specific key value pair
#print(student)  
#student.popitem() # remove last inserted key value pair
#print(student)
#print(len(student)) # shws how may key value pairs contains
#print("name" in student)  # boolean=> wheather key present / not .
#print(student.keys()) # list of all keys
#print(student.fromkeys(['name','age','phone'])) # create new dictionary with given keys and values None
#print(student.items()) # list of all key value pairs
#print(student.setdefault('email')) # returns value of specified key. If key does not exist, insert key with value None
#print(student.values()) # list of all values




# Range 

#numbers = range(1,10) # start to end-1
#evenNumbers = range(2,21,2) # start to end-1 with
#oddNumbers = range(1,21,2) # start to end-1 with step
#print(dir(oddNumbers))  # shows what are the attributes and methods


# for num in range(1,21,2):
#     print(num)





