from django.urls import path
from . import views
app_name="cookieapp"
urlpatterns=[
    path('',views.input,name='input'),
    path('add',views.add,name='add'),
    path('display',views.display,name='display'),
]