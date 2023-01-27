from rest_framework import serializers
from rest_framework.response import Response
from .models import Collections
from django.contrib.auth.models import User
from collections import Counter

#https://www.geeksforgeeks.org/python-program-to-find-the-highest-3-values-in-a-dictionary/


class Registration(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
    
    def create(self, user_data):
        user_details = User.objects.create_user(username = user_data['username'], password = user_data['password'])
        return user_details

class POSTCollections(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('uuid','title','description','movies')
    
    def create(self, data):
        title = data['title']
        description = data['description']
        movies = data['movies']
        user = data['user']
        collection = Collections.objects.create(title = title, description = description, movies = movies, user = user)
        return collection

class GETCollections(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('title', 'uuid', 'description')

    def movie_count(self,movies, genre_count):
        for movie in movies:
            genres = movie['genre'].split(',')
            for genre in genres:
                if genre not in genre_count:
                    genre_count[genre] = 1
                else:
                    genre_count[genre] += 1
        return genre_count
                

    def get_collection(self, data):
        cols = []
        genre_count = {}
        for value in data:
            title = value.title
            description = value.description
            uuid = value.uuid
            movies = value.movies
            cols.append({'title':title, 'uuid': uuid, 'description':description})
            genre_count = self.movie_count(movies, genre_count)
        
        fav3_genres = Counter(genre_count).most_common(3)
        fav_genres = str(fav3_genres[0][0]+', '+fav3_genres[1][0]+', '+fav3_genres[2][0])
        return Response({'is_success':True, 'data':{'collections':cols},'favourite_genres':fav_genres})


class PUTCollection(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('title','description','movies')
    
    def update(self, first_val, data):
        if 'title' in data:
            first_val.title = data['title']
        if 'description' in data:
            first_val.description = data['description']
        if 'movies' in data:
            first_val.movies = data['movies']
        first_val.save()
        return Response({'is_success':True})

class GETCollection(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('title', 'description', 'movies')
    def get_collection(first_val):
        title = first_val.title
        description = first_val.description
        movies = first_val.movies
        return Response({'title':title, 'description':description, 'movies':movies})

class RequestCountSerializer(serializers.Serializer): # Unused but still here, in case I need it somewhere else
    request_count = serializers.IntegerField()
