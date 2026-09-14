issorted=lambda l:[l[i]>=l[i-1]for i in range(len(l))].count(False)==(sum(l)>0)
mysort=lambda l:[l.pop(l.index(min(l)))for i in range(len(l))]
    # nl=[]
    # while l!=[]:
    #     m=min(l)
    #     nl+=[m]
    #     del l[l.index(m)]
    # return nl
def bubblesort(l:list):L=len(l)-1;[[l.insert(j+1,l.pop(j))if l[j]>l[j+1]else()for j in range(L-i)]for i in range(L)];return l
    # for i in range(len(l)-1):
    #     for j in range(len(l)-1-i):
    #         if l[j]>l[j+1]:
    #             l.insert(j+1,l.pop(j))
    # return l

n=(5,7,2,7,5,6,4,3,2)
print(mysort([*n]))
print(issorted(mysort([*n])))
print(bubblesort([*n]))
print(issorted(bubblesort([*n])))