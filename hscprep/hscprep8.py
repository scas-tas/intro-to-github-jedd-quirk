# def orders_by_students(o):
#     d={}
#     for i in o:
#         if i[0] in d:
#             d[i[0]]+=[i[1]]
#         else:
#             d[i[0]]=[i[1]]
#     return d
#def orders_by_students(o):d={};[i[0]in d and d[i[0]].append(i[1])or d.setdefault(i[0],[i[1]])for i in o];return d
orders_by_students=lambda o:dict((i,[r for j,r in o if j==i])for i,u in o)
orders = [
    ("Amelia", "sandwich"),
    ("Josh", "sandwich"),
    ("Amelia", "juice"),
    ("Priya", "salad"),
    ("Josh", "juice"),
    ("Josh", "salad")
]
#print(dict(orders))
print(orders_by_students(orders))