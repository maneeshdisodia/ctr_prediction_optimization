__author__ = 'root'

import csv
import numpy as np
import pandas.io as ps
import time
import csv
import random
import os
#import mysql.connector
#from mysql.connector import Error

os.system("rm temp vw_temp vw_temp.cache vw_temp.model ad_unit_prediction feed_prediction sorted_result")
print 'removing done'
#os.system("cat i*>>impression_data")
#os.system("cat c*>>click_data")
print 'done step 1'

X = "click_data"
Y = "impression_data"

def print_day(s):
    #if s.dtype == string and np.isnan(s):
    if s=='nan':
        print 'nan'
        return 'nan'
    else:
        struct_time = time.strptime(s, "%Y-%m-%d %H:%M:%S")
        d = time.strftime("%A", struct_time)
        # print d
        return d;

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',database='newdatabase',user='root',password='password')
        if conn.is_connected():
            print('Connected to MySQL database')
        cursor = conn.cursor()
        cursor.execute("SELECT `Id` FROM `Creatives` WHERE `Type` = 'text'")
        row = cursor.fetchall()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
    return row


#text=connect()
#new_text=[]
#for index in range(len(text)):
#    new_text.append(text[index][0])


arrSheatherData = np.asarray(ps.parsers.read_csv(X))
arrSheatherData1 = np.asarray(ps.parsers.read_csv(Y))

clk_IDs = np.asarray(arrSheatherData[:,[0,1,2,3,12]]).astype('string')
imp_IDs = np.asarray(arrSheatherData1[:,[0,1,2,3,12]]).astype('string')


print clk_IDs.shape
print imp_IDs.shape
print imp_IDs.shape[0]
print clk_IDs.shape[0]

clk_entryLevel = int(imp_IDs.shape[0]/clk_IDs.shape[0])
#clk_entryLevel = int(clk_IDs.shape[0]/imp_IDs.shape[0])


print clk_entryLevel

with open('temp', 'wb') as outcsv:
    #writer = csv.DictWriter(outcsv, fieldnames = ["LABLE","DAY", "PUB_COMPANY_ID","CREATIVE_ID", "CAMPAINGN_ID" ,"AD_UNIT_ID",])
    #writer.writeheader()
    for t in range(clk_IDs.shape[0]):

        if clk_IDs[t][0]=='nan' or clk_IDs[t][1]=='nan' or clk_IDs[t][2]=='nan'or clk_IDs[t][3]=='nan'or clk_IDs[t][4]=='nan':
            print 'nxt click'
            #writer.writerow({'LABLE': 1.0, 'DAY':print_day(clk_IDs[t][4]), 'PUB_COMPANY_ID': clk_IDs[t][0], 'CREATIVE_ID': clk_IDs[t][1] , 'CAMPAINGN_ID': clk_IDs[t][2] ,'AD_UNIT_ID': clk_IDs[t][3]})
        elif clk_IDs[t][0]=='0' or clk_IDs[t][1]=='0' or clk_IDs[t][2]=='0'or clk_IDs[t][3]=='0':
            print 'csir testing click'
        elif clk_IDs[t][0]=='0.0' or clk_IDs[t][1]=='0.0' or clk_IDs[t][2]=='0.0'or clk_IDs[t][3]=='0.0':
            print 'csir testing click'
        elif clk_IDs[t][1]=='[CREATIVEID]' or clk_IDs[t][3]=='[ADUNITID]':
            print '[ADUNITID] [CREATIVEID]'
        #      elif ( int(clk_IDs[t][1])  in new_text ):
        #       print "text link found"
        else:
            outcsv.write("1 1.0 'CAMPAINGN-ID_%s_DAY_%s_PUB-COMPANY-ID_%s_CREATIVE-ID_%s_AD-UNIT-ID_%s|DAY %s |PUB_COMPANY_ID:%s CREATIVE_ID:%s CAMPAINGN_ID:%s AD_UNIT_ID:%s\n"%(int(float(clk_IDs[t][2])),print_day(clk_IDs[t][4]),int(float(clk_IDs[t][0])),int(float(clk_IDs[t][1])),int(float(clk_IDs[t][3])),print_day(clk_IDs[t][4]),int(float(clk_IDs[t][0])),int(float(clk_IDs[t][1])),int(float(clk_IDs[t][2])),int(float(clk_IDs[t][3]))))
    for i in range(imp_IDs.shape[0]):

        if imp_IDs[i][0]=='nan' or imp_IDs[i][1]=='nan' or imp_IDs[i][2]=='nan' or imp_IDs[i][3]=='nan' or  imp_IDs[i][4]=='nan':
            print 'nxt impression'
        elif imp_IDs[i][0]=='0.0' or imp_IDs[i][1]=='0.0' or imp_IDs[i][2]=='0.0' or imp_IDs[i][3]=='0.0' :
            print 'csir testing impression'
            #writer.writerow({'LABLE': 0.0, 'DAY':print_day(imp_IDs[x][4]), 'PUB_COMPANY_ID': imp_IDs[x][0], 'CREATIVE_ID': imp_IDs[x][1] , 'CAMPAINGN_ID': imp_IDs[x][2] ,'AD_UNIT_ID': imp_IDs[x][3]})
        elif imp_IDs[i][0]=='0' or imp_IDs[i][1]=='0' or imp_IDs[i][2]=='0' or imp_IDs[i][3]=='0' :
            print 'csir testing impression'
        elif imp_IDs[t][1]=='[CREATIVEID]' or imp_IDs[t][3]=='[ADUNITID]':
            print '[ADUNITID] [CREATIVEID]'
        else:
            outcsv.write("0 1.0 'CAMPAINGN-ID_%s_DAY_%s_PUB-COMPANY-ID_%s_CREATIVE-ID_%s_AD-UNIT-ID_%s|DAY %s |PUB_COMPANY_ID:%s CREATIVE_ID:%s CAMPAINGN_ID:%s AD_UNIT_ID:%s\n"%(int(float(imp_IDs[i][2])),print_day(imp_IDs[i][4]),int(float(imp_IDs[i][0])),int(float(imp_IDs[i][1])),int(float(imp_IDs[i][3])),print_day(imp_IDs[i][4]),int(float(imp_IDs[i][0])),int(float(imp_IDs[i][1])),int(float(imp_IDs[i][2])),int(float(imp_IDs[i][3]))))
print 'step 2: mearging done,vw format done'
input_path = "temp"
output_path = "vw_temp"

print 'step3 done ,suffeling file'
with open(input_path, "rb") as file:
    rows = list(csv.reader(file, delimiter=","))

random.shuffle(rows)

with open(output_path, "wb") as file:
    csv.writer(file, delimiter=",").writerows(rows)

print 'step4 learning system'
os.system("vw vw_temp -l 10 --loss_function=logistic --link=logistic  -c -f vw_temp.model && vw -i vw_temp.model -t vw_temp -p  /dev/stdout --quiet >> feed_prediction && awk '!seen[$0]++' feed_prediction >> ad_unit_prediction && echo Verified_and_executed|| echo commmand Down")
os.system("echo hii")
#os.system("sort -n -k1,1 ad_unit_prediction >> sorted_result")
print 'sorted_results are prepared'