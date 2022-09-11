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


class Node:
    def __init__(self):
        self.value = None,
        self.inLinks[]


class Linn:
    def __init__(self, inputNodes, outpurtNodes):
        self.weight = 1
