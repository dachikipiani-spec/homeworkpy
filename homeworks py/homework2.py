# weight = float(input("შეიყვანეთ წონა (კგ): "))
# height = float(input("შეიყვანეთ სიმაღლე (მ): "))

# bmi = weight / (height ** 2)

# print(f"\nთქვენი BMI: {bmi:.2f}")

# if bmi < 19:
#     print("სტატუსი: Underweight (წონის დეფიციტი)")
# elif bmi <= 25:
#     print("სტატუსი: Normal weight (ნორმალური წონა)")
# else:
#     print("სტატუსი: Overweight (ჭარბი წონა)")


# num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
# operator = input("შეიყვანეთ ოპერატორი (+, -, *, /): ")
# num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#      result = num1 / num2
# else:
#     print("შეცდომა: არასწორი ოპერატორი!")

# if operator in ["+", "-", "*"] or (operator == "/" and num2 != 0):
#     print(f"შედეგი: {num1} {operator} {num2} = {result}")


a = float(input("შეიყვანეთ პირველი რიცხვი: "))
b = float(input("შეიყვანეთ მეორე რიცხვი: "))
c = float(input("შეიყვანეთ მესამე რიცხვი: "))

if a == b or b == c or a == c:
    print("გთხოვთ შეიყვანოთ განსხვავებული რიცხვები!")
else:
    largest = a

    if b > largest:
        largest = b

    elif c > largest:
        largest = c

    print(f"ყველაზე დიდი რიცხვია: {largest}")


