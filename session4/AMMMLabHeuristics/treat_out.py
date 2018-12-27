import os
path = './outputs'
results=[]
for filename in os.listdir(path):
    with open(os.path.join(path,filename),"r") as f:
        row = [filename]
        pos=-1
        for line in f.readlines():
            if 'Elap.' in line:
                pos=2
            elif pos>0:
                pos-=1
            elif pos==0:
                row.append(line.split()[0])
                row.append(line.split()[1])
                results.append(row)
                pos=-1

print(results)
