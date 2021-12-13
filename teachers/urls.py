from django.urls import path
from .views import TeachersView, TeacherDetailView

urlpatterns = [
    path('', TeachersView.as_view(), name='teachers'),    
    path('teacher/<int:pk>',TeacherDetailView.as_view(), name='teacher_detail'),    
    # path('categories/<slug:category_slug>',views.category_list, name='courses_by_category'),    
    # path('tags/<slug:tag_slug>',views.tag_list, name='courses_by_tag'),    
]