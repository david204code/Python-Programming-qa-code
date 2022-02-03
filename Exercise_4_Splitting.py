data = "cloudacademy.python.2019"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

#CODE1: Split and Partition word
print("CODE1:")
print(f"split = {data.split('.')}")
print(f"partition = {data.partition('python')}")
print()

#CODE2: Join on letter
print("CODE2:")
print(f"join = {'*'.join(word1)}")
print(f"join = {'*'.join([letter1, word1, num1])}")
print()

#CODE3: Replace word/letter in string
print("CODE3:")
print(f"replace = {data.replace('.','*')}")
print(f"replace = {data.replace(word1,num1)}")
print()