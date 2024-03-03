from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from happiness import views as happiness_views
from sleep import views as sleep_views
from steps import views as steps_views

router = DefaultRouter()
router.register(r'happiness', happiness_views.UserHappinessLogViewSet)
router.register(r'sleep', sleep_views.UserSleepViewSet)
router.register(r'steps', steps_views.UserStepsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls))
]
