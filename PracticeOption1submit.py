#Code snippet for Python data:
data = [ 90,30,13,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83 ]
#print(data)

##PART 1 
#The number of students' marks in the data sample
numberOfStudentMark = len(data)
print(f"Total number of students' marks: {numberOfStudentMark}")

#Lowest marks
lowestMarks = min(data)
#print(f"Lowest mark: {lowestMarks}")

#Highest marks
highestMarks = max(data)
print(f"Highest mark: {highestMarks}")

#Averge mark, formatted to two decimal places
avergeMark = round(sum(data)/len(data), 2)
print(f"The averge formatted to two decimal place: {avergeMark}")

#Part 2 write a code to process the data and claculate how many instances of marks in the categories.

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

for x in dataSorted:
    if x < 10:
        zeroTo10 += 1
    elif x >= 11 and x <= 20:
        tenTo20 += 1
    elif x >=21 and x <= 30:
        twentyTo30 += 1 
    elif x >= 31 and x <= 40:
        thirtyTo40 += 1 
    elif x >= 41 and x <= 50:
        fourtyTo50 += 1 
    elif x >= 51 and x <= 60:
        fiftyTo60 += 1 
    elif x >= 61 and x <= 70:
        sixtyTo70 += 1 
    elif x >= 71 and x <= 100:
        seventyTo100 += 1
    else:
        break

#print("length:", len(dataSorted))

print("Mark 0-10:", zeroTo10)
for a in range(zeroTo10):
    print("*", end="")
print()

print("Mark 11-20:", tenTo20)
for b in range(tenTo20): 
    print("*", end="")
print()

print("Mark 21-30:", twentyTo30)
for c in range(twentyTo30):
    print("*", end="")
print()

print("Mark 31-40:", thirtyTo40)
for d in range(thirtyTo40):
    print("*", end="")
print()

print("Mark 41-50:", fourtyTo50)
for e in range(fourtyTo50):
    print("*", end="")
print()

print("Mark 51-60:", fiftyTo60)
for f in range(fiftyTo60):
    print("*", end="")
print()

print("Mark 61-70:", sixtyTo70)
for g in range(sixtyTo70):
    print("*", end="")
print()

print("Mark 70+:", seventyTo100)
for h in range(seventyTo100):
    print("*", end="")
print()


##Part 3 calculate and print out what the pass mark should be to ensure that at least 60% of students will pass the exam
#print(numberOfStudentMark) 
#100% = 61, total number of mark is 61
#print(f"The averge formatted to two decimal place: {avergeMark}")
#print(dataSorted)
lenOfDataSorted = len(dataSorted)
print("Length of all the student mark: ",lenOfDataSorted)

zeroTo10 = []
tenTo20 = []
twentyTo30 = []
thirtyTo40 = []
fourtyTo50 = []
fiftyTo60 = [] 
sixtyTo70 = [] 
seventyTo100 = [] 

for i in dataSorted:
    if i < 10:
        zeroTo10.append(i)
    if i >= 10 and i <= 20:
        tenTo20.append(i)
    if i >=21 and i <= 30:
        twentyTo30.append(i)
    if i >= 31 and i <= 40:
        thirtyTo40.append(i)
    #if i >= 41 and i <= 50:
    ## set the condition for the past mark to 45 so 60% of the students will past
    if i >= 45 and i <= 50:
        fourtyTo50.append(i)
    if i >= 51 and i <= 60:
        fiftyTo60.append(i)
    if i >= 61 and i <= 70:
        sixtyTo70.append(i)
    if i >= 71 and i <= 100:
        seventyTo100.append(i)
    
print("0 - 10:", zeroTo10, "-Length:", len(zeroTo10), "-Percentage:", (len(zeroTo10)/lenOfDataSorted)*100,"%")
print("10 - 20:", tenTo20, "-Length:", len(tenTo20), "-Percentage:", round((len(tenTo20)/lenOfDataSorted)*100),"%")
print("20 - 30:", twentyTo30, "-Length:", len(twentyTo30), "-Percentage:", round((len(twentyTo30)/lenOfDataSorted)*100),"%")
print("30 - 40:", thirtyTo40, "-Length:", len(thirtyTo40), "-Percentage:", round((len(thirtyTo40)/lenOfDataSorted)*100),"%")
print("40 - 50:", fourtyTo50, "-Length:", len(fourtyTo50), "-Percentage:", round((len(fourtyTo50)/lenOfDataSorted)*100),"%")
print("50 - 60:", fiftyTo60, "-Length:", len(fiftyTo60), "-Percentage:", round((len(fiftyTo60)/lenOfDataSorted)*100),"%")
print("60 - 70:", sixtyTo70, "-Length:", len(sixtyTo70), "-Percentage:", round((len(sixtyTo70)/lenOfDataSorted)*100),"%")
print("70 - 100:", seventyTo100, "-Length:", len(seventyTo100), "-Percentage:", round((len(seventyTo100)/lenOfDataSorted)*100),"%")

print(f"\nCurrently 45% of the stundet will past if the p'ast mark is 50 or abrove.")
print(f"The past mark will need to be at 45 for 60% of the student to past")

print(f"\nPercentage of student with mark 45 to 50 is {round((len(fourtyTo50)/lenOfDataSorted)*100)}%")
print(f"Percentage of studnet with mark 51 to 60 is {round((len(fiftyTo60)/lenOfDataSorted)*100)}%")
print(f"Percentage of studnet with mark 61 to 70 is {round((len(sixtyTo70)/lenOfDataSorted)*100)}%")
print(f"Percentage of studnet with mark 70+ is {round((len(seventyTo100)/lenOfDataSorted)*100)}%")
print(f"\n{round((len(fourtyTo50)/lenOfDataSorted)*100)}% + {round((len(fiftyTo60)/lenOfDataSorted)*100)}% + {round((len(sixtyTo70)/lenOfDataSorted)*100)}% + {round((len(seventyTo100)/lenOfDataSorted)*100)}% = 60%")