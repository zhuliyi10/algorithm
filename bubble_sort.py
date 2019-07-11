# 冒泡排序

def bubbleSort(arr):
    """
    冒泡排序也是一种简单直观的排序算法。
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
    每一轮都会确定后面最大的数
    稳定性：稳定
    时间复杂度：O(n²)
    """
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [12, 11, 13, 5, 6]
bubbleSort(arr)
print("排序后的数组：")
for data in arr:
    print("%d" % data)