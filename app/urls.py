from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.myModel.as_view(),name='home'),
    path('user/signin/',views.send_data_to_DataBase,name='signin')
]