from django.contrib import admin
from django.urls import path, include

from photo.views import PhotoCreate, PhotoDelete, PhotoUpdate, PhotoDetail, PhotoList, PhotoLike, PhotoFavorite, \
    PhotoLikeList, PhotoFavoriteList, PhotoMyList

app_name = 'photo'




urlpatterns = [
    path("mylist/", PhotoMyList.as_view(), name='mylist'),
    path("create/", PhotoCreate.as_view(), name='create'),
    path("like/<int:photo_id>/", PhotoLike.as_view(), name='like'),
    path("favorite/<int:photo_id>/", PhotoFavorite.as_view(), name='favorite'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("delete/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("delete/<int:pk>/", PhotoDetail.as_view(), name='detail'),
    path("", PhotoList.as_view(), name='index'),
    path("like/", PhotoLikeList.as_view(), name='like_list'),
    path("favorite/", PhotoFavoriteList.as_view(), name='favorite_list'),
]

