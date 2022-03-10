import random

counter = random.randint(1,10)

while counter < 5:
    print (f"{counter} is less than or equal 5")
    break
else:
    print (f"{counter} is greater than or equal 5")
    counter = 2*counter
    
    