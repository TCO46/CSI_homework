def count_switches(n, arr):
    switch = 0

    for i in range(n):
        if arr[i] == False:
            switch += 1

    return n - switch
