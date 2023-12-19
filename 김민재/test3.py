scores = [
    [40,80,20,100,80]
    ,[43,60,85,30,90]
    ,[49,82,48,50,100]   
]

for col in zip(*scores):
    print(col)


row_cnt = len(scores)
col_cnt = len(scores[0])
for col in range(col_cnt):
    student = []
    for row in range(row_cnt):
        student.append(scores[row][col])
    print(student)