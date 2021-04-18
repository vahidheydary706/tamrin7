
def sum():
    h1 = int(input("Enter Hour: "))
    m1 = int(input("Enter Minutes: "))
    if 0 > m1 or m1 > 60:
        print("TryAgain")
        exit()
    s1 = int(input("Enter Seconds: "))
    if 0 > s1 or s1 > 60:
        print("TryAgain")
        exit()
    h2 = int(input("Enter Hour2: "))
    m2 = int(input("Enter Minutes2: "))
    if 0 > m2 or m2 > 60:
        print("TryAgain")
        exit()
    s2 = int(input("Enter Seconds2: "))
    if 0 > s2 or s2 > 60:
        print("TryAgain")
        exit()
    result1 = {"h": h1, "m": m1, "s": s1}
    print(result1["h"], ":", result1["m"], ":", result1["s"], end="\t")
    result2 = {"h": h2, "m": m2, "s": s2}
    print(result2["h"], ":", result2["m"], ":", result2["s"])
    result3 = {"h": h1 + h2, "m": m1 + m2, "s": s1 + s2}
    return result3


r = sum()
print(r["h"], ":", r["m"], ":", r["s"])

print("Time Minus")


def minus():
    h1 = int(input("Enter Hour: "))
    m1 = int(input("Enter Minutes: "))
    if 0 > m1 or m1 > 60:
        print("TryAgain")
        exit()
    s1 = int(input("Enter Seconds: "))
    if 0 > s1 or s1 > 60:
        print("TryAgain")
        exit()
    h2 = int(input("Enter Hour2: "))
    m2 = int(input("Enter Minutes2: "))
    if 0 > m2 or m2 > 60:
        print("TryAgain")
        exit()
    s2 = int(input("Enter Seconds2: "))
    if 0 > s2 or s2 > 60:
        print("TryAgain")
        exit()
    result1 = {"h": h1, "m": m1, "s": s1}
    print(result1["h"], ":", result1["m"], ":", result1["s"], end="\t")
    result2 = {"h": h2, "m": m2, "s": s2}
    print(result2["h"], ":", result2["m"], ":", result2["s"])
    result3 = {"h": h1 - h2, "m": m1 - m2, "s": s1 - s2}
    return result3


r = minus()
print(r["h"], ":", r["m"], ":", r["s"])

print("Convert Time To Seconds")


def time():
    h = int(input("Enter Hour: "))
    m = int(input("Enter Minutes: "))
    s = int(input("Enter Seconds: "))
    print(f"{h} : {m} : {s}")
    hour = h * 3600
    minute = m * 60
    result = hour + minute + s
    return result
r = time()
print(f"Seconds: {r}")
print('End of operation (^_^)')