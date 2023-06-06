import time

def bubble_sort(arr):
    n = len(arr)
    iterations = 0
    start_time = time.time()

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            iterations += 1
            time.sleep(0.1)

        if not swapped:
            break

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, iterations, execution_time

size = int(input("Masukkan jumlah elemen dalam array: "))
arr = []

for i in range(size):
    num = int(input(f"Masukkan elemen ke-{i+1}: "))
    arr.append(num)

sorted_arr, iterations, execution_time = bubble_sort(arr)
print("Hasil setelah pengurutan:", sorted_arr)
print("Jumlah iterasi:", iterations)
print("Waktu eksekusi:", execution_time, "detik")
