#print("This is file 2")
#print(100)

#PYTHON Lists, []

#a = [] #empty list
#print(a)
#b = [1, "string", 2.3] #a list can contain different data types
#print(b)
#print("John" in b)

#print(b[0]) #first element starts at position 0
#print(b[-1]) #the last elemt starts at positon -1

#print(b[0])
#print(b[1])
#print(b[2])

#print("negative")
#print(b[-1])
#print(b[-2])
#print(b[-3])

#Slice a list
#print(b[1:])
#print(b[-3:])

#add to a list, append or insert
#print(b)
#b.append("Jesus")
#print(b)
#b.insert(4, "Christ") #4 is the index position
#print(b)

#print("length of the string is",len(b)) #get the length of the string

#replace item on the list, : it's the range not a direct index replacement
#b[2:4] = ["My", "Lord"] 
#print(b)

#delete list
#b[0:] = []
#del(b[1])
#print(b)

#list within a list, multi dementional list
#c = [a, b]
#print(c)
#print(c[0])
#print(c[1])
#print(c[1][2])

#list can refer to itself
#c.append(c)
#print(c) #three dots means a self reference, pointer to itself
#print(c[2][1][1][1])

#print(c[2])

#PYTHON sets, {}
#insertion order is not maintain, only unique, no repeats
#sets is useful for look up operation, it optimize performance
#a = set()
#b = {1, "John", 9.9, "John", "John", "Luke", True}
#True will not print because True equals the numeric value 1
#print(a)
#print(b)
#print("John" in b) #the "in" keyword to see if the item exist in the set
#print(c[1])
#print("My" in c[1])

#PYTHON Dictionary, consist of key value pairs, data must be immutable a={}
#keys can be string or number, each key needs to be unique, each values doesn't need to be unique

#a = {}
#b = {'a': 1, 'b':2, 'c':3}
#print(b)

#print(b['a'])
#b['a'] = "Amos"
#print(b)

#insert new value onto set
#b[15] = 5
#print(b)

#get the list of all the keys
#print(list(b))

#delete from dictionaries
#del(b[15]) #passing in the dictionarie b with the key 15

#print(list(b))
#print('d' in b)

#PYTHON data type - Tuples, immutable data type used to sort Python objects
#can store values of different data type
#t = 1, 2, 3, 4
#print(t)
#print(t[0])

#recursive, new tuple refering to an exiting tuple
#u = 7, t

#empty typle being created 
#empty = ()
#print(empty)

#t2 = 'Lord' #string
#t3 = 'Jesus', #tuple, with the comma appended

#print(len(t3)) #length of the tuple

#PYTHON function
#def lord(s):
#    return "LORD " + s

#print(lord("Jesus"))

#def add(x, y):
#    return x + y, x - y

#print(add(5, 3))

#def reassign(number01):
#    number01 = 2
#    print(number01)

#number02 = 1
#print("line130", number02)
#reassign(number02)
#print("line 132", number02)

#pass by value
def reassign(list01):
    list01 = [2, 3]
    print("Step 2", list01)

def append(list02):
    list02.append(4)
    print("Step 4", list02)

list03 = [0, 1]
print("Step 1", list03)
reassign(list03)
print("Step 3", list03)
append(list03) 
print("Step 5", list03)