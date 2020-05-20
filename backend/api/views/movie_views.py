# from rest_framework import status
# from rest_framework.decorators import api_view
# from api.models import Movie
# from api.serializers import MovieSerializer
# from rest_framework.response import Response


# @api_view(['GET', 'POST', 'DELETE'])
# def movies(request):

#     if request.method == 'GET':
#         id = request.GET.get('id', request.GET.get('movie_id', None))
#         title = request.GET.get('title', None)
#         genres = request.GET.get('genres', None)

#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'POST':
#         movies = request.data.get('movies', None)
#         print(movies)
#         for movie in movies:
#             id = movie.get('id', None)
#             title = movie.get('title', None)
#             genres = movie.get('genres', None)

#             Movie(id=id, title=title, genres='|'.join(genres)).save()
#         print(Movie)
#         return Response(status=status.HTTP_200_OK)
