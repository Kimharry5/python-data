
import pandas as pd
from pandas import DataFrame as df
from pandas import Series
import numpy as np 


#user에 관한 데이터
users = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\users.dat', sep = '::', engine = 'python',
                   names = ['userId', 'gender','age','job','zipcode'])
#movie에 관한 데이터
movies = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\movies.dat', sep = '::', engine = 'python',
                   names = ['movieId', 'title','genre'])     
#rating에 관한 데이터
ratings = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\ratings.dat', sep = '::', engine = 'python',
                   names = ['userId', 'movieId','rate','timestamp'])
#3개의 데이터 합치기
data = pd.merge(movies,ratings,on='movieId')
data = pd.merge(data,users,on='userId')

 #--------------------------------------영화별 평점 정렬, 높은것 5개
def df_Sort_Rate():
    
    pd.options.display.float_format = '{:.1f}'.format
    best_moives = (pd.pivot_table(data=data, index='title', values='rate', aggfunc='mean')
                .rename(columns={'rate' : 'mean_rate'})
                )
    data2 = pd.merge(data,best_moives, on = 'title')
    data3 = data2.drop_duplicates('title')
    df_sort_rate = data3[ ['title','mean_rate'] ].sort_values(by='mean_rate', ascending=False).reset_index(drop=True)  #영화 평점순 
    df_sort_rate5 = df_sort_rate[:5]# 평점 best5 영화
   # print('<영화 평점 높은순> \n',df_sort_rate,'\n','<영화 평점 best5> \n',df_sort_rate5) 



def df_Sort_Rate5():
    
    pd.options.display.float_format = '{:.1f}'.format
    best_moives = (pd.pivot_table(data=data, index='title', values='rate', aggfunc='mean')
                .rename(columns={'rate' : 'mean_rate'})
                )
    data2 = pd.merge(data,best_moives, on = 'title')
    data3 = data2.drop_duplicates('title')
    df_sort_rate = data3[ ['title','mean_rate'] ].sort_values(by='mean_rate', ascending=False).reset_index(drop=True)  #영화 평점순 
    df_sort_rate5 = df_sort_rate[:5]# 평점 best5 영화
   # print('<영화 평점 높은순> \n',df_sort_rate,'\n','<영화 평점 best5> \n',df_sort_rate5) 


#------------------------각 연령대 영화 추천 5개 (평점 높은순)-------------------------
def age_Rate():
    age_rate = data.pivot_table ( index = 'title', columns = 'age'  , aggfunc = 'mean'
                                ,values ='rate'
                                ,fill_value= 0
                                )
   # print(age_rate)

#-----------------------영화 제목과 개봉년도 분리
def movies_release():
    movies['release'] = movies['title'].str[-5:-1]
    movies['title'] = movies['title'].str[:-6]
   # print(movies)
