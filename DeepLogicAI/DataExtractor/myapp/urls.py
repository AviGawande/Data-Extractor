from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.myapp, name='home'),
    path('images/', views.images, name='images'),
    path('documents/', views.documents, name='documents'),
    path('download-csv/', views.generate_csv_from_image, name='download_csv'),
]
