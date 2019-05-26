from django.urls import path

from .views import (
    NewsList,
    NewsDetail,
    DraftsList
)

urlpatterns = [
    path('',NewsList.as_view(),name='news_list'),
    path('drafts/',DraftsList.as_view(),name='draft_news_list'),
    path('<int:pk>',NewsDetail.as_view(),name='news_detail'),
]