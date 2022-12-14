"""
DICTIONARY

    word : meaning
    Key : Value
    A dictionary is a Key value pair

    Key1 : Value1
    Key2 : Value2
    Key3 : Value3

    1.Dictionary is used to represent a key value pairs
    2.We can use duplicate values but cannot use keys
    3.Insertion order is not preserved because dictionary is based on Hashcode of keys
    4.Indexing and slicing operations are NOT allowed
    5.For both keys and values ,HETEROGENOUS values are allowed
    6.Dictionary is mutable in nature (CRUD) - UPDATE options are allowed
    7.Key value pairs are represented using curley braces


"""

# Different ways to create a dictionaries

# 1.Creating an empty dictionary

database = {}
print(database)
print(type(database))

db = dict()
print(type(db))

# 2. If the data is available , : Colon is used for mapping of keys with the values
db2 = {
    "name": "Steve Jobs",
    "salary": "10000000"

}
print(db2)  # {'name': 'Steve Jobs', 'salary': '10000000'}
print(type(db2))

#3.Converting other data types
#Convert list to dictionary
db3=[(1,"Ashish"),(2,"Steve Jobs"),(3,"Bill Gates")] #list of tuple [(1, 'Ashish'), (2, 'Steve Jobs'), (3, 'Bill Gates')]
print(db3)
db4=dict(db3)
print(db4) #{1: 'Ashish', 2: 'Steve Jobs', 3: 'Bill Gates'}

#Tuple of Tuple to Dictionary
data=((1,"Simon",2323.23838,3),3283,3434,347734) #((1, 'Simon', 2323.23838, 3), 3283, 3434, 347734)
print(data)

#db5=dict(data) #ValueError: dictionary update sequence element #0 has length 4; 2 is required
#print(db5)
#print(type(db5))

#List of tuple
#List of List
#Tuple of List
#Set of Tuple

#Using the dynamic input
db7=input("Enter the dictionary- ")
print(db7)
print(type(db7))

