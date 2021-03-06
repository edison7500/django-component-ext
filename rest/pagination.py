from rest_framework import pagination
from rest_framework.settings import api_settings


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = api_settings.PAGE_SIZE
    page_size_query_param = 'size'
    max_page_size = 1000


class BiggerResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    max_page_size = 1000
