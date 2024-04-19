from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    # Function Based Views
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_detail, name='movie-detail'),

    # Class Based Views
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
]
