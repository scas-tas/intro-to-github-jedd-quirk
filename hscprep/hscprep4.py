# def upper(m):return "".join([chr(ord(i)-32*i.islower()) for i in m])
# def isupper(m): return [ord(i) not in [*range(ord("a"),ord("z")+1)] for i in m].count(True)==len(m)
# print(isupper("Hello"))
# print(isupper("HELLO"))
# def modeold(l):
#    m={}
#    for i in l:
#        try:m[i]+=1
#        except:m[i]=1
#    M=m[l[0]]
#    for i in m:
#        if m[i]>m[M]:
#            M=i
#    return M
def mode(l):L=[l.count(i) for i in l];return l[L.index(max(L))]
print(mode([0,1,1,2,2,1,3,3,3,3]))
# def printASCIITable():print(*[str(i)+" "+chr(i) for i in range(32,127)],sep="\n")
# printASCIITable()
# def multiplicationtable(l):
#    ml=len(str(l))
#    mml=len(str(l*l))
#    print(" "*ml,"|",*[str(i+1).rjust(mml+1) for i in range(l)],sep="")
#    print("-"*ml+"+"+"-"*(mml+1)*l)
#    print(*[str(i+1).rjust(ml)+"|"+"".join([str((j+1)*(i+1)).rjust(mml+1) for j in range(l)]) for i in range(l)],sep="\n")
# multiplicationtable(10)
# fnr=lambda s,f,r: r.join(s.split(f))
# print(fnr("hi how are you, are you cool?","are","is"))
# def mergesortedlists(a,b):
#     c=[]
#     while len(a)>0 and len(b)>0:
#         if a[0]<b[0]:c+=[a.pop(0)]
#         else:c+=[b.pop(0)]
#     if a==[]:c+=b
#     else:c+=a
#     return c
# print(mergesortedlists([0,1,3,4,4],[1,2,2,3]))
#def db(w,h):sw=(w-2);e="+"+"-"*sw+"+";print(e,*["|"+" "*sw+"|" for i in range(h-2)],e,sep="\n")
#db(10,6)