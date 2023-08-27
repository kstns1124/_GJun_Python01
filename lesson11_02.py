
import student

try:
    no = int(input("輸入學生數量:"))
except ValueError:
    print("input int")
else:
    print(student.get_students(num=no))


#names = student.__getAllNames();
#print(names[:5])