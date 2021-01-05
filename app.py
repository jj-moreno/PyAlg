def has_duplicate(arr):
    found_duplicate = False
    known_nums = {}
    num_steps = 0
    for i in range(len(arr) - 1):
        known_nums.__setitem__(arr[i], arr[i])
        if known_nums.get(arr[i + 1]):
            found_duplicate = True
        num_steps += 1
    return str(found_duplicate) + ", num of steps " + str(num_steps)


arr0 = [3, 2, 1, 4, 2, 5]
print(has_duplicate(arr0))

################################################################
arr1 = [1, 3, 4, 2]


# noinspection SpellCheckingInspection


def bubblesort(arr):
    dynamiclen = len(arr) - 1
    issorted = False
    numcomps = 1
    numswaps = 0
    while not issorted:
        issorted = True
        for i in range(dynamiclen):
            numcomps += 1
            if arr[i] > arr[i + 1]:
                numswaps += 1
                issorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        dynamiclen -= 1
    return arr, numcomps, numswaps


arr1, num1c, num1s = bubblesort(arr1)
print(arr1, num1c, num1s)

################################################################
arr2 = [1, 3, 4, 2]


# noinspection SpellCheckingInspection


def selectionsort(arr):
    numcomps = 0
    numswaps = 0
    for li in range(len(arr)):
        lowestindex = li
        for j in range(li + 1, len(arr)):
            numcomps += 1
            if arr[lowestindex] > arr[j]:
                lowestindex = j
        if li != lowestindex:
            numswaps += 1
            arr[li], arr[lowestindex] = arr[lowestindex], arr[li]
    return arr, numcomps, numswaps


arr2, num2c, num2s = selectionsort(arr2)
print(arr2, num2c, num2s)

################################################################
arr3 = [1, 3, 4, 2]


# noinspection SpellCheckingInspection


def insertionsort(arr):
    numcomps = 0
    numswaps = 0
    arrlen = len(arr)
    for i in range(arrlen - 1):
        position = i + 1
        temp = arr[position]
        while position > 0:
            numcomps += 1
            if temp < arr[position - 1]:
                numswaps += 1
                arr[position] = arr[position - 1]
                position -= 1
            else:
                break
        arr[position] = temp
    return arr, numcomps, numswaps


arr3, num3c, num3s = insertionsort(arr3)
print(arr3, num3c, num3s)
