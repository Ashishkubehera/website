from . import views
from django.urls import path



urlpatterns = [
    # music/
    path('', views.index, name='index'),
    # music/712
    path('<int:album_id>/',views.details, name='detail'),
]
