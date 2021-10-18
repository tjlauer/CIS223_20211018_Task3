import time
import numpy
import multiprocessing


def GenerateArray(length, direction):
    A = []
    if direction == 1:
        for i in range(0, length):
            A.append(i)
    elif direction == -1:
        for i in range(0, length):
            A.append(length-1-i)
    return A


def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[1 ... j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A


def MergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        MergeSort(L)

        # Sorting the second half
        MergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def CountSort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i] - min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Build the output character array
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]

    return arr


def ExecuteSort(aType, aLength, aCase):
    aDirection = 1
    if aCase == "B":
        aDirection = -1

    sortValues = GenerateArray(aLength, aDirection)

    start = time.perf_counter()

    if aType == "Insert":
        InsertionSort(sortValues)
    elif aType == "Merge":
        MergeSort(sortValues)
    elif aType == "Count":
        CountSort(sortValues)

    end = time.perf_counter()
    dur = end - start

    print(aType + "\t" + str(aLength) + "\t" + aCase + "\t" + str(dur))


ExecutionResults = []

ExecutionParameters = [
    {"Type": "Insert", "Length":   10000},
    {"Type": "Merge",  "Length":   10000},
    {"Type": "Count",  "Length":   10000},
    {"Type": "Insert", "Length":  100000},
    {"Type": "Merge",  "Length":  100000},
    {"Type": "Count",  "Length":  100000},
    {"Type": "Insert", "Length": 1000000},
    {"Type": "Merge",  "Length": 1000000},
    {"Type": "Count",  "Length": 1000000}
]

if __name__ == '__main__':
    for ExecutionParameter in ExecutionParameters:
        for _ in range(3):
            multiprocessing.Process(target=ExecuteSort, args=(ExecutionParameter["Type"], ExecutionParameter["Length"], "A",)).start()
    for ExecutionParameter in ExecutionParameters:
        for _ in range(3):
            multiprocessing.Process(target=ExecuteSort, args=(ExecutionParameter["Type"], ExecutionParameter["Length"], "B",)).start()
