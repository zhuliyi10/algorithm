# 希尔排序


def shellSort(arr):
    """
    希尔排序是插入排序的一种更高效的改进版本
    先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
    稳定性：不稳定
    时间复杂度O (nlogn)
    """
    n=len(arr)
    mid=int(n/2)
    while mid>0:
        for i in range(mid,n):
            temp=arr[i]
            j=i
            while j>=mid and arr[j-mid]>temp:
                arr[j]=arr[j-mid]
                j-=mid
            arr[j]=temp
        mid=int(mid/2)


arr = [12, 11, 13, 5, 6]
shellSort(arr)
print("排序后的数组：")
for data in arr:
    print("%d" % data)