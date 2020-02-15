# class Car():
#     def __init__(self,modelname,year,price):         #this is the constructor
#         self.modelname = modelname
#         self.year = year
#         self.price = price
#
#     def price_increase(self):
#         self.price = int(self.price*1.15)
#
# honda = Car("City", 2017, 10000)
#
# print(honda.price)
# honda.price_increase()
# print(honda.price)

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Bubble Sort----------------------------------------------------------------------------
def bubbleSort(arr):
    n = len(arr)  # gets the length of the array

    # Go through the whole array
    for i in range(n):  # range(start, stop, step) -> (optinal, required, optional)
        # After this for loop the last i elements should be in order
        for j in range(0, n - i - 1):
            # If current element is greater than next element swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Selection Sort----------------------------------------------------------------------------
def selectionSort(arr):
    n = len(arr)

    for i in range(n):  # go through the array
        min = i
        for j in range(i + 1, n):  # find the smallest element from the remaining array
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]  # swap


# Insertion Sort----------------------------------------------------------------------------
def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # Merge Sort Recursive----------------------------------------------------------------------------
    # def mergeSort(self, arr):
    #     n = len(arr)
    #     if n > 1:
    #         mid = n // 2  # need // for floor division, using / will give error
    #         left = arr[:mid]  #:mid returns everything before mid including mid
    #         right = arr[mid:]  # mid: returns everything after mid
    #
    #         self.mergeSort(left)
    #         self.mergeSort(right)
    #
    #         i = j = k = 0
    #
    #         while i < len(left) and j < len(right):
    #             if left[i] < right[j]:
    #                 arr[k] = left[i]
    #                 i += 1
    #             else:
    #                 arr[k] = right[j]
    #                 j += 1
    #             k += 1
    #
    #         while i < len(left):
    #             arr[k] = left[i]
    #             i += 1
    #             k += 1
    #
    #         while j < len(right):
    #             arr[k] = right[j]
    #             j += 1
    #             k += 1


# Merge Sort Iterative---------------------------------------------------------------------------------
def mergeSort(a):
    current_size = 1
    # traversing subarrays
    while current_size < len(a) - 1:
        left = 0
        # subarray being sorted
        while left < len(a) - 1:
            # calculating mid value
            mid = left + current_size - 1
            # current_size
            right = ((2 * current_size + left - 1, len(a) - 1)[2 * current_size + left - 1 > len(a) - 1])
            # Merge
            merge(a, left, mid, right)
            left = left + current_size * 2
        # Increasing sub array size
        current_size = 2 * current_size


# Merge Function
def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


# Quick Sort----------------------------------------------------------------------------
def quickSort(arr, low, high):
    if low < high:
        par = partition(arr, low, high)

        quickSort(arr, low, par - 1)
        quickSort(arr, par + 1, high)


# arr1 = [10, 7, 8, 9, 1, 5]
# n1 = len(arr1)
# quickSort(arr1, 0, n1 - 1)
# print("Sorted array by Quick Sort is:")
# for i in range(n1):
#     print(arr1[i], end=" ")
#
# arr2 = [4, 10, 9, 3, 6, 1]
# n2 = len(arr2)
# bubbleSort(arr2)
# print("\nSorted array by Bubble Sort is:")
# for i in range(n2):
#     print(arr2[i], end=" ")
#
# arr3 = [10, 6, 7, 5, 9, 8]
# n3 = len(arr3)
# insertionSort(arr3)
# print("\nSorted array by Insertion Sort is:")
# for i in range(n3):
#     print(arr3[i], end=" ")
#
# arr4 = [5, 200, 76, 2, 4, 6, 8, 2, 50, 2, 3, 5]
# n4 = len(arr4)
# mergeSort(arr4)
# print("\nSorted array by Merge Sort is:")
# for i in range(n4):
#     print(arr4[i], end=" ")
#
# arr5 = [5, 10, 7, 5, 6, 1]
# n5 = len(arr5)
# selectionSort(arr5)
# print("\nSorted array by Selection Sort is:")
# for i in range(n5):
#     print(arr3[i], end=" ")
#
# abc = [5, 4, 3, 2, 1]
#
# print(abc)
