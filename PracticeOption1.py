
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
print(dataSorted)

zeroTo10 = 0
tenTo20 =  []
twentyTo30 = 0
thirtyTo40 = 0
fourtyTo50 = 0
fiftyTo60 = 0 
SixtyTo70 = 0 

#loop through the data and sort them into category
for i in range(dataSorted[0]):
    #print(dataSorted[i])
    if dataSorted[i] < 10:
        zeroTo10 = len(i)
    if dataSorted[i] >= 10 and dataSorted[i] <=20:
        #tenTo20 = tenTo20.append()
        print(dataSorted)
        print("*")
    else:
        break
    



    print(tenTo20)
