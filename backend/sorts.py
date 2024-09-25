# reference : https://www.geeksforgeeks.org/python-program-for-quicksort/
#             https://www.geeksforgeeks.org/python-program-for-radix-sort/

from time import process_time
import random

def bubble_sort(arr):
    start_time = process_time()
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap if the next element is bigger
    
    end_time = process_time()
    elapsed_time = end_time - start_time
    return arr, elapsed_time

def merge_sort(arr):
    start_time = process_time()
    
    # Merge sort algorithm implementation goes here
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half) 

        i = j = k = 0 # i for the left, j for the right, k for the overal list

        # left half block
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
              arr[k] = right_half[j]
              j += 1
              k +=1
        
        #Remaining left half block
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        #Remaining right half block
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
    end_time = process_time()
    elapsed_time = end_time - start_time
    return arr, elapsed_time
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
    start_time = process_time()
    
    sorted_array = _quick_sort(arr)

    end_time = process_time()
    elapsed_time = end_time - start_time
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
    start_time = process_time()
    
    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        arr = counting_sort(arr, place)
        place *= 10
    
    end_time = process_time()
    elapsed_time = end_time - start_time
    return arr, elapsed_time

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
    elapsed_time = end_time - start_time
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



