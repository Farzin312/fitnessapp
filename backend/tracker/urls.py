from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from happiness import views as happiness_views
from sleep import views as sleep_views
from steps import views as steps_views
from weight import views as weight_views
from streak import views as streak_views 
from level import views as level_views
from users import views as user_views

router = DefaultRouter()
router.register(r'happiness', happiness_views.UserHappinessLogViewSet)
router.register(r'sleep', sleep_views.UserSleepViewSet)
router.register(r'steps', steps_views.UserStepsViewSet)
router.register(r'weight', weight_views.UserWeightViewSet)
router.register(r'streak', streak_views.UserStreakViewSet)
router.register(r'level', level_views.UserLevelViewSet)
router.register(r'userprofiles', user_views.UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
