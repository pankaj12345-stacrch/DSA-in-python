R = int(input("Enter the number of rows:"))

C = int(input("Enter the number of columns:"))


m = []

print("Enter the entries rowwise:")



for i in range(R):

    a = []

    for j in range(C):

        a.append(int(input()))

    m.append(a)



for i in range(R):

    for j in range(C):
        print(m[i][j], end=" ")

    print()
print("the m matrix is")
print("length of matrix is",R*C)