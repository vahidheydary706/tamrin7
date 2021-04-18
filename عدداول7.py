def prime_number():
    number = int(input("Enter Number: "))
    if number % 2 == 1:
        return ("T")
    else:
        return ("F")


print(prime_number())


def number_between():

    for i in range(a , b):
        if i % 2 == 1:
            print(i)
