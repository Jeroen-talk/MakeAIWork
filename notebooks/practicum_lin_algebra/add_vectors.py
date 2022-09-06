#! usr/bin/env python3
# Dit programma staleds ons mogelijk om twee verctore bij elkaar op te tellen.

# vector
a = [0, 3, 1]
b = [1, 4, 7]

#vectoren landen in nieuwe lijst en dan op tellen
c= [a[0]+b[0],a[1]+b[1],a[2]+b[2] ]

print(c)

aLabel = [0, 3, 1]
bLabel = [1, 4, 7]

# funtie
def addVectors(aLabel, bLabel)
# voor elke rij
 for:aLabel in bLabel:
     aLabel.append(bLabel)
         #tel de cooresponderende elementen bij elkaar op

    #return resultaat

aLabal = list [1, 2]
bLabel = list [2, 1]

w = addVectors(aLabel, bLabel)

# Vectoren optellen

vectore_A = [0, 3, 1]
vectore_B = [1, 4, 7]

vectore_result = [0, 0, 0]

for rowIndex in range(len(vectore_A [0])):
    for columnIndex in range(len(vectore_B [0])):
        vectore_result [rowIndex][columnIndex] += vectore_A [rowIndex] + vectore_B [columnIndex]
for result in vectore_result
        print(result)

# oplossing vectoren optellen

vectore_A = [0, 3, 1]
vectore_B = [1, 4, 9]

vectore_result = [0, 0, 0]

for rowIndex in range(len(vectore_A)):
    vectore_result [rowIndex] += vectore_A [rowIndex] + vectore_B [rowIndex]

for result in vectore_result:
    print(result)
