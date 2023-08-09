from django.urls import path
from .views import (AllCreate,DetailUpdateDeleteAPIView)

urlpatterns = [
    path('pk/',DetailUpdateDeleteAPIView.as_view()),
    path('',AllCreate.as_view())
]