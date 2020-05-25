
import pandas as pd
from pandas import DataFrame as df
from pandas import Series
import numpy as np 
import requests
import json

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
    #df_sort_rate5 = df_sort_rate[:5]# 평점 best5 영화
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
    age_rate_1 = age_rate.sort_values(by = 1 , ascending = False)[1].iloc[:5]

    age_rate2 = age_rate.sort_values(by = 18 , ascending = False)[18].iloc[:5]

    age_rate3 = age_rate.sort_values(by = 25 , ascending = False)[25].iloc[:5]

    age_rate4 = age_rate.sort_values(by = 35 , ascending = False)[35].iloc[:5]

    age_rate5 = age_rate.sort_values(by = 45 , ascending = False)[45].iloc[:5]

    age_rate6 = age_rate.sort_values(by = 50 , ascending = False)[50].iloc[:5]

    age_rate7 = age_rate.sort_values(by = 56 , ascending = False)[56].iloc[:5]
    
    print(age_rate3)
#---->로그인 한 후 유저에 맞춰? 랜덤으로?

#-----------------------영화 최신 개봉순
def movies_release():
    movies['release'] = movies['title'].str[-5:-1]
    movies['title'] = movies['title'].str[:-6]
   # print(movies)
    
    #최신 개봉순
    movies_rsort = movies.sort_values(by = 'release' , ascending = False)
    #최신 개봉순 5개
    movies_rsort5 = movies.sort_values(by = 'release' , ascending = False).iloc[:5] 









#test--------------------------------------------------------------------------

def create_movies() : 
    #movies = open('E:\\코멘토\\2주차\\영화데이터\\movies.dat', 'r', encoding='ISO-8859-1')
   # request_data ={'movies':[]}
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
    #함수마다 데이터 불러와야하나?



    pd.options.display.float_format = '{:.1f}'.format
    best_moives = (pd.pivot_table(data=data, index='title', values='rate', aggfunc='mean')
                .rename(columns={'rate' : 'mean_rate'})
                )
    data2 = pd.merge(data,best_moives, on = 'title')
    data3 = data2.drop_duplicates('title')
    df_sort_rate = data3[ ['title','mean_rate'] ].sort_values(by='mean_rate', ascending=False).reset_index(drop=True)  #영화 평점순 
    df_sort_rate = df_sort_rate.to_json()
    API_URL =  'http://127.0.0.1:8000/api/'
    headers = {'content-type': 'application/json; charset=utf8'}
    response = requests.post(API_URL + 'movies/', data = json.dumps(df_sort_rate), headers = headers)
    print(response.text)

create_movies()

