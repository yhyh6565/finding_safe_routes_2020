import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import descartes
import chardet

# CCTV 데이터 전처리
'''
with open('전국CCTV표준데이터.csv', 'rb') as rawdata:
    result = chardet.detect(rawdata.read(50000))
print(result)
'''
cctv_data = pd.read_csv('전국CCTV표준데이터.csv', encoding = 'EUC-KR')
#print(cctv_data.shape)
#print(cctv_data.head())

final_cctv = pd.get_dummies(cctv_data[['위도','경도']])
cctv_lat = final_cctv.iloc[:,0]
cctv_long = final_cctv.iloc[:,1]

#print(cctv_lat.head())
#print(cctv_long.head())
#print(final_cctv[:3])


# 안심벨 데이터 전처리
'''
with open('서울특별시_안전비상벨위치_20180801.csv', 'rb') as rawdata:
    result = chardet.detect(rawdata.read(50000))
print(result)
'''
bell_data = pd.read_csv('서울특별시_안전비상벨위치_20180801.csv', encoding = 'EUC-KR')
#print(bell_data.shape)

final_bell = pd.get_dummies(bell_data[['위도','경도']])
bell_lat = final_bell.iloc[:,0]
bell_long = final_bell.iloc[:,1]

#print(bell_lat.head())
#print(bell_long.head())
#print(final_bell[:3])

# 지도 위에 위치 데이터 표기
#from mpl_toolkits.basemap import Basemap
#import csv

