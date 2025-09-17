def find_cached_int_range():
    N = 0
    while True:
        a = N + 1
        b = N + 1
        if id(a) != id(b):
            break
        N += 1
    M = 0
    while True:
        a = -M - 1
        b = -M - 1
        if id(a) != id(b):
            break
        M += 1
    
    return -M, N

min_val, max_val = find_cached_int_range()
print(f"Диапазон кэширования: [{min_val}, {max_val}]")
