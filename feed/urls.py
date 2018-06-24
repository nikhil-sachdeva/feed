from django.urls import path, include
from . import views

urlpatterns = [

path('home/', views.index, name='index'),
path('feed/', views.PostView.as_view(),name='feeds'),
path('feed/<int:pk>', views.PostDetailView.as_view(),name='post-detail'),
]
