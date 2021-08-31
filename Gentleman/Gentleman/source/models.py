from django.db import models
from django.urls import reverse
from PIL import Image


class Podcast(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, default='test.jpg')
    audio_div = models.CharField(max_length=200, null=True)
    script = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('podcast_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.save(self.image.path, quality=50, optimize=True)

    def __str__(self):
        return self.title


class FeaturedArticle(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, default='test.jpg')
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('featured-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.save(self.image.path, quality=50, optimize=True)

    def __str__(self):
        return self.title


class TopStories(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, default='test.jpg')
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.save(self.image.path, quality=50, optimize=True)

    def __str__(self):
        return self.title


class FeaturedPodcast(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, default='test.jpg')
    audio_div = models.CharField(max_length=200, null=True)
    script = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        return reverse('featured-podcast_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.save(self.image.path, quality=50, optimize=True)

    def __str__(self):
        return self.title