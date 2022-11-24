import pandas as pd
import numpy as np

train=pd.read_csv('train.tsv', sep='\t', header=0)
train_new=pd.read_csv('train_new.tsv', sep='\t', header=0)
# print(train.keys()) #Index(['id', 'len'], dtype='object')
# print(train_new.keys())   #Index(['id', 'audio', 'n_frames', 'tgt_text', 'speaker'], dtype='object')


output=[]
for i in range(len(train_new)):
    
    id=train["id"][i]
    real_id=id.split('/')[-1][:-5] #print(real_id)  #103-1240-0000
    row=train_new.loc[train_new["id"] == real_id].values[0][:3]
    output.append(row)
    print(i)

output=np.vstack(output)
print(output.shape)
df = pd.DataFrame(output, columns = ['id','audio','n_frames'])
print(df)
df.to_csv('output.csv',index=False,header=True,sep='\t')




