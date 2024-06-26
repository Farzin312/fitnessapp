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
from .views import UserAggregateView

router = DefaultRouter()
router.register(r'happiness', happiness_views.UserHappinessLogViewSet)
router.register(r'sleep', sleep_views.UserSleepViewSet)
router.register(r'steps', steps_views.UserStepsViewSet)
router.register(r'weight', weight_views.UserWeightViewSet)
router.register(r'streak', streak_views.UserStreakViewSet)
router.register(r'level', level_views.UserLevelViewSet)
router.register(r'userworkouts', workout_views.UserWorkoutViewSet)
router.register(r'diet', diet_views.UserDietLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-aggregate/', UserAggregateView.as_view(), name='user_aggregate'),
    path('api/', include(router.urls)),
    path('login/', user_views.LoginAPIView.as_view(), name='login'),
    path('token-auth/', obtain_auth_token, name='token_auth'), 
    path('userprofiles/', user_views.UserProfileViewSet.as_view({'post': 'create', 'get': 'list'}), name='userprofiles'),
    path('userprofiles/<int:pk>/', user_views.UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}), name='userprofile_detail'),
    path('password-reset/', user_views.password_reset_request, name='password_reset'),
    path('password/confirm/<int:user_id>/<str:token>/', user_views.password_reset_confirm, name='password_reset_confirm'), 
]