#def ismagic(s):l=sum([s[i][i] for i in range(len(s))]);return (sum([s[i][len(s)-i-1] for i in range(len(s))])==l and [sum([s[j][i] for j in range(len(s))]) for i in range(len(s))].count(l)==len(s)==[sum(i) for i in s].count(l))
def ismagic(s):S=sum(s,[]);l=len(s);c=[sum(S[i::l]) for i in range(l)]+[sum(i) for i in s]+[sum(S[::l+1]),sum(S[l-1:l*l-l+1:l-1])];return c.count(sum(s[0]))==2*(1+l)
print(("Not magic.","Magic!")[ismagic([[2,7,6],        #magic
                                       [9,5,1],
                                       [4,3,8]])])
print(("Not magic.","Magic!")[ismagic([[2,7,6],        #not magic
                                       [9,5,2],
                                       [4,3,8]])])
print(("Not magic.","Magic!")[ismagic([[2,16,13,3],    #magic
                                       [11,5,8,10],
                                       [7,9,12,6],
                                       [14,4,1,15]])])
print(("Not magic.","Magic!")[ismagic([[2,16,13,3],    #not magic
                                       [11,5,8,10],
                                       [7,9,12,7],
                                       [14,4,1,15]])])