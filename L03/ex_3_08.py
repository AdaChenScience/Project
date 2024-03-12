import time
import random
import sort_algorithm

n=int(input('请输入待排序数组长度:'))
array = [random.uniform(0,1) for i in range(n)]

t1 = time.perf_counter()
print('开始计时')

res1= sort_algorithm.bubble_sort(array.copy())
t2 = time.perf_counter()
print('冒泡排序耗时: %.6fs'%(t2-t1))

res2= sort_algorithm.select_sort(array.copy())
t3 = time.perf_counter()
print('选择排序耗时: %.6fs'%(t3-t2))

res3= sort_algorithm.insert_sort(array.copy())
t4 = time.perf_counter()
print('插入排序耗时: %.6fs'%(t4-t3))

res4= sort_algorithm.shell_sort(array.copy())
t5 = time.perf_counter()
print('希尔排序耗时: %.6fs'%(t5-t4))

res5= sort_algorithm.merge_sort(array.copy())
t6 = time.perf_counter()
print('归并排序耗时: %.6fs'%(t6-t5))

res6= sort_algorithm.quick_sort(array.copy())
t7 = time.perf_counter()
print('快速排序耗时: %.6fs'%(t7-t6))

res7= sort_algorithm.heap_sort(array.copy())
t8 = time.perf_counter()
print('堆排序耗时:   %.6fs'%(t8-t7))
