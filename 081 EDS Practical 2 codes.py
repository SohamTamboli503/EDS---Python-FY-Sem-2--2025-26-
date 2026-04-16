list81=[76,77,78,80,81,82,84]
list81.append(85)
print(list81)
[76, 77, 78, 80, 81, 82, 84, 85]
list81.insert(3,79)
print(list81)
[76, 77, 78, 79, 80, 81, 82, 84, 85]
list81.remove(85)
list81.remove(79)
print(list81)
[76, 77, 78, 80, 81, 82, 84]
list81.append(85)
print(list81)
[76, 77, 78, 80, 81, 82, 84, 85]
list81.pop()
85


student={"name":"Pooja","surname":"Gosavi","class":"IT1"}
print(student)
{'name': 'Pooja', 'surname': 'Gosavi', 'class': 'IT1'}
student["PRN"]=82
student["address"]="Nashik"
print(student)
{'name': 'Pooja', 'surname': 'Gosavi', 'class': 'IT1', 'PRN': 82, 'address': 'Nashik'}
student["CGPA"]=8.10
print(student)
{'name': 'Pooja', 'surname': 'Gosavi', 'class': 'IT1', 'PRN': 82, 'address': 'Nashik', 'CGPA': 8.1}
student.update({"PRN":202501080082})
print(student)
{'name': 'Pooja', 'surname': 'Gosavi', 'class': 'IT1', 'PRN': 202501080082, 'address': 'Nashik', 'CGPA': 8.1}
student.pop("name")
'Pooja'