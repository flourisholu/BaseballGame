"""
Author: Flourish Oluwamakinde
Name: Baseball Game Score Keeper

Given a list of strings, ops, each item in the string with update the score accordingly:
    1. integer (x) - record a new score of x
    2. + - record sum of previous two scores
    3. D - record double of previous score
    4. C - remove previous score from record
    
This program is designed with the assumption that players do not score more than 5 points at a time
"""
def scoreUpdate(ops):
    opsList = list(ops) #put input in an array
    inputLength = len(opsList)
    
    # Append records to list array
    record = []
    for i in range(inputLength):
        # Check if the item is a number
        if opsList[i] == '1':
            record.append(int(opsList[i]))
        elif opsList[i] == '2':
            record.append(int(opsList[i]))
        elif opsList[i] == '3':
            record.append(int(opsList[i]))
        elif opsList[i] == '4':
            record.append(int(opsList[i]))
        elif opsList[i] == '5':
            record.append(int(opsList[i]))
        elif opsList[i] == '+':
            prev1 = len(record) - 1 #get previous score index
            prev2 = len(record) - 2 #get second previous score index
            sum = int(record[prev1]) + int(record[prev2])
            record.append(sum)
        elif opsList[i] == 'C':
            previousScore = len(record) - 1 #get previous score index
            record.remove(record[previousScore]) #remove previous record
        elif opsList[i] == 'D':
            previousScore = len(record) - 1 #get previous score index
            double = 2 * record[previousScore]
            record.append(double)
    
    # Get sum of all scores on record
    finalSum = 0
    recordLength = len(record)      
    for j in range(recordLength):
        finalSum = finalSum + record[j]
    print('The final score is: ', finalSum)
  
def main():
    ops = input("Enter list of strings to calculate final score: ")
    scoreUpdate(ops)
   
if __name__ == "__main__":
    main()