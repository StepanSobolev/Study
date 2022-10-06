def numero(a, b):
    sered = b // 2
    for i in range(1, sered+1):
        print(a * i)
    print(a * (sered+1))
    for i in range(1, sered+1):
        print(a * ((sered+1) - i))


numero('&', 13)