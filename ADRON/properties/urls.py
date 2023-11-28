from django.urls import path
from .views import NewHomePage, DetailPage

urlpatterns = [
    path('', NewHomePage.as_view(), name='home-page'),
    path('<str:id>/', DetailPage.as_view(), name='detail-page')

]