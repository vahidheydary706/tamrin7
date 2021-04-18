def total():
    s = int(input("Enter S: "))
    m = int(input("Enter m: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    result = {"s": ((s * m2) + (s2 * m)), "m": m * m2}
    return result


a = total()
print(a["s"], "/", a["m"])

print("Fraction Multiplication: ")


def multi():
    s = int(input("Enter S: "))
    m = int(input("Enter m: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    result = {"s": s * s2, "m": m * m2}
    return result


a = multi()
print(a["s"], "/", a["m"])

print("Fraction Minus: ")


def minus():
    s = int(input("Enter S: "))
    m = int(input("Enter m: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    m3 = m * m2
    result = {"s": (m3 // m) * s - (m3 / m2) * s2, "m": m3}
    return result


a = minus()
print(a["s"], "/", a["m"])

print("Fraction Divide: ")


def divide():
    s = int(input("Enter S: "))
    m = int(input("Enter m: "))
    s2 = int(input("Enter S2: "))
    m2 = int(input("Enter m2: "))
    result = {"s": s * m2, "m": s2 * m}
    return result


a = divide()
print(a["s"], "/", a["m"])
print('End of operation (^_^)')