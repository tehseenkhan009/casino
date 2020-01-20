from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from django.db.models import Q
from rest_framework import pagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from .serializers import PostSerializer, Post
from ...core.pagination import PostLimitOffsetPagination


class PostListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.filter(Q(status=1)).exclude(Q(category__title='Legal'))

        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('post')
        if query:
            queryset_list = queryset_list.filter(Q(slug=query))

        return queryset_list.order_by('-id')
