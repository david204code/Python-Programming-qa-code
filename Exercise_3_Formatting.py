data = "cloudacademy.PYTHON.2019"
data_spaces = "     DevOps"
letter1 = 'a'
word1 = 'cloud'
num1 = '2019'

#CODE1: Strip format string
print("CODE1:")
print(f"strip = {data_spaces.strip()}")
print(f"lstrip = {data.lstrip(word1)}")
print(f"rstrip = {data.rstrip(num1)}")
print()

#CODE2: Lower and upper case string
print("CODE2")
print(f"upper = {data.upper()}")
print(f"lower = {data.lower()}")
print()

#CODE3: Swap case string
print("CODE3")
print(f"swapcase = {data.swapcase()}")
print()

#CODE4: Title case string
print("CODE4")
print(f"title = {data.title()}")
print()

#CODE5: Center string
print("CODE5")
print(word1.center(20))
print(word1.center(20,'*'))
print()

#CODE6: Left and Right adjust string
print("CODE6")
print(word1.ljust(20,'*'))
print(word1.rjust(20,'*'))
print()