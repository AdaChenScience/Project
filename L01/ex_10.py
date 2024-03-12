def check(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
s=input('请输入字符串S:')
print(check(s))