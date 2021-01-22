from django.urls import path
from . import views
urlpatterns = [
path('dm1',views.fnDemo1),
path('fnhrk',views.fnh),
path('form',views.form),
path('reg',views.regform),
]
