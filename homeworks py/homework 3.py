# n = int(input("შეიყვანე რიცხვი: "))

# result = 1
# for i in range(1, n + 1):
#     result = result * i

# print(n, "!=", result)

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i, "*", j, "=", i * j)

sul = 50
shesadzlokupiur = [5, 10, 20]

print(f"გადასახდელი {sul} ლარი")

while sul > 0:
    kupiura = int(input("შეიყვანეთ თანხა"))
    
    if kupiura not in shesadzlokupiur:
        print("შეიყვანეთ (5, 10 ან 20 ლარი)")
        continue
    sul -= kupiura
    if sul > 0:
        print(f"დარჩა {sul} ლარი")

xurda = -sul
if xurda    > 0:
    print(f"ხურდა: {xurda} ლარი")
else:
    print("დასრულდა")