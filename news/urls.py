from django.urls import path
from . import views

urlpatterns = [
    path('news_list/', views.NewsListView.as_view()),
    path('news_list/<int:id>/', views.NewsDetailView.as_view()),
    path('news_list/<int:id>/delete/', views.NewsDeleteView.as_view()),
    path('news_list/<int:id>/update/', views.NewsUpdateView.as_view()),
    path('create_news/', views.NewsCreateView.as_view())
]