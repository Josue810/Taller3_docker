from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.add_user, name='add_user'),  # Cambiado para coincidir con la ruta '/user' en la API Flask
    path('user/delete/<int:id>/', views.delete_user, name='delete_user'),
    path('user/<int:id>/', views.edit_user, name='edit_user'),  # Cambiado para coincidir con la ruta '/user/<id>' en la API Flask
]
