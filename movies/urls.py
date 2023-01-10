from django.contrib import admin
from django.urls import path, include

from .views import (
    MovieList,
    CollectionList,
    MyCollectionList,
    MyPrivateCollectionList,
    CollectionCreate,
    CollectionUpdate,
    CollectionDetail,
)

urlpatterns = [
    path("", MovieList.as_view(), name="movie-list"),
    path(
        "collections/", view=CollectionList.as_view(), name="collection-list"
    ),
    path(
        "my-collections/",
        view=MyCollectionList.as_view(),
        name="my-collection",
    ),
    path(
        "my-collections-private/",
        view=MyPrivateCollectionList.as_view(),
        name="my-collection",
    ),
    path(
        "my-collections/create",
        view=CollectionCreate.as_view(),
        name="collection-list",
    ),
    path(
        "my-collections/<pk>",
        view=CollectionDetail.as_view(),
        name="collection-detail",
    ),
    path(
        "my-collections/<pk>/edit",
        view=CollectionUpdate.as_view(),
        name="collection-edit",
    ),
]
