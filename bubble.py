import time
s=[1,222,45,456,7,5]
n=len(s)
print("list before sort")
print(s)
for i in range (0 , n):
    for j in range(i+1,n):
        if s[i]>s[j]:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
print("list after sort ")
print(s)
print(" time for ascending order" ,time.process_time())