def count_empty(classroom: list,count = 0) -> int:
    for row in classroom:count+=row.count(0)
    return count
 
def most_empty_row(classroom: list) -> int:
    best_row = 0
    best_count = -1
    for row in classroom:
        if row.count(0)>best_count:
            best_count=row.count(0)
            best_row=classroom.index(row)
    return best_row

classroom = [[2],[0,1],[2,0,0],[4,2,3]]
print(most_empty_row(classroom))
print(count_empty(classroom))
