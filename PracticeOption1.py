
#Code snippet for Python data:
data = [ 90,30,13,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83 ]
#print(data)

#The number of students' marks in the data sample
numberOfStudentMark = len(data)
#print(f"Total number of students' marks: {numberOfStudentMark}")

#Lowest marks
lowestMarks = min(data)
#print(f"Lowest mark: {lowestMarks}")

#Highest marks
highestMarks = max(data)
#print(f"Highest mark: {highestMarks}")

#Averge mark, formatted to two decimal places
avergeMark = round(sum(data)/len(data), 2)
#print(f"The averge formatted to two decimal place: {avergeMark}")

#Part 2 write a code to process the data and claculate how many instances of marks in the categories.
#convert the lists to sets, this rout out any duplicates
#dataInSets = set(data)
#print(f"The newly converted data to set: {dataInSets}")
#print(f"The length of the set is {len(dataInSets)}")

#print(f"The length of the data is {len(data)}")

#sort the dataInSets from lowest to highest
#print(sorted(data))
dataSorted = sorted(data)
#print(dataSorted)

zeroTo10 = 0
tenTo20 = 0
twentyTo30 = 0
thirtyTo40 = 0
fourtyTo50 = 0
fiftyTo60 = 0 
sixtyTo70 = 0 
seventyTo100 = 0

#for x in dataSorted:
#    if x < 10:
#        zeroTo10 += 1
#    elif x >= 10 and x <= 20:
#        tenTo20 += 1
#    elif x >=20 and x <= 30:
#        twentyTo30 += 1 
#    elif x >= 30 and x <= 40:
#        thirtyTo40 += 1 
#    elif x >= 40 and x <= 50:
#        fourtyTo50 += 1 
#    elif x <= 50 and x <= 60:
#        fiftyTo60 += 1 
#    elif x <= 60 and x <= 70:
#        sixtyTo70 += 1 
#    elif x < 100:
#        seventyTo100 += 1
#    else:
#        break

#for a in range(zeroTo10):
#    print("*", end="")
#print()

#for b in range(tenTo20): 
#    print("*", end="")
#print()

#for c in range(twentyTo30):
#    print("*", end="")
#print()

#for d in range(thirtyTo40):
#    print("*", end="")
#print()

#for e in range(fourtyTo50):
#    print("*", end="")
#print()

#for f in range(fiftyTo60):
#    print("*", end="")
#print()

#for g in range(sixtyTo70):
#    print("*", end="")
#print()

#loop through the data and sort them into category
#for i in range(dataSorted[0]):
#    #print(dataSorted[i])
#    if dataSorted[i] < 10:
#        zeroTo10 = len(i)
#    elif dataSorted[i] >= 10 and dataSorted[i] <=20:
#        tenTo20.append([i])
#        #print(dataSorted)
#        #print(tenTo20)
#        #print(len(tenTo20))
#        #print("*")
#    else:
#        break

#print(len(tenTo20))

#Part 3 calculate and print out what the pass mark should be to ensure that at least 60% of students will pass the exam

#print(numberOfStudentMark) 
#100% = 61, total number of mark is 61
#print(f"The averge formatted to two decimal place: {avergeMark}")
#print(dataSorted)
lenOfDataSorted = len(dataSorted)
#print(lenOfDataSorted)

zeroTo10 = 0
tenTo20 = 0
twentyTo30 = 0
thirtyTo40 = 0
fourtyTo50 = 0
fiftyTo60 = 0 
sixtyTo70 = 0 
seventyTo100 = 0

i = 0
while i < len(data):
    #print(dataSorted[i])
    if i <= 70 and i <= 100:
        seventyTo100 += 1
    elif i <= 60 and i <= 70:
        sixtyTo70 += 1 
    elif i <= 50 and i <= 60:
        fiftyTo60 += 1     
    elif i >= 40 and i <= 50:
        fourtyTo50 += 1 
    elif i >= 30 and i <= 40:
        thirtyTo40 += 1
    elif i >=20 and i <= 30:
        twentyTo30 += 1 
    elif i >=10 and i <= 20:
        tenTo20 += 1
    elif i <= 10:
        zeroTo10 += 1
    else:
        break
    i = i + 1
print(seventyTo100)
    #if i < 10:
    #    zeroTo10 += 1
    #elif i >= 10 and i <= 20:
    #    tenTo20 += 1
    #elif i >=20 and i <= 30:
    #    twentyTo30 += 1 
    #elif i >= 30 and i <= 40:
    #    thirtyTo40 += 1 
    #elif i >= 40 and i <= 50:
    #    fourtyTo50 += 1 
    #elif i <= 50 and i <= 60:
    #    fiftyTo60 += 1 
    #elif i <= 60 and i <= 70:
    #    sixtyTo70 += 1 
    #elif i <= 70 and i <= 100:
    #    seventyTo100 += 1
    #else:
    #    break
    #i = i + 1



#for x in dataSorted:
#    if x < 10:
#        zeroTo10 += 1
#    elif x >= 10 and x <= 20:
#        tenTo20 += 1
#    elif x >=20 and x <= 30:
#        twentyTo30 += 1 
#    elif x >= 30 and x <= 40:
#        thirtyTo40 += 1 
#    elif x >= 40 and x <= 50:
#        fourtyTo50 += 1 
#    elif x <= 50 and x <= 60:
#        fiftyTo60 += 1 
#    elif x <= 60 and x <= 70:
#        sixtyTo70 += 1 
#    elif x <= 70 and x <= 100:
#        seventyTo100 += 1
#    else:
#        break

#print("0 - 10:", zeroTo10)
#print("10 - 20:", tenTo20)
#print("20 - 30:", twentyTo30)
#print("30 - 40:", thirtyTo40)
#print("40 - 50:", fourtyTo50)
#print("50 - 60:", fiftyTo60)
#print("60 - 70:", sixtyTo70)
#print("70 - 100:", seventyTo100)

#print(zeroTo10 + tenTo20 + twentyTo30 + thirtyTo40 + fourtyTo50 + fiftyTo60 + sixtyTo70 + seventyTo100)
#47 is 100% after the if statment