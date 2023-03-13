def quickSort(arr):
    pos = 0
    tablice = [arr]
    while any([True if len(pos) > 1 else False for pos in tablice]):
        n = len(tablice[pos]) - 1
        obiektow_do_poz = sum([1 for sublist in tablice[:pos] for liczba in sublist])
        if n + 1 < 2:
            pos += 1
            continue
        pivot = n
        i = -1
        j = -1
        while True:
            i += 1
            j += 1
            # print('C', obiektow_do_poz + i, obiektow_do_poz + pivot)
            yield (obiektow_do_poz + i, obiektow_do_poz + pivot, 0)
            if i == pivot:
                # print('Z', obiektow_do_poz + i, obiektow_do_poz + pivot)
                tablice[pos][j], tablice[pos][pivot] = tablice[pos][pivot], tablice[pos][j]
                yield (obiektow_do_poz + j, obiektow_do_poz + pivot, 1)
                pivot = j
                tablice.insert(pos, tablice[pos][0:pivot])
                pos += 1
                tablice.insert(pos + 1, tablice[pos][pivot + 1:n + 1])
                tablice[pos] = [tablice[pos][pivot]]
                pos = 0
                break
            if tablice[pos][i] <= tablice[pos][pivot]:
                # print('Z', obiektow_do_poz + i, obiektow_do_poz + j)
                yield (obiektow_do_poz + i, obiektow_do_poz + j, 1)
                tablice[pos][i], tablice[pos][j] = tablice[pos][j], tablice[pos][i]
            else:
                j -= 1
    flattened = [liczba for sublist in tablice for liczba in sublist]
    print(flattened)

ad = [6, -2, -10, 7, -5, -5, 1, 4, -6, -8, -10, 7, -7, 0, 9, -4, 2, -2, 9, 10]
for i in quickSort([6, -2, -10, 7, -5, -5, 1, 4, -6, -8, -10, 7, -7, 0, 9, -4, 2, -2, 9, 10]):
    print(i)
    if i[2] == 1:
        ad[i[0]], ad[i[1]] = ad[i[1]], ad[i[0]]
print(ad)
