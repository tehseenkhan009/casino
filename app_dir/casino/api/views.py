from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)
from django.db.models import Q
from rest_framework import pagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny)
from .serializers import CasinoSerializer, Casino, DealsSerializer, Deals, Country, CountryUrl
from ...core.pagination import PostLimitOffsetPagination
from django.contrib.gis.geoip2 import GeoIP2
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import HttpResponse


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_client_country(request):
    ip = get_client_ip(request)
    g = GeoIP2()
    try:
        country_info = g.country(ip)
    except:
        country_info = 0

    return country_info


class CasinoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CasinoSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Casino.objects.filter(is_disabled=False)

        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 12

        query = self.request.GET.get('slug')
        if query:
            queryset_list = queryset_list.filter(Q(slug=query))

        sort = self.request.GET.get('sort')
        if sort == 'recommended':
            queryset_list = queryset_list.filter(is_recommended=True)

        return queryset_list.order_by('order_id')


class DealsListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DealsSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        country = get_client_country(self.request)
        try:
            client_country = country['country_code']
        except:
            client_country = 0
        filters = Q(url_country=None)
        country_id = 243
        if client_country is not 0:
            country_id = Country.objects.get(code=client_country)
            filters = (~Q(url_country__country_id=country_id) | Q(url_country=None))

        queryset_list = Deals.objects.prefetch_related(
            Prefetch('url_country', queryset=CountryUrl.objects.filter(country_id=country_id))). \
            filter(filters & Q(is_disabled=False))

        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10

        queryset_list.order_by('order_id')

        sort = self.request.GET.get('sort')
        if sort == 'spins':
            queryset_list = queryset_list.order_by('-free_spins')
        if sort == 'bonus':
            queryset_list = queryset_list.order_by('-bonus__price')
        if sort == 'percent':
            queryset_list = queryset_list.order_by('-bonus__percent')
        if sort == 'newest':
            queryset_list = queryset_list.order_by('-created_at')

        return queryset_list


class DealActions(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = DealsSerializer
    lookup_field = 'id'

    def get_object(self):
        print(self.kwargs)
        return

    def put(self, request, *args, **kwargs):

        deal_id = self.request.GET.get('id')
        deal = get_object_or_404(Deals, id=deal_id)
        deal.counter = F('counter') + 1
        deal.save()

        return HttpResponse('Hello')