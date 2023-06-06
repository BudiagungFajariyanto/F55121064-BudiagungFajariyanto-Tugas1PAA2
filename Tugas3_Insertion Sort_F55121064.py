import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print_iteration(arr, i)
        time.sleep(0.1)

def print_iteration(arr, i):
    print(f"Iterasi {i}: {arr}")

arr = input("Masukkan elemen array (pisahkan dengan spasi): ").split()
arr = [int(x) for x in arr]
print("Masukkan data:", arr)

start_time = time.time()
insertion_sort(arr)
end_time = time.time()
execution_time = end_time - start_time

print("Data Terurut:", arr)
print("Waktu Eksekusi:", execution_time, "seconds")
