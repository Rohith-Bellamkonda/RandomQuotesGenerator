from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('api_show/',views.api_show,name='api_show'),
    path('api_add/',views.api_add,name='api_add'),
    path('api_update/<int:id>',views.api_update,name='api_update'),
    path('api_delete/<int:id>',views.api_delete,name='api_delete'),
]