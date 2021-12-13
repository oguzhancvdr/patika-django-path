from django.urls import path
from . import views

urlpatterns = [
    path('',views.courses, name='courses'),    
    path('<slug:category_slug>/<int:course_id>',views.course_detail, name='course_detail'),    
    path('categories/<slug:category_slug>',views.courses, name='courses_by_category'),    
    path('tags/<slug:tag_slug>',views.courses, name='courses_by_tag'),    
    path('search/',views.search, name='search'),    
]