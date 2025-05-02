from django.contrib import admin
from django.urls import path
from mathapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('powerofincandescentbulb/',views.powerofincandescentbulb,name="powerofincandescentbulb"),
    path('',views.powerofincandescentbulb,name="powerofincandescentbulbroot") 
]