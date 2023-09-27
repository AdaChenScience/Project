def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'F'
n=float(input('请输入百分制成绩:'))
print('转换为等级制为:', grade(n))