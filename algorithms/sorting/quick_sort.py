"""
Algorithm: Quick Sort
Description: Efficient divide-and-conquer sorting algorithm
Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) for recursion stack
"""

def quick_sort(arr):
    """
    Sort an array using quick sort algorithm
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_inplace(arr, low, high):
    """
    In-place quick sort implementation
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """
    Partition the array around a pivot
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    # Test quick sort
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr1}")
    sorted_arr = quick_sort(arr1)
    print(f"Sorted array: {sorted_arr}")
    
    # Test in-place quick sort
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal array: {arr2}")
    quick_sort_inplace(arr2, 0, len(arr2) - 1)
    print(f"Sorted array (in-place): {arr2}")

if __name__ == "__main__":
    main()
