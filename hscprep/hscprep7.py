# count_vowels=lambda s:sum([s.count(i)for i in"aeiou"])
# print(count_vowels("Hello, world!"))
V=lambda L:[sum(i)for i in L]
print(V([[1,0,0,0],
         [3,4,3,2],
         [2,0,5,4]]))