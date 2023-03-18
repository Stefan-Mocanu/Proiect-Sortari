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
        buc = [[] for _ in range(2**16)]
        ok = 0
        for elem in L:
            aux = elem >> p
            if aux > 2**16-1:
                ok = 1
            aux %= 2**16
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


with open("input.txt", "r") as f:
    ins = [[int(x) for x in f.readline().split()] for _ in range(int(f.readline()))]

for (lungime, maxim) in ins:
    if maxim == -1:
        print("Lungime: 100000 \t Sir constant.")
        L = [1 for _ in range(100000)]
        maxim = 1
    elif maxim == -2:
        print("Lungime: 100000 \t Sir sortat")
        L = [x+1 for x in range(100000)]
        maxim = 100000
    elif maxim == -3:
        print("Lungime: 100000 \t Sir descrescator")
        L = [100000 - x for x in range(100000)]
        maxim = 100000
    else:
        print(f"Lungime: {lungime} \t Maxim: {maxim}")
        L = [random.randint(0, maxim) for _ in range(lungime)]
    L1 = L.copy()
    L_init = L.copy()
    L.sort()
    timp = float(time.time())
    radix10(L1)
    timp = float(time.time()) - timp
    if L == L1:
        print(f"Sortat in {timp} secunde cu radix10.")
    else:
        print("SORTAT GRESIT")

    L1 = L_init.copy()
    timp = float(time.time())
    radix10000(L1)
    timp = float(time.time()) - timp
    if L == L1:
        print(f"Sortat in {timp} secunde cu radix10000.")
    else:
        print("SORTAT GRESIT")

    L1 = L_init.copy()
    timp = float(time.time())
    radix2la16(L1)
    timp = float(time.time()) - timp
    if L == L1:
        print(f"Sortat in {timp} secunde cu radix2la16.")
    else:
        print("SORTAT GRESIT")

    L1 = L_init.copy()
    timp = float(time.time())
    merge_sort(L1)
    timp = float(time.time()) - timp
    if L == L1:
        print(f"Sortat in {timp} secunde cu merge_sort.")
    else:
        print("SORTAT GRESIT")

    L1 = L_init.copy()
    if lungime < 100000000:
        timp = float(time.time())
        shell_sort(L1, lungime)
        timp = float(time.time()) - timp
        if L == L1:
            print(f"Sortat in {timp} secunde cu shell_sort.")
        else:
            print("SORTAT GRESIT")
    else:
        print("Shell sort este prea lent")

    L1 = L_init.copy()
    if maxim > 100000000:
        print("Maximul este prea mare pentru count sort.")
    else:
        timp = float(time.time())
        count_sort(L1, maxim)
        timp = float(time.time()) - timp
        if L == L1:
            print(f"Sortat in {timp} secunde cu count_sort.")
        else:
            print("SORTAT GRESIT")

    L1 = L_init.copy()
    timp = float(time.time())
    if lungime < (maxim * 750):
        timp = float(time.time())
        quick_sort(L1, 0, lungime-1)
        timp = float(time.time()) - timp
        if L == L1:
            print(f"Sortat in {timp} secunde cu quick_sort.")
        else:
            print("SORTAT GRESIT")
    else:
        print("Quick sort e posibil sa dea eroare de depasire a recursiilor posibile")
    print("\n")
