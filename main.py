def radix10000(L):
    p = 1
    ok = 1
    while ok:
        buc = [[] for _ in range(10000)]
        ok = 0
        for elem in L:
            aux = elem//p
            if aux > 9999:
                ok = 1
            aux %= 10000
            buc[aux].append(elem)
        cnt = 0
        for i in range(len(buc)):
            for j in range(len(buc[i])):
                L[cnt] = buc[i][j]
                cnt += 1
                buc[i][j] = -1

        p *= 10000


def radix2la16(L):
    p = 0
    ok = 1
    while ok:
        buc = [[] for _ in range(16)]
        ok = 0
        for elem in L:
            aux = elem >> p
            if aux > 2**16-1:
                ok = 1
            aux %= 16
            buc[aux].append(elem)
        cnt = 0
        for i in range(len(buc)):
            for j in range(len(buc[i])):
                L[cnt] = buc[i][j]
                cnt += 1
                buc[i][j] = -1

        p += 16


def merge_sort(nesortat):

    if len(nesortat) > 1:
        mij = len(nesortat)//2
        st = nesortat[:mij]
        dr = nesortat[mij:]
        merge_sort(st)
        merge_sort(dr)

        i = j = k = 0

        while i < len(st) and j < len(dr):
            if st[i] < dr[j]:
                nesortat[k] = st[i]
                i += 1
            else:
                nesortat[k] = dr[j]
                j += 1
            k += 1

        while i < len(st):
            nesortat[k] = st[i]
            i += 1
            k += 1

        while j < len(dr):
            nesortat[k] = dr[j]
            j += 1
            k += 1


f = open("input.txt", "r")
L = [4, 2, 3, 523, 41, 124, 412, 1, 7, 123]
radix10000(L)
print(L)
f.close()
