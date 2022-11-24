km="ssl/dev_clean.km"
phn="ssl/val_100.phn"

pairs=[]

km_all=[]
phn_all=[]

km_len=[]
phn_len=[]

for line in open(km,"r",encoding='UTF-8'):
    # print(line.type)
    item=(line.strip().split(' '))
    item=[int(i) for i in item]
    #print(item)  292
    #print(len(item))
    #km_all += item
    #print(km_all)
    km_len.append(len(item))
print(km_len)
    
for line in open(phn,"r",encoding='UTF-8'):
    item=(line.strip().split(' '))
    #item=[int(i) for i in item]
    #print(item)  292
    phn_len.append(len(item))
    #print(len(item))
    #phn_all += item
    #print(phn_all)

print(phn_len)


#先统计一波长度好了