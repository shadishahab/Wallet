from django.urls import path
from .views import CreditSubtractionCreateAPIView

urlpatterns = [
    path('create/', CreditSubtractionCreateAPIView.as_view(), name='creditsubtraction-create')
]