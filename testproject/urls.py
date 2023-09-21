

from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('reg/', views.reg_user, name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_note/', views.add_note, name='add_note'),
    path('notes/', views.notes, name='notes'),
    path('', views.base, name='base'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('note/<int:pk>/', views.note, name='note'),
    path('edit_note/<int:pk>/', views.edit_note, name='edit_note'),
    path('delete_note/<int:pk>/', views.delete_note, name='delete_note'),
]
