from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from happiness import views as happiness_views

router = DefaultRouter()
router.register(r'happiness', happiness_views.UserHappinessLogViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls))
]
