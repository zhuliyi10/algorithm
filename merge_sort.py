# 归并排序


def mergerSort(arr, l, r):
    """
    把序列分成元素尽可能相等的两半。
    把两半元素分别进行排序。
    把两个有序表合并成一个。
    稳定性：稳定
    时间复杂度O (nlogn)
    """
    if l < r:
        m = int((l+r)/2)
        mergerSort(arr, l, m)
        mergerSort(arr, m+1, r)
        merge(arr,l,m,r)


def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m
    # 创建临时数组
    L = [0]*n1
    R = [0]*n2
    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l+i]

    for j in range(0, n2):
        R[j] = arr[j+m+1]

    # 归并临时数组到 arr[l..r]
    i = 0     # 初始化第一个子数组的索引
    j = 0     # 初始化第二个子数组的索引
    k = l     # 初始归并子数组的索引

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # 拷贝 L[] 的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # 拷贝 R[] 的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 2
        k += 1


arr = [12, 11, 13, 5, 6]
mergerSort(arr, 0, len(arr)-1)
print("排序后的数组：")
for data in arr:
    print("%d" % data)
