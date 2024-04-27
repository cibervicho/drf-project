from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail

urlpatterns = [
    # Function Based Views
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_detail, name='movie-detail'),

    # Class Based Views
    path('list/', WatchListAV.as_view(), name='watchlist-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]
