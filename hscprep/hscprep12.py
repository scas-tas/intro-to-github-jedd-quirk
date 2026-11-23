def mode(l):L=[l.count(i) for i in l];return l[L.index(max(L))]
print(mode([0,1,1,2,2,1,3,3,3,3]))