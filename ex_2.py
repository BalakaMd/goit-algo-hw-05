def binary_search_float(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        if arr[mid] == x:
            # Знайдено точний елемент
            return iterations, arr[mid]
        elif arr[mid] < x:
            # Ігноруємо ліву половину
            low = mid + 1
        else:
            # Ігноруємо праву половину
            high = mid - 1

    # Елемент не знайдено, повертаємо верхню межу
    if low < len(arr):
        return iterations, arr[low]
    else:
        # Весь масив менший за x
        return iterations, None


# Приклад використання
arr_float = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
x_float = 4.0
iterations, upper_bound = binary_search_float(arr_float, x_float)

if upper_bound is not None:
    print(f"Елемент {x_float} знаходиться за індексом {arr_float.index(upper_bound)}")
    print(f"Верхня межа: {upper_bound}")
else:
    print(f"Елемент {x_float} не знайдено в масиві.")
    print(f"Верхня межа: {arr_float[-1]}")
