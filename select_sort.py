# 选择排序
def selectSort(arr):
    """
    选择排序是一种简单直观的排序算法。
    它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    以此类推，直到所有元素均排序完毕。
    稳定性：不稳定
    时间复杂度：O(n²)
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


arr = [12, 11, 13, 5, 6]
selectSort(arr)
print("排序后的数组：")
for data in arr:
    print("%d" % data)
