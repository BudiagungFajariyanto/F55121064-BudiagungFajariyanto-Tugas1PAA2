def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Jika tidak ada pertukaran dalam satu iterasi,
        # maka array sudah terurut dan kita bisa berhenti.
        if not swapped:
            break

# Fungsi untuk mencetak array
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Contoh datanya
arr = [24, 64, 51, 4, 23, 21, 19]
print("Data pada array sebelum Bubble Sort:")
print_array(arr)

bubble_sort(arr)

print("Data pada array setelah Bubble Sort:")
print_array(arr)
