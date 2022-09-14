#https://github.com/yeftaindri10/71210788_PrakStrukdat_B.git

n = int(input('Masukkan range data : '))


def fact(f):
    return 1 if (f == 1 or f == 0) else f * fact(f - 1)


for i in range(0, n, 2):
    test = i
    for x in range(0, n, 2):
        faktorial = fact(x)
        print(f'{test}: {faktorial}', end=" ")