from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('teachers/list', views.list_teachers, name='teachers_list'),
    path('teachers/add', views.add_teachers, name='teachers_add'),
    path('teachers/edit/<int:pk>', views.edit_teachers, name='teachers_edit'),
    path('teachers/delete/<int:pk>', views.delete_teachers, name='teachers_delete'),
    path('students/list', views.list_students, name='students_list'),
    path('students/add', views.add_students, name='students_add'),
    path('students/edit/<int:pk>', views.edit_students, name='students_edit'),
    path('students/delete/<int:pk>', views.delete_students, name='students_delete'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
