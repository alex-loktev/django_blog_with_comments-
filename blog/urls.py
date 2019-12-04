from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view(), name = 'PostList'),
    path('tags/', TagsList.as_view(), name = 'TagsList'),
    path('tags/detail/<int:pk>/', TagsDetail.as_view(), name = 'TagDetail'),
    path('posts/detail/<int:pk>/', PostDetail.as_view(), name = 'PostDetail')

]
