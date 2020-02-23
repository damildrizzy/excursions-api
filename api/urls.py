from django.urls import path
from . import views
from .views import ExcursionList, ExcursionDetail
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', ExcursionList.as_view()),
    path('api/<int:pk>/', ExcursionDetail.as_view()),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]