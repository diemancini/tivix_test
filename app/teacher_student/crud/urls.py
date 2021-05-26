from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('teachers/list', views.list_teachers, name='list'),
    path('teachers/add', views.add_teachers, name='add'),
    path('teachers/edit', views.edit_teachers, name='edit'),
    path('teachers/delete', views.delete_teachers, name='delete'),
    path('students/list', views.list_students, name='list'),
    path('students/add', views.add_students, name='add'),
    path('students/edit', views.edit_students, name='edit'),
    path('students/delete', views.delete_students, name='delete'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)