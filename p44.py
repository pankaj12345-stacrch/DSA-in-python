global r,c
def printmatrix(A):
    print('The entered matrix M=')
    for i in range(r):
        print(A[i])
def printrows(A):
    print('rows of matrix m=')
    for i in range(r):
        print('row %d='%i,A[i])
def printcol(A):
    print('cols of matrix =')
    for j in range(c):
        print(A[i][j], end='')
        print("\n")
def scalmul(A,s):
    N=[[s*A[i][j] for j in range(c) for i in range(r)]]
    print('the scalar multiplication is s*m=')
    printmatrix(N)
def transpose(A):
    T=[[A[i][j] for i in range(r)] for j in range(c)]
    print('transpose of M= ')
    for j in range(c):
        print(T[j])
print('enter the dimension of matrix m : ')
r=int (input('enter no of rows: '))
c=int (input('enter of col: '))
M=[]
for i in range(r):
    print('element of rows')
    M.append([])
    for j in range(c):
     n=int(input('enter elements: '))
     M[i].append(n)
printmatrix(M)
printrows(M)
printcol(M)
sc= int(input('enter scale'))
scalmul(M,sc)
transpose(M)