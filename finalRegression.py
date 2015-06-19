
__author__ = 'machine'

import numpy as np
import pandas.io as ps
import pandas as pa
import time
import csv
import random
import os

os.system("rm xab xaa temp vw_temp vw_temp.cache vw_temp.model ad_unit_prediction feed_prediction sorted_result")
print 'removing done'

# X = "mini.csv"
#X = "chopSample.csv"
X = "data.csv"
arrSheatherData = np.asarray(ps.parsers.read_csv(X, skiprows=1))

x2array = np.asarray(arrSheatherData[:]).astype('int')

print x2array.shape
print x2array.shape[0]
print x2array.shape[1]

click = np.array([1])
miss = np.array([0])
count = 0
with open('temp', 'wb') as outcsv:
    for y in range(x2array.shape[0]):




        if 1 in x2array[y]:
            #x = np.in1d(x2array[y], click[1]).any()
            # x= np.where(pa.Index(pa.unique(click)).get_indexer(x2array[y]) >= 0)
            count = count + 1
            print count
            outcsv.write(
                "1 1.0 'A_B_C_D| a1:.%s| a2:.%s| a3:.%s| a4:.%s| a5:.%s| a6:.%s| a7:.%s| a8:.%s | b1:.%s| b2:.%s| b3:.%s| b4:.%s| b5:.%s| b6:.%s| b7:.%s| b8:.%s | c1:.%s| c2:.%s| c3:.%s| c4:.%s| c5:.%s| c6:.%s| c7:.%s| c8:.%s | d1:.%s| d2:.%s| d3:.%s| d4:.%s| d5:.%s| d6:.%s| d7:.%s| d8:.%s \n" % (
                    x2array[y][0], x2array[y][1], x2array[y][2], x2array[y][3], x2array[y][4], x2array[y][5],
                    x2array[y][6], x2array[y][7], x2array[y][8], x2array[y][9], x2array[y][10], x2array[y][11],
                    x2array[y][12], x2array[y][13], x2array[y][14], x2array[y][15], x2array[y][16], x2array[y][17],
                    x2array[y][18], x2array[y][19], x2array[y][20], x2array[y][21], x2array[y][22], x2array[y][23],
                    x2array[y][24], x2array[y][25], x2array[y][26], x2array[y][27], x2array[y][28], x2array[y][29],
                    x2array[y][30], x2array[y][31]))


        else:
            outcsv.write(
                "-1 1.0 'A_B_C_D| a1:.%s| a2:.%s| a3:.%s| a4:.%s| a5:.%s| a6:.%s| a7:.%s| a8:.%s | b1:.%s| b2:.%s| b3:.%s| b4:.%s| b5:.%s| b6:.%s| b7:.%s| b8:.%s | c1:.%s| c2:.%s| c3:.%s| c4:.%s| c5:.%s| c6:.%s| c7:.%s| c8:.%s | d1:.%s| d2:.%s| d3:.%s| d4:.%s| d5:.%s| d6:.%s| d7:.%s| d8:.%s \n" % (
                    x2array[y][0], x2array[y][1], x2array[y][2], x2array[y][3], x2array[y][4], x2array[y][5],
                    x2array[y][6], x2array[y][7], x2array[y][8], x2array[y][9], x2array[y][10], x2array[y][11],
                    x2array[y][12], x2array[y][13], x2array[y][14], x2array[y][15], x2array[y][16], x2array[y][17],
                    x2array[y][18], x2array[y][19], x2array[y][20], x2array[y][21], x2array[y][22], x2array[y][23],
                    x2array[y][24], x2array[y][25], x2array[y][26], x2array[y][27], x2array[y][28], x2array[y][29],
                    x2array[y][30], x2array[y][31]))
# input_path = "temp"

output_path = "vw_temp"
input_path = "temp"
print 'step3 done ,suffeling file'
with open(input_path, "rb") as file:
    rows = list(csv.reader(file, delimiter=","))

random.shuffle(rows)
with open(output_path, "wb") as file:
    csv.writer(file, delimiter=",").writerows(rows)
size= int(x2array.shape[0])* (0.7)
size= int(size)
print int(size)
split = 'split -l '+str(size)+' vw_temp || echo commmand Down'
print split
os.system(split)

print "preparing train_data and test_data"

test_data = "xab"
train_data = "xaa"

print 'step4 learning system with 70% of giver data as training data and 30% to test'
os.system("vw vw_temp -l 1 --loss_function=logistic --link=logistic  -c -f vw_temp.model && vw -i vw_temp.model -t xab -p  /dev/stdout --quiet >> feed_prediction && awk '!seen[$0]++' feed_prediction >> ad_unit_prediction && echo Verified_and_executed|| echo commmand Down")

#os.system("vw vw_temp -l 10 --loss_function=logistic --link=logistic  -c -f vw_temp.model && vw -i vw_temp.model -t vw_temp -p  /dev/stdout --quiet >> feed_prediction && awk '!seen[$0]++' feed_prediction >> ad_unit_prediction && echo Verified_and_executed|| echo commmand Down")

#os.system("vw train_data -l 10 --loss_function=logistic --link=logistic  -c -f  train.model && vw -i train.model -t testing -p  /dev/stdout --quiet >> feed_prediction && awk '!seen[$0]++' feed_prediction >> ad_unit_prediction  &&  echo Verified_and_executed|| echo commmand Down")
os.system("echo hii...its done")
os.system("sort -n -k1,1 ad_unit_prediction >> sorted_result")
print 'sorted_results are prepared'






