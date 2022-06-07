from django.urls import path,re_path
from . import views
 
urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name="create"),
    path('retrieve',views.retrieve,name="retrieve"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
   # re_path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
    path(r'^delete_product/?P<pk>[0-9](+)/$', views.delete, name="delete"),
]
