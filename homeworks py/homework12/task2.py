import csv

with open("students.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    students = list(reader)

failed = [s for s in students if int(s["Grade"]) < 50]
passed = [s for s in students if int(s["Grade"]) >= 50]

with open("failed_students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(failed)

with open("passed_students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(passed)

print(f"Failed: {len(failed)}, Passed: {len(passed)}")
