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
            if left_half[i][0] < right_half[j][0]:
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

def quick_sort(arr):
    start_time = process_time()
    
    # Quick sort algorithm implementation goes here
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    arr = quick_sort(left) + middle + quick_sort(right)

    end_time = process_time()
    elapsed_time = end_time - start_time
    return arr, elapsed_time

def radix_sort(arr):
    start_time = process_time()
    
    # Radix sort algorithm implementation goes here
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

def generate_random_array(number):
    
    # Generate the random array
    random_array = [random.randint(0, 100) for _ in range(number)]
    
    return random_array
