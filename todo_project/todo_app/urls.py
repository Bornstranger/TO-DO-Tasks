from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insert", views.add_item, name="add_item"),
    path('delete/<id>',views.deleteData,name="deleteData"),
    path('update/<id>',views.updateData,name="updateData"),
]
