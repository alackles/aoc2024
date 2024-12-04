import numpy as np

matrix = np.array([list(x) for x in np.loadtxt("input.txt", dtype=str)])

horiz = [] 
vert = []
diag = []

for row in matrix:
    horiz.append("".join(row))

for row in np.transpose(matrix):
    vert.append("".join(row))

for i in range(0, matrix.shape[1]):
    diag1 = matrix.diagonal(i)
    diag2 = matrix.diagonal(i, axis1=1, axis2=0)
    diag3 = np.flip(matrix, 1).diagonal(i)
    diag4 = np.flip(matrix, 1).diagonal(i, axis1=1, axis2=0)
    diag.append("".join(diag1))
    diag.append("".join(diag3))
    if i>0:
        diag.append("".join(diag2))
        diag.append("".join(diag4))

xmas_count = 0

for h in horiz:
    xmas_count += h.count("XMAS") + h[::-1].count("XMAS")

for v in vert:
    xmas_count += v.count("XMAS") + v[::-1].count("XMAS")

for d in diag:
    xmas_count += d.count("XMAS") + d[::-1].count("XMAS")


mas_count = 0

for i, row in enumerate(matrix[1:-1]):
    for j, char in enumerate(row[1:-1]):
        if char == 'A':
            #MAS x MAS
            if matrix[i,j] == 'M' and matrix[i+2,j+2] == 'S' and matrix[i, j+2] == 'M' and matrix[i+2, j] == 'S':
                mas_count += 1
            #MAS x SAM
            elif matrix[i,j] == 'M' and matrix[i+2,j+2] == 'S' and matrix[i, j+2] == 'S' and matrix[i+2, j] == 'M':
                mas_count += 1
            #SAM x MAS
            elif matrix[i,j] == 'S' and matrix[i+2,j+2] == 'M' and matrix[i, j+2] == 'M' and matrix[i+2, j] == 'S':
                mas_count += 1
            #SAM x SAM
            elif matrix[i,j] == 'S' and matrix[i+2,j+2] == 'M' and matrix[i, j+2] == 'S' and matrix[i+2, j] == 'M':
                mas_count += 1

print(xmas_count)
print(mas_count)