marks=[1,2,3,4,5,6,7,8,9,10]
print(marks[5])
print(marks[0:5])
marks.append(11)
print(marks)
marks.extend([14,15])
print(marks)
marks.append([13,12])
print(marks)
del marks[-1]
print(marks)
marks.remove(14)
for mark in marks:
    print(mark)
    mark=mark-1
    del marks[5:7]
    print(mark)