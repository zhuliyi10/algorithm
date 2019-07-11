# 二分查找


def binarySearch(arr, l, r, x):
    """
    从中间开始查找，如果相等则返回下标，如果中间数大于查找数，则查找左边，如果中间数小于查找数，则查找右边
    时间复杂度 o（log（n））
    """
    if r >= l:
        mid = int((l+r)/2)
        if arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        elif arr[mid] < x:
            return binarySearch(arr, mid+1, r, x)
        else:
            return mid
    else:
        return -1


# 测试数组
arr = [3, 4]
x = 4

result = binarySearch(arr, 0, len(arr)-1, x)
if result == -1:
    print("元素不在数组中")
else:
    print("元素在数组中的索引为%d" % result)
