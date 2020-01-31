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


class sortFunc:
    # Bubble Sort----------------------------------------------------------------------------
    def bubbleSort(self, arr):
        n = len(arr)  # gets the length of the array

        # Go through the whole array
        for i in range(n):  # range(start, stop, step) -> (optinal, required, optional)

            # After this for loop the last i elements should be in order
            for j in range(0, n - i - 1):
                # If current element is greater than next element swap
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Selection Sort----------------------------------------------------------------------------
    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n):  # go through the array
            min = i
            for j in range(i + 1, n):  # find the smallest element from the remaining array
                if arr[min] > arr[j]:
                    min = j

            arr[i], arr[min] = arr[min], arr[i]  # swap

    # Insertion Sort----------------------------------------------------------------------------
    def insertionSort(self, arr):
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

    # Merge Sort----------------------------------------------------------------------------
    def mergeSort(self, arr):
        n = len(arr)
        if n > 1:
            mid = n // 2        #need // for floor division, using / will give error
            left = arr[:mid]    #:mid returns everything before mid including mid
            right = arr[mid:]   # mid: returns everything after mid

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    # Quick Sort----------------------------------------------------------------------------

    def quickSort(self, arr, low, high):
        if low < high:
            par = partition(arr, low, high)

            self.quickSort(arr, low, par - 1)
            self.quickSort(arr, par + 1, high)


arr1 = [10, 7, 8, 9, 1, 5]
n1 = len(arr1)
sf = sortFunc()
sf.quickSort(arr1, 0, n1 - 1)
print("Sorted array by Quick Sort is:")
for i in range(n1):
    print(arr1[i], end=" ")

arr2 = [4, 10, 9, 3, 6, 1]
n2 = len(arr2)
sf.bubbleSort(arr2)
print("\nSorted array by Bubble Sort is:")
for i in range(n2):
    print(arr2[i], end=" ")

arr3 = [10, 6, 7, 5, 9, 8]
n3 = len(arr3)
sf.insertionSort(arr3)
print("\nSorted array by Insertion Sort is:")
for i in range(n3):
    print(arr3[i], end=" ")

arr4 = [5, 2, 4, 6, 8, 2]
n4 = len(arr4)
sf.mergeSort(arr4)
print("\nSorted array by Merge Sort is:")
for i in range(n4):
    print(arr3[i], end=" ")

arr5 = [5, 10, 7, 5, 6, 1]
n5 = len(arr5)
sf.selectionSort(arr5)
print("\nSorted array by Selection Sort is:")
for i in range(n5):
    print(arr3[i], end=" ")
