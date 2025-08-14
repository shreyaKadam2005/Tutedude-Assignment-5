

l={'Shreya':100,'Atharv':98,'Om':97,'Sneha':100}
a=input("Enter the student name: ")
if a in l:
    print(a+"'s marks: ",l[a])
else:
    print("student not found")