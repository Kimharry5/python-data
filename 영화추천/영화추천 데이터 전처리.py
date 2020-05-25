
import pandas as pd
from pandas import DataFrame as df
from pandas import Series
import numpy as np 
import matplotlib.pyplot as plt
#%matplotlib inline

movie_file=open('E:\\코멘토\\2주차\\영화데이터\\movies.dat', encoding='UTF8')
user_file = open('E:\\코멘토\\2주차\\영화데이터\\users.dat', encoding='UTF8')
rating_file = open('E:\\코멘토\\2주차\\영화데이터\\ratings.dat', encoding='UTF8')


#user에 관한 데이터
users = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\users.dat', sep = '::', engine = 'python',
                   names = ['userId', 'gender','age','job','zipcode'])
#print(users)  
                 
#movie에 관한 데이터
movies = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\movies.dat', sep = '::', engine = 'python',
                   names = ['movieId', 'title','genre'])
#print(movies)      

#rating에 관한 데이터
ratings = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\ratings.dat', sep = '::', engine = 'python',
                   names = ['userId', 'movieId','rate','timestamp'])
#print(ratings)      

#3개의 데이터 합치기
data = pd.merge(movies,ratings,on='movieId')
data = pd.merge(data,users,on='userId')
# ----------------------------------------

#--------------------------------------영화별 평점 정렬, 높은것 5개
pd.options.display.float_format = '{:.1f}'.format
best_moives = (pd.pivot_table(data=data, index='title', values='rate', aggfunc='mean')
            .rename(columns={'rate' : 'mean_rate'})
            )
data2 = pd.merge(data,best_moives, on = 'title')
data3 = data2.drop_duplicates('title')
df_sort_rate = data3[ ['title','mean_rate'] ].sort_values(by='mean_rate', ascending=False).reset_index(drop=True)  #영화 평점순 
df_sort_rate5 = df_sort_rate[:5]# 평점 best5 영화
print('<영화 평점 높은순> \n',df_sort_rate,'\n','<영화 평점 best5> \n',df_sort_rate5) 

#----------출력결과--------------------------------------------------------------------
#<영화 평점 높은순> 
#                                    title  mean_rate
#0     Gate of Heavenly Peace, The (1995)        5.0 
#1                           Lured (1947)        5.0 
#2                   Smashing Time (1967)        5.0 
#3               One Little Indian (1973)        5.0 
#4                 Song of Freedom (1936)        5.0 
#...                                  ...        ... 
#3701                  Get Over It (1996)        1.0 
#3702                      Cheetah (1989)        1.0
#3703                    Sleepover (1995)        1.0
#3704                Venice/Venice (1992)        1.0
#3705                   White Boys (1999)        1.0
#[3706 rows x 2 columns]
 
#<영화 평점 best5>
#                                 title  mean_rate
#0  Gate of Heavenly Peace, The (1995)        5.0
#1                        Lured (1947)        5.0
#2                Smashing Time (1967)        5.0
#3            One Little Indian (1973)        5.0
#4              Song of Freedom (1936)        5.0
#--------------------------------------------------------------------




#------------------------각 연령대 영화 추천 5개 (평점 높은순)-------------------------
age_rate = data.pivot_table ( index = 'title', columns = 'age'  , aggfunc = 'mean'
                            ,values ='rate'
                            ,fill_value= 0
                             )
print(age_rate)

age_rate1 = age_rate.sort_values(by = 1 , ascending = False)[1].iloc[:5]

age_rate2 = age_rate.sort_values(by = 18 , ascending = False)[18].iloc[:5]

age_rate3 = age_rate.sort_values(by = 25 , ascending = False)[25].iloc[:5]

age_rate4 = age_rate.sort_values(by = 35 , ascending = False)[35].iloc[:5]

age_rate5 = age_rate.sort_values(by = 45 , ascending = False)[45].iloc[:5]

age_rate6 = age_rate.sort_values(by = 50 , ascending = False)[50].iloc[:5]

age_rate7 = age_rate.sort_values(by = 56 , ascending = False)[56].iloc[:5]

print(age_rate1 , '\n' ,age_rate2, '\n' ,age_rate3, '\n' ,age_rate4, '\n' ,age_rate5, '\n' ,age_rate6, '\n' ,age_rate7) 

#----------출력결과--------------------------------------------------------------------
#title
#Faces (1968)                                        5.0
#Man and a Woman, A (Un Homme et une Femme) (1966)   5.0
#Phantasm II (1988)                                  5.0
#Somewhere in Time (1980)                            5.0
#Phantasm III: Lord of the Dead (1994)               5.0
#Name: 1, dtype: float64 

#18세 미만 영화 추천
#--------------------------------------------------------------------



#-----------------------영화 제목과 개봉년도 분리
#data:전체 데이터
#필요한데이터 제목 개봉년도 평점
movies['release'] = movies['title'].str[-5:-1]
movies['title'] = movies['title'].str[:-6]
print(movies)
#      movieId                         title                         genre release
#0           1                     Toy Story   Animation|Children's|Comedy    1995
#1           2                      Jumanji   Adventure|Children's|Fantasy    1995
#2           3             Grumpier Old Men                 Comedy|Romance    1995
#3           4            Waiting to Exhale                   Comedy|Drama    1995
#4           5  Father of the Bride Part II                         Comedy    1995
#...       ...                           ...                           ...     ...
#3878     3948             Meet the Parents                         Comedy    2000
#3879     3949          Requiem for a Dream                          Drama    2000
#3880     3950                    Tigerland                          Drama    2000
#3881     3951             Two Family House                          Drama    2000
#3882     3952               Contender, The                 Drama|Thriller    2000

#최신 개봉순
movies_rsort = movies.sort_values(by = 'release' , ascending = False)
#최신 개봉순 5개
movies_rsort5 = movies.sort_values(by = 'release' , ascending = False).iloc[:5] 
print(movies_rsort, movies_rsort5)
