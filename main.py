def rot(num):
    return int(str(num).replace("6","9", 1))

while True:
    num = int(input("Вход: "))
    print("Результат: ", rot(num))
