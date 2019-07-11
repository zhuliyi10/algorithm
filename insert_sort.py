# 插入排序
def insertSort(arr):
    """
    插入排序是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    稳定性：稳定
    时间复杂度：O(n²)

    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            j = j-1


arr = [12, 11, 13, 5, 6]
insertSort(arr)
print("排序后的数组：")
for data in arr:
    print("%d" % data)
