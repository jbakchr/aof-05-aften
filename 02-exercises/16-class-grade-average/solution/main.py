class_grades = [
    {"name": "Mia", "grades": {"math": 10, "english": 4, "physics": 4}},
    {"name": "Jakob", "grades": {"math": 4, "english": 12, "physics": 4}},
    {"name": "Morten", "grades": {"math": 7, "english": 7, "physics": 12}},
    {"name": "Sara", "grades": {"math": 2, "english": 10, "physics": 7}},
]

total_grades = 0
numbers_of_exams = 0

for student in class_grades:
    for subject, grade in student["grades"].items():
        total_grades += grade
        numbers_of_exams += 1

print(
    f"Klassens elever har i gennemsnit fået en karakter på {total_grades / numbers_of_exams}"
)
