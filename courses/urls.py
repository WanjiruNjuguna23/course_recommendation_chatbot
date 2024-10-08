# urls.py

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.select_interests, name='select_interests'), 
    path('select-interests/', views.select_interests, name='select_interests'),  # URL to select interests
    path('recommend-courses/', views.recommend_courses, name='recommend_courses'),  # URL to display course recommendations
]

# courses/urls.py

#urlpatterns = [
    #path('', views.select_interests, name='select_interests'),  # Root URL maps to select_interests view
    #path('recommend-courses/', views.recommend_courses, name='recommend_courses'),
#]
