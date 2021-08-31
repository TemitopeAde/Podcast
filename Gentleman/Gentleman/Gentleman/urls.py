from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from source.views import index, podcast, podcastdetails, postdetails, \
    topstories, featuredetails, featuredPodcast

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('podcast/', podcast, name='podcast'),
    path('podcast/<slug>/', podcastdetails, name='podcast_details'),
    path('topstories/<slug>/', postdetails, name='post-details'),
    path('topstories/', topstories, name='topstories'),
    path('featured/<slug>/', featuredetails, name='featured-details'),
    path('newsletter/', include('newsletter.urls')),
    path('featured-podcast/<slug>/', featuredPodcast,  name="featured-podcast_details")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
