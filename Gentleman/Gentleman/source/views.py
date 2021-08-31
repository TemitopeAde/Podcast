from django.shortcuts import render
from .models import FeaturedArticle, TopStories, Podcast, FeaturedPodcast
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404


def index(request):
    featured = FeaturedArticle.objects.all()[:3]
    featured_podcast = FeaturedPodcast.objects.all()[:1]
    topstories = TopStories.objects.all().order_by('-timestamp')
    paginated_topstories = paginate_top(request, topstories)
    context = {
        'featured': featured,
        'featured_podcast': featured_podcast,
        'topstories': paginated_topstories
    }
    return render(request, 'index.html', context)


def featuredPodcast(request, slug):
    podcast = get_object_or_404(FeaturedPodcast, slug=slug)
    context = {
        'podcast': podcast
    }
    return render(request, 'featured-podcast.html', context)


def paginate_top(request, topstories):
    object_list = topstories
    paginator = Paginator(object_list, 30)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return  post_list


def podcast(request):
    podcast = Podcast.objects.all().order_by('-timestamp')
    paginated_podcast = paginate_podcast(request, podcast)
    context = {
        'podcast': paginated_podcast
    }
    return render(request, 'podcast.html', context)


def paginate_podcast(request, podcast):
    object_list = podcast
    paginator = Paginator(object_list, 21)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return  post_list


def podcastdetails(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    featured = FeaturedArticle.objects.all()[:3]
    context = {
        'podcast': podcast,
        'featured': featured,
    }
    return render(request, 'single-podcast.html', context)


def postdetails(request, slug):
    post = get_object_or_404(TopStories, slug=slug)
    featured = FeaturedArticle.objects.all()[:3]
    latest = Podcast.objects.all()[:6]
    context = {
        'post': post,
        'featured': featured,
        'latest': latest
    }
    return render(request, 'single-post.html', context)


def topstories(request):
    stories = TopStories.objects.all()
    pag_stories = paginate_topstories(request, stories)
    context = {
        'stories': pag_stories
    }
    return render(request, 'top-stories.html', context)


def paginate_topstories(request, stories):
    object_list = stories
    paginator = Paginator(object_list, 21)
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return  post_list


def featuredetails(request, slug):
    featured = get_object_or_404(FeaturedArticle, slug=slug)
    context = {
        'post': featured,
    }
    return render(request, 'single-featured.html', context)
