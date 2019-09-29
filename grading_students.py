def gradingStudents(grades):
    # Write your code here
    for i in grades:
        diff=int(((i//5)*5+5)-i)
        if i>37 and diff<3:
            print(i+diff)
        elif i>37 and diff>3:
            print(i)
        else:
            print(i)

grades=[73,67,38,33]
gradingStudents(grades)
