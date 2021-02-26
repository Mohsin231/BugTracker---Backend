from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('bugs/', views.BugList.as_view(), name='bug_list'),
    path('bugs/<int:pk>', views.BugDetail.as_view(), name='bug_detail'),
]