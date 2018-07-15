# -*- coding:utf-8 -*-
# Author: lishiyun19 
# Mail: lishiyun19@163.com
# Created Time: Tue Sep 19 14:20:55 2017

import matplotlib.pyplot as plt
import numpy as np


def drawLine(thpList, cpuList):
    # plot the origin line
    x = range(0, len(thpList))
    plt.plot(x, thpList, label='origin throughput', linewidth=2, color='r', marker='o',
             markerfacecolor='blue', markersize=12)
    plt.ylim(100000000, 1000000000)
    plt.show()

    plt.plot(x, cpuList, label='origin cpu', linewidth=2, color='r', marker='o',
             markerfacecolor='blue', markersize=12)
    plt.ylim(0, 100)
    plt.show()

def drawScatter(clf, xTrain):
    # plot the line and coordinate
    xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 50), np.linspace(-0.5, 1.5, 50))
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # plot the scatter
    plt.title("IsolationForest")
    plt.contourf(xx, yy, Z)
    scatter = plt.scatter(xTrain[:, 0], xTrain[:, 1], c='black')
    plt.axis('tight')
    plt.xlim((-0.5, 1.5))
    plt.ylim((-0.5, 1.5))
    plt.legend([scatter], ["IsolationForest"], loc="upper right")
    plt.show()
