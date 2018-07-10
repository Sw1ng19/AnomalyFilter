# -*- coding:utf-8 -*-
# Author: lishiyun19 
# Mail: lishiyun19@163.com
# Created Time: Tue Sep 19 14:20:55 2017

import reader
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import canvas

thps_key = 'data.total_bytes_received'
cpus_key = 'avg(data.pct_cpu)'

def detect():
    # read the data
    thpDict, cpuDict = reader.read()

    # caculate length
    thpLen = len(thpDict)
    cpuLen = len(cpuDict)
    length = min(thpLen, cpuLen)

    i = 0
    xOrigin = []
    thpList = []
    cpuList = []
    thpSum = 0
    cpuSum = 0
    while (i < length):
        thpList.append(thpDict[i][thps_key])
        thpSum += float(thpDict[i][thps_key])
        cpuList.append(cpuDict[i][cpus_key])
        cpuSum += float(cpuDict[i][cpus_key])
        i += 1

    # print thpList
    canvas.drawLine(thpList, cpuList)
    # print "the average throughput is %s MB per minute" % (thpSum/length/1024**2)
    # print "the average CPU load is %s percent" % (cpuSum/length)

    # normalization data
    i = 0
    while (i < length):
        thp = float(thpList[i])/1024.0**3
        cpu = float(cpuList[i])/100.0
        xOrigin.append([cpu, thp])
        i += 1

    # transfer list to matrix and train data
    xTrain = np.array(xOrigin)
    # print xTrain

    rng = np.random.RandomState(42)
    clf = IsolationForest(max_samples=length, random_state=rng)
    clf.fit(xTrain)
    canvas.drawScatter(clf, xTrain)

    # eliminate noise data
    y_train = clf.predict(xOrigin)
    i = 0
    index = []
    for y in y_train:
        if y == -1:
            index.append(i)
        i += 1

    j = 0
    for i in index:
        del (thpList[i - j])
        del (cpuList[i - j])
        j += 1

    # draw line & scatter
    canvas.drawLine(thpList, cpuList)
    length = len(thpList)
    xOrigin = []
    i = 0
    while (i < length):
        thp = float(thpList[i]) / 1024.0 ** 3
        cpu = float(cpuList[i]) / 100.0
        xOrigin.append([cpu, thp])
        i += 1

    xTrain = np.array(xOrigin)
    canvas.drawScatter(clf, xTrain)

if __name__ == "__main__":
    detect()
