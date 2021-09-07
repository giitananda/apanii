rangeSearch = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(rangeSearch)
search = int(input('Cari angka : '))
find = False
L = 0
H = len(rangeSearch)-1
while not find and L <= H:
    M = L + (H)//2
    if rangeSearch[M] == search:
        find = True
        # print(f"Angka {search} ditemukan pada index {M}")
    elif rangeSearch[M] > search:
        H = M - 1
    elif rangeSearch[M] < search:
        L = M + 1
    # elif rangeSearch[M] != search :
    #     print(f"Angka {search} tidak ditemukan")
if find:
    print(f"Angka {search} ditemukan pada index {M}")
else:
    print(f"Angka {search} tidak ditemukan")

   