def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def is_super_prime(num):
    if not is_prime(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True
