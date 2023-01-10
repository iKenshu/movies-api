from rest_framework import serializers

from .models import Movie, Collection


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "synopsis",
            "director",
            "rating",
            "created_by",
            "slug",
        ]


class CollectionSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Movie.objects.all(),
    )

    class Meta:
        model = Collection
        fields = ["id", "name", "is_private", "movies", "user"]
