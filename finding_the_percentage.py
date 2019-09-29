n = 2
student_marks = {}
a=["Harsh","Anurag"]
n1=[25,26]
n2=[26.5,28]
n3=[28,30]
for i in range(n):
    name,*line=a[i],n1[i],n2[i],n3[i]
    scores=list(map(float,line))
    student_marks[name] = scores

query_name="Anurag"
print("{0:.2f}".format(sum(student_marks[query_name])/3))
