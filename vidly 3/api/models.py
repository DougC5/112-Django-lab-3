from django.db import models
from tastypie.resources import ModelResource, ALL
from tastypie.authentication import BasicAuthentication
from movies.models import Movie, Genre

class MovieResource(ModelResource):
    class Meta:
        resource_name = 'movies'
        queryset = Movie.objects.all()
        #excludes = ['price']
        filtering = {'price': ALL, 'stock': ALL}
        authentication = BasicAuthentication()

class GenreResource(ModelResource):
    class Meta:
        resource_name = 'genre'
        queryset = Genre.objects.all()
        #excludes = ['price']
        filtering = {'price': ALL, 'stock': ALL}
        authentication = BasicAuthentication()