import numpy as np
import matplotlib.pyplot as plt

# path = "finetune_results.xlsx"
# data = np.loadtxt(path, dtype=np.float32, delimiter=",")
# print(data)

# 取平均补了一个数
x=[20,40,60,80,100,120,140,160,180,200,220,240,260,280]
original=[24.286,18.211,16.332,15.369,14.228,14.093,13.738,13.722,13.647,13.514,13.48,13.396,13.27,13.319]
phoneme_mask=[None,37.411,34.55,31.689,30.3,29.469,28.294,27.915,27.693,27.175,26.812,26.955,26.441,26.054]
phoneme_nomask=[30.058,23.862,22.372,21.642,21.343,21.222,21.228,21.249,21.196,21.078,21.561,21.408,21.612,21.475]
fbank=[44.204,36.19,33.766,32.186,31.624,30.407,29.715,29.351,28.914,28.916,28.5,28.382,28.433,28.451]

plt.xlabel('epoch_num')
plt.ylabel('best_WER')

plt.plot(x,original,marker='o',markersize='3',markerfacecolor='white')
plt.plot(x,phoneme_mask,marker='o',markersize='3',markerfacecolor='white')
plt.plot(x,phoneme_nomask,marker='o',markersize='3',markerfacecolor='white')
plt.plot(x,fbank,marker='o',markersize='3',markerfacecolor='white')

plt.legend(['original', 'phoneme_mask', 'phoneme_nomask', 'fbank'])
plt.savefig("finetune_results.png",dpi=500)
plt.show()
