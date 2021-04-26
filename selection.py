import timeit
def selection(x,n):
    for i in range(n-1):
        si=i
        for j in range(i+1,n):
            if x[j]<x[si]:
                si=j
            if si!=i:
                temp=x[i]
                x[i]=x[si]
                x[si]=temp
            print("largest ele is:",x[n-1])
            print("smallest elem is:",x[0])
data=[123,13,14,155,16,817,18,19]
print("before sort:",data)
l=len(data)
selection(data,l)
print("after sort:",data)
print("worst running time",timeit.timeit())