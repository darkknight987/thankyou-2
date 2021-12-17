import pandas as pd 
import numpy as np
df = pd.read_csv("diabetes.csv")
BP_list = list(df['BloodPressure'])
def equifreq(array, m):
    a = len(array)
    n = int(a / m)
    bins = []
    for i in range(0, m):
        arr = []
        for j in range(i * n, (i + 1) * n):
            if j >= a:
                break
            arr = arr + [array[j]]
        bins.append(arr) 
    return bins
ef_bins = equifreq(BP_list, 3)
for i in ef_bins : print (i)
def sm_mean(arr):
    arr1 = arr[:]
    mean = np.mean(np.array(arr1))
    for i in range(len(arr1)):
        arr1[i] = mean
    return arr1
ef_bin_mean = []
for i in ef_bins:
    x = sm_mean(i)
    ef_bin_mean.append(x)
for i in ef_bin_mean : print(i)
def sm_median(arr):
    arr1 = arr[:]
    median = np.median(np.array(arr1))
    for i in range(len(arr1)):
        arr1[i] = median
    return arr1
ef_bin_median = []
for i in ef_bins:
    x = sm_median(i)
    ef_bin_median.append(x)
for i in ef_bin_median : print(i)
def boundry(arr):
    arr1 = arr[:]
    max_boundry = max(arr1)
    min_boundry = min(arr1)
    for i in range(len(arr1)):
        if arr1[i]-min_boundry < max_boundry-arr1[i]:
            arr1[i] = min_boundry
        else:
            arr1[i] = max_boundry
    return arr1
ef_bin_boundry = []
for i in ef_bins:
    x = boundry(i)
    ef_bin_boundry.append(x)
for i in ef_bin_boundry : print(i)
def equiwidth(array,m):
    a = len(array)
    min1 = min(array)
    w = (max(array)-min(array))/m
    bins = []     
    for i in range(0, m):
        arr = []
        for j in array:
            if j >= (min1 + (w * i)) and j <= (min1 + (w * (i+1))):
                arr += [j]
        bins += [arr]
    return(bins)
ew_bins = equiwidth(BP_list, 4)
for i in ew_bins: print(i)
ew_bin_boundry = []
for i in ew_bins:
    x = boundry(i)
    ew_bin_boundry.append(x)
for i in ew_bin_boundry : print(i)
ew_bin_median = []
for i in ew_bins:
    x = sm_median(i)
    ew_bin_median.append(x)
for i in ew_bin_median : print(i)
ew_bin_mean = []
for i in ew_bins:
    x = sm_mean(i)
    ew_bin_mean.append(x)
for i in ew_bin_mean : print(i)
