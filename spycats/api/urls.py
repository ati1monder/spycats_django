from django.urls import path
from .views import MissionAPIView, CatAPIView, UpdateTargetView

urlpatterns = [
    path('cats/', CatAPIView.as_view(), name='cat_manipulation'),
    path('cats/<int:pk>/', CatAPIView.as_view(), name='cat_detail'),
    path('missions/', MissionAPIView.as_view(), name='mission_manipulation'),
    path('missions/<int:pk>/', MissionAPIView.as_view(), name='mission_detail'),
    path('missions/<int:mission_id>/targets/<int:target_id>/', UpdateTargetView.as_view(), name='update_target'),
]