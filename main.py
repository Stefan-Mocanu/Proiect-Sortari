import time
import random


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
        for i in range(10000):
            for j in range(len(buc[i])):
                L[cnt] = buc[i][j]
                cnt += 1
            buc[i].clear()

        p *= 10000


def radix10(L):
    p = 1
    ok = 1
    while ok:
        buc = [[] for _ in range(10)]
        ok = 0
        for elem in L:
            aux = elem//p
            if aux > 9:
                ok = 1
            aux %= 10
            buc[aux].append(elem)
        cnt = 0
        for i in range(10):
            for j in range(len(buc[i])):
                L[cnt] = buc[i][j]
                cnt += 1
            buc[i].clear()

        p *= 10


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


def shell_sort(nesortat, lenght):
    interval = lenght//2
    while interval > 0:
        for i in range(interval, lenght):
            aux = nesortat[i]
            j = i
            while j >= interval and nesortat[j - interval] > aux:
                nesortat[j] = nesortat[j - interval]
                j -= interval

            nesortat[j] = aux
        interval //= 2


def count_sort(nesortat, maxim):
    if maxim > 1000000000:
        print("Maximul este prea mare.")
        return
    Numere = [0 for _ in range(maxim+1)]
    for elem in nesortat:
        Numere[elem] += 1
    nesortat.clear()
    for i in range(maxim + 1):
        for j in range(Numere[i]):
            nesortat.append(i)


def quick_sort(nesortat, st, dr):
    if st < dr:
        (p1, p2, p3) = (random.randint(st, dr) for _ in range(3))
        pivot = max(min(nesortat[p1], nesortat[p2]), min(nesortat[p2], nesortat[p3]))
        if pivot == nesortat[p1]:
            nesortat[p1], nesortat[dr] = nesortat[dr], nesortat[p1]
        elif pivot == nesortat[p2]:
            nesortat[p2], nesortat[dr] = nesortat[dr], nesortat[p2]
        else:
            nesortat[p3], nesortat[dr] = nesortat[dr], nesortat[p3]
        i = st - 1
        for j in range(st, dr):
            if nesortat[j] < pivot:
                i += 1
                nesortat[i], nesortat[j] = nesortat[j], nesortat[i]

        nesortat[i+1], nesortat[dr] = nesortat[dr], nesortat[i+1]
        quick_sort(nesortat, st, i)
        quick_sort(nesortat, i+2, dr)


f = open("input.txt", "r")
for _ in range(10):
    L = [random.randint(0, 1500) for _ in range(1000000)]
    #L = [2, 10, 34, 5, 16, 18, 20]

    L1 = L.copy()
    timp = float(time.time())
    quick_sort(L, 0, len(L) - 1)
    timp = float(time.time()) - timp
    if L == sorted(L1):
        print(f"Sortat in {timp} secunde.")
    else:
        print("SORTAT GRESIT")
f.close()
