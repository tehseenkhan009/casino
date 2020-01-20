from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.translation import pgettext_lazy


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_hidden = models.BooleanField(blank=True, choices=[(False, 'No'), (True, 'Yes')], default=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_category', default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.FileField(
        upload_to='posts',
        null=True,
        blank=True
    )
    updated_on = models.DateTimeField(auto_now= True)
    content = HTMLField(
        pgettext_lazy('Casino Description', 'description'),
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

