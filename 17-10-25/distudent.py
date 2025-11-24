student={"name":"Fehrin","roll number":32,"register number":19878,"department":"MCA","semester":1}
print(student)
student["Mark"]=int(input("enter the total mark"))
print(student)
if student["Mark"]>=90:
    student["Grade"]="A"
elif student["Mark"]>=82:
    student["Grade"]="B"
elif student["Mark"]>=75:
    student["Grade"]="C"
elif student["Mark"]>=60:
    student["Grade"]="D"
elif student["Mark"]>=50:
    student["Grade"]="P"
else:
    student["Grade"]="F"
print(student)
student.pop("roll number")
print(student)
