"""students = []
students.append({"name": "Pias", "roll": 1, "math": 88})
students.append({"name": "Tania", "roll": 2, "math": 75})
for s in students:
    print(s["name"], s["math"])

name=["pias","joy","rony",'shuvo','jonny']
students=[]
for x in name:
    students.append({"name":x})
for student in students:
    print(student["name"])"""
import time

print("Loading...", end='')

for i in range(20):
    print("█", end='', flush=True)
    time.sleep(0.1) 
print(" Done!")
