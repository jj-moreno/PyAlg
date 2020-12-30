arr1 = [4, 2, 7, 1, 3]


# noinspection SpellCheckingInspection
def bubblesort(arr):
    dynamiclen = len(arr) - 1
    issorted = False
    while not issorted:
        issorted = True
        for i in range(dynamiclen):
            if arr[i] > arr[i + 1]:
                issorted = False
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        dynamiclen -= 1
    return arr


arr1 = bubblesort(arr1)
print(arr1)
