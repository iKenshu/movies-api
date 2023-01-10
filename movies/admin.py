from django.contrib import admin

from .models import Movie, Collection


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass
