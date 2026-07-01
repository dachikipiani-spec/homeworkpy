# def dec(func):
#     def wrap(balance, amount):
#         if balance < amount + 1:
#             return "არ არის"
#         return func(balance, amount + 1)
#     return wrap


# @dec
# def trans(balance, amount):
#     balance -= amount
#     return balance


# print(trans(100, 20))
# print(trans(20, 20))




class M(type):
    def __new__(cls, name, bases, attrs):
        for i in attrs:
            if callable(attrs[i]):
                if i[0] != "_":
                    raise ValueError("შეცდომა")
        return type.__new__(cls, name, bases, attrs)


class A(metaclass=M):
    x = 5

    def _one(self):
        print("1")

    def _two(self):
        print("2")