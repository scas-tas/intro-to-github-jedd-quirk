f,v="aeiouy\nanenninounnnyy\nasdinois\naieouy","aeiouy"
for i in f.split("\n"):l=[i.index(c)if(c in i)else len(i)for c in v];print(i+"\n"if[l[j]>l[j-1]for j in range(6)].count(False)==1 else"",end="")