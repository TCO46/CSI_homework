def get_triangle_type(a, b, c):
    if (a < b + c and b < a + c and c < a + b):
        if (a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b):
            return 2
        elif (a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b):
            return 3
        else:
            return 1

    return 0


print(get_triangle_type(3, 4, 6))
