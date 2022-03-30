# -*- coding: utf-8 -*-
""" 
@Time    : 2022/3/10 15:43
@Author  : Chen_Sir
@FileName: draw7.py
@SoftWare: PyCharm
"""
# Integer_underFlow
import csv
import matplotlib.pyplot as plt
csv_file = csv.reader(open("../Integer_UnderFlow.CSV"))
epoch = []
accuracy = []
loss = []
accuracy_1 = []
loss_1 = []
for info in csv_file:
    if csv_file.line_num == 1:
        continue
    epoch.append(int(info[0]) + 1)
    accuracy.append(float(info[1]) * 100)
    loss.append(float(info[2]) * 100)
    accuracy_1.append(float(info[3]) * 100)
    loss_1.append(float(info[4]) * 100)

# for info in csv_file:
#     if csv_file.line_num == 1:
#         continue

plt.plot(epoch, accuracy,lw=1.5, color='b', label='train acc', marker='.', markevery=1,
                 mew=1)
plt.plot(epoch, loss, lw=1.5, color='r', label='train acc', marker='.', markevery=1,
                 mew=1)
plt.plot(epoch, accuracy_1,lw=1.5, color='y', label='train acc', marker='.', markevery=1,
                 mew=1)
plt.plot(epoch, loss_1, lw=1.5, color='g', label='train acc', marker='.', markevery=1,
                 mew=1)
plt.xlabel("epochs", fontsize=12)
plt.ylabel("Accuracy", fontsize=12)
plt.show()
