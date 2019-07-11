# 快速排序


def quickSort(arr, low, high):
    """

    首先任意选取一个数据（通常选用数组的第一个数）作为基准值，然后将所有比它小的数都放到它左边，所有比它大的数都放到它右边，这个过程称为一趟快速排序
    然后基准值的左右两边分成两个子数组，递归排序两个数组
    稳定性：不稳定
    时间复杂度O (nlogn)

    """
    if low < high:
        mid_index = partition(arr, low, high)
        quickSort(arr, low, mid_index-1)
        quickSort(arr, mid_index+1, high)


def partition(arr, low, high):
    mid_index = low
    key = arr[mid_index]  # 选第一个做为基准
    while low < high:
        while key <= arr[high] and high > mid_index:
            high = high-1
        arr[mid_index], arr[high] = arr[high], arr[mid_index]
        mid_index = high
        while key >= arr[low] and low < mid_index:
            low = low+1
        arr[mid_index], arr[low] = arr[low], arr[mid_index]
        mid_index = low

    return mid_index


arr = [12, 11, 13, 5, 6]
quickSort(arr,0,len(arr)-1)
print("排序后的数组：")
for data in arr:
    print("%d" % data)
