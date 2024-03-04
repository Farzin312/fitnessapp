from django.contrib import admin
from .models import UserDietLogEntry, UserDietLog, UserFoodItem 

admin.site.register(UserDietLogEntry)
admin.site.register(UserDietLog)
admin.site.register(UserFoodItem)
