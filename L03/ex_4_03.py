import random
import sort_algorithm
array=[round(random.uniform(0,1),2) for i in range(10)]
new_array=sort_algorithm.insert_sort(array.copy())
print('原数组为:',array)
print('排序后为:',new_array)