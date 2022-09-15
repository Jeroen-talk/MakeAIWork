import math

# Derfine symbols
symbolVecs = {'O': (1, 0), 'X': (0, 1)}
symbolChars = dict((value, key) for key, value in symbolVecs.items())

# Define datasets (training set should normally be much larger than test set for best result)

trainingSet = (
    ((
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    ), 'X'),
    ((
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 1)
    ), 'X')
)


# make one list out of the tuples in tulp
tupleToList = (list(trainingSet))
tuplesInTupleToLists = []
for t in tupleToList:
    for i in t:
        for k in i:
            for j in k:
                tuplesInTupleToLists.append(j)

# print(tuplesInTupleToLists)

# divide in to four lists

divideList = list()
divideNumber = 4


def divide(divideList, divideNumber):
    for i in range(0, len(tuplesInTupleToLists), divideNumber):
        divideList.appand(tuplesInTupleToLists[i:i+divideList])


print(divideList)


# myList = []
# for tuple in tupleOfTuples:
#     myList = myList + list(tuple)

# print(trainingSet)


# matrixToVactor = []
# for

# test sets

# class Node:
#     def __init__(self):
#         self.value = None,
#         self.inLinks[]


# class Linn:
#     def __init__(self, inputNodes, outpurtNodes):
#         self.weight = 1
