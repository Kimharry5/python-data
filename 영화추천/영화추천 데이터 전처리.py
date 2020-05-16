#직무부트캠프 2주차 과제 - 영화 데이터 전처리
import pandas as pd
from pandas import DataFrame as df
from pandas import Series 

movie_file=open('E:\\코멘토\\2주차\\영화데이터\\movies.dat', encoding='UTF8')
user_file = open('E:\\코멘토\\2주차\\영화데이터\\users.dat', encoding='UTF8')
rating_file = open('E:\\코멘토\\2주차\\영화데이터\\ratings.dat', encoding='UTF8')

'''
for line in movie_test_file :
    movieID_list.append(int(line.split('::')[0]))
    title_list.append(line.split('::')[1])
    genre_list.append(line.split('::')[2])
   
print('movieID_list=',movieID_list,'\ntitle_list=',title_list,'\ngenre_list=',genre_list)
'''

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

#rate값 문자-> 숫자로 변형
#data.astype({'rate':int})
#print(data.dtypes)

#최신영화순으로 출력하기
#movies, title(제목(년도)) 나누기
#print(movies.title)

movies_data = {"movies" : []} 

for s in movie_file.readlines() : #영화 갯수만큼
    [id, title, genre] = s.split('::')
          #제목안에 괄호가 있는 경우....
    title = title[:len(title)-6]                                #영화데이터 추가할시 변경해야함
    movies_data['movies'].append({
        'mId' : id,
        'title' : title,
        'genre' : genre
    })

#print(movies_data)


#평점 가장 높은 영화 5개 출력하기
#unexpected indent -> 들여쓰기 에러
#mrdata = pd.merge(movies,ratings,on='movieId')
#movie_mean = mrdata.groupby('title')['rate'].mean().iloc[:5]
#새로운 열에 mean_rate를 추가해서 데이터,,넣어야 DB에 들어갈수있나?
#print(movie_mean)

#                                                title
#                                                $1,000,000 Duck (1971)           3.027027
#                                                'Night Mother (1986)             3.371429
#                                                'Til There Was You (1997)        2.692308
#                                                'burbs, The (1989)               2.910891
#                                                ...And Justice for All (1979)    3.713568
#                                                Name: rate, dtype: float64

#grp = data.groupby('title') 
  
#print ( grp.agg({'rate' : 'mean'}).iloc[:5] )
#print( type(grp), type(movie_mean))             #<class 'pandas.core.groupby.generic.DataFrameGroupBy'> <class 'pandas.core.series.Series'>
                                                #                                   rate
                                                #title
                                                #$1,000,000 Duck (1971)         3.027027
                                                #'Night Mother (1986)           3.371429
                                                #'Til There Was You (1997)      2.692308
                                                #'burbs, The (1989)             2.910891
                                                #...And Justice for All (1979)  3.713568

best5_movies = data.groupby('title') #영화별로 묶기
data = data.astype({'rate':'int'})
best5_movies = best5_movies['rate'].agg('mean').iloc[:5] #영화별 평점 평균값 구하기
data = pd.merge(data,best5_movies,on='title')
#print(best5_movies)

#높은 평점 순 영화 목록
high_rate = pd.merge(movies,ratings,on='movieId')
#영화별 평점 평균에서 내림차순으로 정렬함
pd.options.display.float_format = '{:.1f}'.format
high_rate = high_rate.groupby('title')

high_rate = high_rate['rate'].agg('mean')
print(high_rate)
#high_rate = high_rate['rate'].agg('mean').sort_values(ascending=False)
#print(high_rate)

best_moives = (pd.pivot_table(data=ratings, index='movieId', values='rate', aggfunc='mean')
            .sort_values(by='rate', ascending=False)
            .rename(columns={'rate' : 'mean_rate'})
               #.head(5)
            )

print(best_moives)
"""
영화별로묶은후 평점 다시 구하기
        mean_rate
movieId
989            5.0
3881           5.0
1830           5.0
3382           5.0
787            5.0
...            ...
826            1.0
3228           1.0
2845           1.0
3209           1.0
142            1.0
"""
