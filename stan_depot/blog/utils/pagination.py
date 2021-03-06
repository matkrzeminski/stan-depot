from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 6
    page_query_param = "page_size"
    max_page_size = 100
