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


# Voorbeelden van Matrix berekingen
#
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# B = [[25, 24, 23, 22],
#      [21, 20, 19, 18],
#      [17, 16, 15, 14]]
#
# #
# res = [[sum(a * b for a, b in zip(A_row, B_col))
#         for B_col in zip(*B)] for A_row in A]
# for r in res:
#    print(r)
