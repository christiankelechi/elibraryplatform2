from django.urls import path
from . import views
from .views import captureindex, detect, trainer, create_dataset
from .views import capture_face, login_with_face

app_name='core_app_root'
urlpatterns=[
    path('',views.index,name='index'),
    path('image/', captureindex),
    path('image/createdataset', create_dataset,name='createdataset'),
    path('image/detect', detect,name='detect'),
    path('image/train', trainer,name='train'),
    path('capture_face/', capture_face, name='capture_face'),
    path('login_with_face/', login_with_face, name='login_with_face'),
]