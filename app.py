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
arr1 = [7, 3, 4, 1, 2]


# noinspection SpellCheckingInspection


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


# noinspection SpellCheckingInspection

def everyother(array):
    counter = 0
    length = len(array)
    newarr = []
    while counter < length:
        newarr += array[counter],
        counter += 2
    print(newarr)


everyother(arr2)

################################################################
arr3 = [4, 2, 7, 1, 3]


# noinspection SpellCheckingInspection


def insertionsort(arr):
    numswaps = 0
    arrlen = len(arr)
    for i in range(1, arrlen):
        temp = arr[i]
        checkleft = i - 1
        while checkleft >= 0:
            if temp < arr[checkleft]:
                arr[checkleft + 1] = arr[checkleft]
            else:
                break
            checkleft -= 1
        numswaps += 1
        arr[checkleft + 1] = temp
    return arr, numswaps


arr3, num3 = insertionsort(arr3)
print(arr3, num3)
