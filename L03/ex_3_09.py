a=[float(i) for i in input('请输入数组A(元素以空格分隔):').split(' ')]
def dq(arr):
    if len(arr)==1:
        return [1],arr[0]
    left,ltotal=dq(arr[:len(arr)//2])
    right,rtotal=dq(arr[len(arr)//2:])
    total=[i*rtotal for i in left]+[i*ltotal for i in right]
    return total,ltotal*rtotal
print('对应的数组B为:',dq(a)[0])