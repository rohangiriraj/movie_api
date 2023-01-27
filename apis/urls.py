from django.urls import path, include
from . import views
#from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('movies/',views.MovieList.as_view(), name='movie_list'),
    #path('register/',jwt_views.TokenObtainPairView.as_view(), name='register'),
    path('register/',views.Register.as_view(),name='register'),
    path('collection/', views.CollectionsView.as_view(),name='collections'),
    path('collection/<uuid:uuid>/', views.CollectionView.as_view(),name='collection'),
    path('request-count/', views.RequestCountView.as_view(),name='request_counter'),
    path('request-count/reset/', views.RequestCountResetView.as_view(),name='request-reset'),
    ]