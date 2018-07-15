# -*- coding:utf-8 -*-
# Author: lishiyun19 
# Mail: lishiyun19@163.com
# Created Time: Tue Sep 19 14:20:55 2017

import csv


def read():
    with open('HEC.csv', 'rb') as file:
        reader = csv.DictReader(file)
        thpDict = [thp for thp in reader]

    with open('CPU.csv', 'rb') as file:
        reader = csv.DictReader(file)
        cpuDict = [cpu for cpu in reader]
    return thpDict,cpuDict
