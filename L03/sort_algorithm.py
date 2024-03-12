# 优化后冒泡排序
def bubble_sort(ary):
	n = len(ary)
	k = n    #k为循环的范围，初始值n
	for i in range(n):
		flag = True
		for j in range(1, k):    #只遍历到最后交换的位置即可
			if ary[j-1] > ary[j]:
				ary[j-1], ary[j] = ary[j], ary[j-1]
				k = j     #记录最后交换的位置
				flag = False
		if flag:
			break
	return ary
				
# 选择排序
def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if ary[j] < ary[min] :
                min = j                     #找到最小值的下标
        ary[min],ary[i] = ary[i],ary[min]   #交换两者
    return ary

# 插入排序
def insert_sort(ary):
	count = len(ary)
	for i in range(1, count):
		key = i - 1
		mark = ary[i]    # 注： 必须将ary[i]赋值为mark，不能直接用ary[i]
		while key >= 0 and ary[key] > mark:
			ary[key+1] = ary[key]
			key -= 1
		ary[key+1] = mark
	return ary

# 希尔排序
def shell_sort(ary):
    count = len(ary)
    gap = round(count / 2)
    # 双杠用于整除（向下取整），在python直接用 “/” 得到的永远是浮点数，
    # 用round()得到四舍五入值
    while gap >= 1:
        for i in range(gap, count):
            temp = ary[i]
            j = i
            while j - gap >= 0 and ary[j - gap] > temp:  # 到这里与插入排序一样了
                ary[j] = ary[j - gap]
                j -= gap
            ary[j] = temp
        gap = round(gap / 2)
    return ary

# 归并排序
def merge_sort(ary):    
    if len(ary) <= 1:
        return ary    
    median = int(len(ary)/2)    # 二分分解
    left = merge_sort(ary[:median])
    right = merge_sort(ary[median:])
    return merge(left, right)    # 合并数组
def merge(left, right):
    res = []
    i = j = k = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1           
    res = res + left[i:] + right[j:]
    return res

# 快速排序
def quick_sort(ary):
    return qsort(ary, 0, len(ary) - 1)
def qsort(ary, start, end):
    if start < end:
        left = start
        right = end
        key = ary[start]
    else:
        return ary
    while left < right:
        while left < right and ary[right] >= key:
            right -= 1
        if left < right:  # 说明打破while循环的原因是ary[right] <= key
            ary[left] = ary[right]
            left += 1
        while left < right and ary[left] < key:
            left += 1
        if left < right:  # 说明打破while循环的原因是ary[left] >= key
            ary[right] = ary[left]
            right -= 1
    ary[left] = key  # 此时，left=right，用key来填坑

    qsort(ary, start, left - 1)
    qsort(ary, left + 1, end)
    return ary

# 堆排序
def heap_sort(ary):
	n = len(ary)
	first = int(n/2-1)    #最后一个非叶子节点
	for start in range(first,-1,-1):    #构建最大堆
		max_heapify(ary,start,n-1)
	for end in range(n-1,0,-1):    #堆排，将最大跟堆转换成有序数组
		ary[end],ary[0] = ary[0], ary[end]    #将根节点元素与最后叶子节点进行互换，取出最大根节点元素，对剩余节点重新构建最大堆
		max_heapify(ary,0,end-1)    #因为end上面取的是n-1，故而这里直接放end-1，相当于忽略了最后最大根节点元素ary[n-1]
	return ary
#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
	root = start
	while True:
		child = root * 2 + 1    #调整节点的子节点
		if child > end:
			break
		if child + 1 <= end and ary[child] < ary[child+1]:
			child = child + 1   #取较大的子节点
		if ary[root] < ary[child]:    #较大的子节点成为父节点
			ary[root], ary[child] = ary[child], ary[root]    #交换
			root = child
		else:
			break
