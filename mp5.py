global r1,c1,r2,c2

def printmatrix(A):
 for i in range(len(A)):
   print(A[i])
def matrixadd(A,B):
 C=[[A[i][j]+B[i][j] for j in range(len(B[0]))] for i in
range(len(A))]
 print('Addtion of two matrix=')
 printmatrix(C)
def matrixmul(A,B):
 C=[[sum(A[i][k]*B[k][j] for k in range(len(B)))for j in
range(len(B[0]))]for i in range(len(A))]
 print('Multiplication of 2 matrix =')
 printmatrix(C)
def matrixvecmul(A,v):
  C=[sum(A[i][j]*v[j]for j in range(len(v))) for i in range(len(A))]
  print('Matrix vector multiplication (M1*v)=',C)
def vecmatrixmul(v,A):
  C=[sum(v[j]*A[j][i]for j in range(len(v)))for i in range(len(A))]
  print('vector of matrix multiplication (v*M1)=',C)
print('enter the dimensionof Matrix1')
r1=int(input('enter no of rows'))
c1=int(input('enter no of columns'))
M=[]
for i in range(r1):
 print('enter elements of row',i)
 M.append([])
 for j in range(c1):
    n=int(input('enter no'))
    M[i].append(n)
print('The entered Matrix M1 is')
printmatrix(M)
print('enter the dimensions of Matrix2')
r2=int(input('enter no of rows'))
c2=int(input('enter no of columns'))
N=[]
for i in range(r2):
 print('enter elements of row',i)
 N.append([])
 for j in range(c2):
   n=int(input('enter no'))
   N[i].append(n)
print('The entered Matrix M2 is')
printmatrix(N)
matrixadd(M,N)
matrixmul(M,N)
s=input('Enter elements of vector separated by spaces')
v=[int(x)for x in s.split()]
print(len(v))
if len(v)!=c1:
  print('invalid vector add vector of %d elements ((Columns of M1)%c1')
else:
  matrixvecmul(M,v)
s=input('Enter elements of vector separated by spaces')
v=[int(x)for x in s.split()]
print(len(v))
if len(v)!=r1:
  print('invalid vector add vector of %d elements ((Rows of M1)%r1')
else:
  vecmatrixmul(v,M)