from django.urls import include, path
from rest_framework import routers
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = routers.DefaultRouter()
router.register(r'blog', views.BlogViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-auth/', TokenObtainPairView.as_view()),
    # path('api/token/refresh', TokenRefreshView.as_view()),
]
