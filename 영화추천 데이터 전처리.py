#직무부트캠프 2주차 과제 - 영화 데이터 전처리
import pandas as pd
from pandas import DataFrame,Series

movie_file=open('E:\\코멘토\\2주차\\영화데이터\\movies.dat', encoding='UTF8')
user_file = open('E:\\코멘토\\2주차\\영화데이터\\users.dat', encoding='UTF8')
rating_file = open('E:\\코멘토\\2주차\\영화데이터\\ratings.dat', encoding='UTF8')

#for line in movie_file :
#    print('movieID : \n',line.split('::')[0], end='')

#for line in user_file :
#        print(line, end='')

#for line in rating_file :
#       print(line, end='')

title_list=[]
movieID_list=[]
genre_list=[]

for line in movie_test_file :
    movieID_list.append(int(line.split('::')[0]))
    title_list.append(line.split('::')[1])
    genre_list.append(line.split('::')[2])
   
print('movieID_list=',movieID_list,'\ntitle_list=',title_list,'\ngenre_list=',genre_list)


#user에 관한 데이터
users = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\users.dat', sep = '::', engine = 'python',
                   names = ['userId', 'gender','age','job','zipcode'])
print(users)                   
#movie에 관한 데이터
movies = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\movies.dat', sep = '::', engine = 'python',
                   names = ['movieId', 'title','genre'])
print(movies)      

#rating에 관한 데이터
ratings = pd.read_csv('E:\\코멘토\\2주차\\영화데이터\\ratings.dat', sep = '::', engine = 'python',
                   names = ['userId', 'movieId','rate','timestamp'])
print(ratings)      

#3개의 데이터 합치기
data = pd.merge(movies,ratings,on='movieId')
data = pd.merge(data,users,on='userId')
print(data)
#최신영화순으로 출력하기

data.pivot_table(index = 'title', aggfunc = 'mean', values = 'rate').sort_values(by = 'rate', ascending = False)

#평점 가장 높은 영화 5개 출력하기


