a, op, b = input("Введите через пробел: Число 1, Операцию (+, -, *, /), Число 2: ").split()
if op == "+":
    print("Ответ: {0}".format(float(a) + float(b)))
elif op == "-":
    print("Ответ: {0}".format(float(a) - float(b)))
elif op == "*":
    print("Ответ: {0}".format(float(a) * float(b)))
elif op == "/":
    print("Ответ: {0}".format(float(a) / float(b)))
else:
    print("Неверная операция")