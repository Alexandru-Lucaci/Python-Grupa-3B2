def is_prime(a):
    for i in range(2, int((a ** 0.5 + 1))):
        if a % i == 0:
            return False
    return True


def process_item(x):
    # the least prime number greater than x
    x += 1
    if is_prime(x):
        return x
    return process_item(x)


if __name__ == '__main__':
    print(process_item(3))

    a = int(input("Introdu un numar"))
    print(process_item(a))
