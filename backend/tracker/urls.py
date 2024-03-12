from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from happiness import views as happiness_views
from sleep import views as sleep_views
from steps import views as steps_views
from weight import views as weight_views
from streak import views as streak_views 
from level import views as level_views
from users import views as user_views
from workout import views as workout_views
from diet import views as diet_views
from . import views

router = DefaultRouter()
router.register(r'happiness', happiness_views.UserHappinessLogViewSet)
router.register(r'sleep', sleep_views.UserSleepViewSet)
router.register(r'steps', steps_views.UserStepsViewSet)
router.register(r'weight', weight_views.UserWeightViewSet)
router.register(r'streak', streak_views.UserStreakViewSet)
router.register(r'level', level_views.UserLevelViewSet)
router.register(r'userprofiles', user_views.UserProfileViewSet, basename='userprofile')
router.register(r'userworkouts', workout_views.UserWorkoutViewSet)
router.register(r'diet', diet_views.UserDietLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
    path('password-reset-confirm/<int:user_id>/<str:token>/', views.password_reset_confirm, name='password_reset_confirm')
]
