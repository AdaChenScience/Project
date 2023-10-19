def statistic(file):
    f=open(file)
    d=dict()
    for line in f.readlines():
        if len(line)>10:
            mark=[',','.','!','?',':',';','\'s','(',')']
            for m in mark:
                line=line.replace(m,'')
            lineattr=line.strip().split(' ')
            for char in lineattr:
                if char not in d:
                    d[char]=1
                else:
                    d[char]+=1
    a=sorted(d.items(),key=lambda x:x[1],reverse=True)
    return a

result=statistic('./data/sonnets.txt')
print(result[:20])