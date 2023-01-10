from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    CreateAPIView,
)

from .models import Movie, Collection
from .serializers import MovieSerializer, CollectionSerializer


class MovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CollectionList(ListAPIView):
    queryset = Collection.objects.filter(is_private=False)
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]


class MyCollectionList(ListAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Collection.objects.filter(user=user)
        return queryset


class MyPrivateCollectionList(ListAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Collection.objects.filter(user=user, is_private=True)
        return queryset


class CollectionCreate(CreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]


class CollectionUpdate(UpdateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]


class CollectionDetail(RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]
