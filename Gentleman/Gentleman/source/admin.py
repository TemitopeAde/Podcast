from django.contrib import admin
from .models import Podcast, FeaturedArticle, TopStories, \
    FeaturedPodcast


class FeatureArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp',)
    prepopulated_fields = {'slug': ('title',)}


class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp',)
    prepopulated_fields = {'slug': ('title',)}


class FeaturedPodcastdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp',)
    prepopulated_fields = {'slug': ('title',)}


class TopstoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(FeaturedArticle, FeatureArticleAdmin)
admin.site.register(TopStories, TopstoriesAdmin)
admin.site.register(FeaturedPodcast, FeaturedPodcastdmin)
admin.site.register(Podcast, PodcastAdmin)



