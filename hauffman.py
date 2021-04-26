import timeit
import heapq
from collections import defaultdict
def Encode_fun(feq):
    heap=[[weight,[symbol,'']] for symbol , weight  in  feq.items()]
    heapq.heapify(heap)
    while len(heap)>1:
        low  =heapq.heappop(heap)
        hi=heapq.heappop(heap)
        for pair in low[1:]:
            pair[1]='0'+pair[1]
        for pair in hi[1:]:
            pair[1]='1'+ pair[1]
        heapq.heappush(heap,[low[0]+hi[0]]+low[1:]+hi[1:])
    return sorted(heapq.heappop(heap)[1:],key=lambda p:(len(p[-1]),p))
input="pizza"
feq=defaultdict(int)
for symbol in input:
    feq[symbol]+=1
huff=Encode_fun(feq)
print("symbol".ljust(10)+"weight".ljust(10)+"huffman coding")
for p in huff:
    print(p[0].ljust(10)+str(feq[p[0]]).ljust(10)+p[1])
man=15
comp=10
perofcomp=(man-comp)/(man+comp)
print("percentage =",perofcomp)
print("time required ", timeit.timeit())