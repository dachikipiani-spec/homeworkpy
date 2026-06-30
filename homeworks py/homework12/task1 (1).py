import csv


def collect_students(count):
    with open("students_input.csv", "w", newline="", encoding="utf-8") as f:
        fieldnames = ["ID", "first_name", "last_name", "age"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, count + 1):
            first_name = input("First name: ")
            last_name = input("Last name: ")

            while True:
                try:
                    age = int(input("Age: "))
                    break
                except ValueError:
                    print("Please enter a valid integer for age!")

            writer.writerow({
                "ID": i,
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            })


n = int(input("How many people? "))
collect_students(n)
