def calculate(a, b, c):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        if c == 0:
            return "На ноль делить нельзя"
        return a / c
    else:
        return "Некорректный ввод b"


