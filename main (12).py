student = {
    "name": "Prince",
    "age": 18,
    "course": "BCA",
    "university": "Galgotias University"
}
print("Student Information:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
print("\nName of the student:", student["name"])
student["semester"] = 2
student["age"] = 21
student.pop("course")
print("\nUpdated Student Information:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
