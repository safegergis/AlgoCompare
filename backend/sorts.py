# reference : https://www.geeksforgeeks.org/python-program-for-quicksort/
#             https://www.geeksforgeeks.org/python-program-for-radix-sort/

from time import process_time
import random

def bubble_sort(arr):
    array = arr.copy()
    start_time = process_time()
    
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] #swap if the next element is bigger
    
    end_time = process_time()
    elapsed_time = round((end_time - start_time) * 1000, 3)
    return array, elapsed_time
def _merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        _merge_sort(left_half)
        _merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
            
def merge_sort(arr):
    array = arr.copy()
    start_time = process_time()
    
    _merge_sort(array)
        
    end_time = process_time()
    elapsed_time = round((end_time - start_time) * 1000, 3)
    return array, elapsed_time

def _quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return _quick_sort(left) + middle + _quick_sort(right)
def quick_sort(arr):
    array = arr.copy()
    start_time = process_time()
    
    sorted_array = _quick_sort(array)

    end_time = process_time()
    elapsed_time = round((end_time - start_time) * 1000, 3)
    return sorted_array, elapsed_time

    
def counting_sort(arr, place):
        size = len(arr)
        output = [0] * size
        count = [0] * 10

        # Calculate count of elements
        for i in range(size):
            index = arr[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = arr[i] // place
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        return output
def radix_sort(arr):
    array = arr.copy()
    start_time = process_time()
    
    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        array = counting_sort(array, place)
        place *= 10
    
    end_time = process_time()
    elapsed_time = round((end_time - start_time) * 1000, 3)
    return array, elapsed_time

def linear_search(arr, target):
    start_time = process_time()
    
    # Linear search algorithm implementation goes here
    found = False
    for i  in range(len(arr)):
        if arr[i] == target:
            print(f"{target} is at {i}")
            found = True
            break       
    if not found:
        print(f"{target} is not in the list. ")
        
    end_time = process_time()
    elapsed_time = round((end_time - start_time) * 1000, 3)
    return found, elapsed_time  # Return found


# Simple tests for sorting algorithms
if __name__ == "__main__":
    # Test array
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", test_arr)
    
    # Test bubble sort
    sorted_arr, time_bubble = bubble_sort(test_arr.copy())
    print("\nBubble Sort:")
    print("Sorted array:", sorted_arr)
    print("Time taken:", time_bubble)
    
    # Test merge sort
    sorted_arr, time_merge = merge_sort(test_arr.copy())
    print("\nMerge Sort:")
    print("Sorted array:", sorted_arr)
    print("Time taken:", time_merge)
    
    # Test quick sort
    sorted_arr, time_quick = quick_sort(test_arr.copy())
    print("\nQuick Sort:")
    print("Sorted array:", sorted_arr)
    print("Time taken:", time_quick)
    
    # Test radix sort
    sorted_arr, time_radix = radix_sort(test_arr.copy())
    print("\nRadix Sort:")
    print("Sorted array:", sorted_arr)
    print("Time taken:", time_radix)
    
    # Test linear search
    target = 22
    found, time_linear = linear_search(test_arr, target)
    print("\nLinear Search:")
    print(f"Searching for {target}: {'Found' if found else 'Not found'}")
    print("Time taken:", time_linear)



