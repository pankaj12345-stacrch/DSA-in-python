import timeit
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k += 1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j< len(R):
            arr[k]=R[j]
            j+=1
            k+=1

def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
print("Complexity of merge sorrt with array size n is O(n* log n)")
arr = [12,11,13,5,6,7]
print("given array is ", end="\n")
printlist(arr)
mergesort(arr)
print("sorted array is:", end="\n")
printlist(arr)
print("timing ",timeit.timeit())