a_Matrix = [[1, 2, 3],
           [4, 5, 6], 
           [7, 8, 9]]

        print(row
b_Matrix = [[9, 8, 7], 
           [6, 5, 4], 
           [3, 2, 1]]

c_Result = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]] # result matrix 

for rowIndex in range(len(a_Matrix)):
    for columnIndex in range(len(b_Matrix[0])):
        for termIndex in range(len(a_Matrix[0])): 
            c_Result[rowIndex][columnIndex] += a_Matrix[rowIndex][termIndex] * b_Matrix[termIndex][columnIndex]

print(a_Matrix)
print(b_Matrix)

for row in c_Result:
    print(row)
