s=[[2,7,6],[9,5,1],[4,3,8]]
#print(sum(sum(s,[])[::3])==sum(s[0]))
S=sum(s,[]);c=[sum(S[i::len(s)]) for i in range(len(s))]+[sum(i) for i in s]+[sum(S[::len(s)+1]),sum(S[len(s)-1:len(S)-len(s)+1:len(s)-1])]
#c+=[sum(i) for i in s]
#c+=[sum(S[::len(s)+1])]
#c+=[sum(S[len(s)-1:len(S)-len(s)+1:len(s)-1])]
#print(9**.5)
print(c.count(15)==8)
#print(c.count(sum(s[0]))==2*(1+len(s)))