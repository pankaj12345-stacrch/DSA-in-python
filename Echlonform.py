def rref(m):
    if not m:
        return
    lead=0
    rowcount=len(m)
    colcount=len(m[0])
    for r in range(rowcount):
            if lead>=colcount:
                return
            i=r
            while m[i][lead]==0:
                i+=1
                if i==rowcount:
                    i=r
                    lead+=1
                    if colcount==lead:
                        return
            m[i],m[r]=m[r],m[i]
            lv=m[r][lead]
            m[r]=[mrx/float(lv) for mrx in m[r]]
            for i in range(rowcount):
                if i!=r:
                    lv=m[i][lead]
                    m[i]=[iv-lv*rv for rv,iv in zip(m[r],m[i])]
            lead+=1
    return m
m=[[1,2,-1,-4],[2,3,-1,-11],[-2,0,-3,-22]]
A=rref(m)
print(A)
