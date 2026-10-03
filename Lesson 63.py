#Write a program to find the mean and median of a given array
def find_mean_and_median(arr):
    if not arr:
        return None, None
    mean = sum(arr) / len(arr)
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2
    if n % 2 != 0:
        median = sorted_arr[mid]
    else:
        median = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    return mean, median
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
mean, median = find_mean_and_median(numbers)
print(f"Mean: {mean}, Median: {median}")
#Write a program to find the maximum and minimum elements in an array.
def find_max_and_min(arr):
    if not arr:
        return None, None
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num     
    return max_val, min_val
numbers = [12, 45, 2, 67, 8, 23]
maximum, minimum = find_max_and_min(numbers)
print(f"Maximum: {maximum}, Minimum: {minimum}")
#Write a program to find the second largest element in an array.
def find_second_largest(arr):
    if len(arr) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None
numbers = [10, 20, 4, 45, 45, 99, 99, 4]
second_max = find_second_largest(numbers)
print(f"Second Largest Element: {second_max}")