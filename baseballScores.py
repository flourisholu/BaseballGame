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
    opsArray = list(ops) #put input in an array
    inputLength = len(opsArray)
    
    # Append records to list array
    record = []
    for i in range(inputLength):
        # Check if the item is a number
        if opsArray[i] == '1':
            record.append(opsArray[i])
        elif opsArray[i] == '2':
            record.append(opsArray[i])
        elif opsArray[i] == '3':
            record.append(opsArray[i])
        elif opsArray[i] == '4':
            record.append(opsArray[i])
        elif opsArray[i] == '5':
            record.append(opsArray[i])
        elif opsArray[i] == '+':
            if len(record) > 2:
                prev1 = int(record[i-1])
                prev2 = int(record[i-2])
                sum = prev1 + prev2
                record.append(sum)
            else:
                prev1 = int(record[1])
                prev2 = int(record[0])
                sum = prev1 + prev2
                record.append(sum)
        elif opsArray[i] == 'C':
            record.remove(opsArray[i-1]) #remove previous record
        elif opsArray[i] == 'D':
            if len(record) == 1:
                previousScore = int(record[0]) #type cast string to integer
                double = 2 * previousScore
                record.append(double)
            else:
                previousScore = int(record[i-1]) #type cast string to integer
                double = 2 * previousScore
                record.append(double)
    
    # Get sum of all scores on record
    finalSum = 0
    recordLength = len(record)      
    for j in range(recordLength):
        finalSum = finalSum + int(record[j])
    print('The final score is: ', finalSum)
  
def main():
    ops = input("Enter list of strings to calculate final score: ")
    scoreUpdate(ops)
   
if __name__ == "__main__":
    main()