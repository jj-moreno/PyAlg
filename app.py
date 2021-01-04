arr1 = [7, 3, 4, 1, 2]

# # noinspection SpellCheckingInspection


def bubblesort(arr):
    dynamiclen = len(arr) - 1
    issorted = False
    numswaps = 0
    while not issorted:
        issorted = True
        for i in range(dynamiclen):
            if arr[i] > arr[i + 1]:
                numswaps += 1
                issorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        dynamiclen -= 1
    return arr, numswaps


arr1, num1 = bubblesort(arr1)
print(arr1, num1)

################################################################
arr2 = [7, 3, 4, 1, 2]

# noinspection SpellCheckingInspection


def selectionsort(arr):
    numswaps = 0
    lowestindex = -1
    for li in range(len(arr)):
        lowestindex = li
        for j in range(li + 1, len(arr)):
            if arr[lowestindex] > arr[j]:
                lowestindex = j
        if li != lowestindex:
            numswaps += 1
            arr[li], arr[lowestindex] = arr[lowestindex], arr[li]
    return arr, numswaps


arr2, num2 = selectionsort(arr2)
print(arr2, num2)


# def everyother(array):
#     counter = 0
#     length = len(array)
#     newarr = []
#     while counter < length:
#         newarr += array[counter],
#         counter += 2
#     print(newarr)


# everyother(arr2)

################################################################
arr3 = [4, 2, 7, 1, 3]


def insertionsort(arr):
