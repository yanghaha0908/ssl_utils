from numpy import *
import numpy as np
import ast

one_update=[]
fbank=[]
apply_mask=[]
Transformer=[]
Predict=[]
count=0
file="time_fbank.log"
for line in open(file,"r",encoding='UTF-8'):
    if '{' in line:
        if "[train][INFO]" in line or "valid" in line:
            continue
        index=line.find("{")
        dict=ast.literal_eval(line[index:])
        
        one_update.append(float(dict['one_update']))
        fbank.append(float(dict['fbank']))
        apply_mask.append(float(dict['apply mask']))
        Transformer.append(float(dict['Transformer']))
        Predict.append(float(dict['Predict']))
        
        count+=1
        
one_update_mean=mean(one_update)
fbank_mean= mean(fbank)
apply_mask_mean= mean(apply_mask)
Transformer_mean= mean(Transformer)
Predict_mean= mean(Predict)

# print(one_update)
# print(sum(one_update))

# average
print("fbank_analysis")
print("count:",count)
print("one_update_mean:",one_update_mean)
print("fbank_mean:",fbank_mean)
print("apply_mask_mean:",apply_mask_mean)
print("Transformer_mean:",Transformer_mean)
print("Predict_mean:",Predict_mean)


print('\n')
# # percent
# print("fbank:%.4f" % (fbank_mean/one_update_mean))
# print("apply_mask:%.4f" % (apply_mask_mean/one_update_mean))
# print("Transformer:%.4f" % (Transformer_mean/one_update_mean))
# print("Predict:%.4f"%(Predict_mean/one_update_mean))

# real percent

print("fbank:%.4f%%" % (100*fbank_mean/one_update_mean))
print("apply_mask:%.4f%%" % (100*apply_mask_mean/one_update_mean))
print("Transformer:%.4f%%" % (100*Transformer_mean/one_update_mean))
print("Predict:%.4f%%"%(100*Predict_mean/one_update_mean))

#得出一个结论 [2022-11-23 13:43:12,403][fairseq_cli.train][INFO] - end of epoch 1 (average epoch stats below)
# [2022-11-23 13:43:12,428][train][INFO] - { 后面的结果和 取sum的不一样 很奇怪？？？

print("==============================================================================================================")


one_update=[]
CNN=[]
apply_mask=[]
Transformer=[]
Predict=[]
count=0
file="time_origin.log"
for line in open(file,"r",encoding='UTF-8'):
    if '{' in line:
        if "[train][INFO]" in line or "valid" in line:
            continue
        index=line.find("{")
        dict=ast.literal_eval(line[index:])
 
        one_update.append(float(dict['one_update']))
        CNN.append(float(dict['CNN']))
        apply_mask.append(float(dict['apply mask']))
        Transformer.append(float(dict['Transformer']))
        Predict.append(float(dict['Predict']))

        count+=1
        if count==41:
            break
        
        
one_update_mean=mean(one_update)
CNN_mean= mean(CNN)
apply_mask_mean= mean(apply_mask)
Transformer_mean= mean(Transformer)
Predict_mean= mean(Predict)

# print(one_update)
# print(sum(one_update))

# average
print("CNN_analysis")
print("count:",count)
print("one_update_mean:",one_update_mean)
print("CNN_mean:",CNN_mean)
print("apply_mask_mean:",apply_mask_mean)
print("Transformer_mean:",Transformer_mean)
print("Predict_mean:",Predict_mean)

print('\n')

# # percent
# print("fbank:%.4f" % (fbank_mean/one_update_mean))
# print("apply_mask:%.4f" % (apply_mask_mean/one_update_mean))
# print("Transformer:%.4f" % (Transformer_mean/one_update_mean))
# print("Predict:%.4f"%(Predict_mean/one_update_mean))

# real percent

print("CNN:%.4f%%" % (100*CNN_mean/one_update_mean))
print("apply_mask:%.4f%%" % (100*apply_mask_mean/one_update_mean))
print("Transformer:%.4f%%" % (100*Transformer_mean/one_update_mean))
print("Predict:%.4f%%"%(100*Predict_mean/one_update_mean))