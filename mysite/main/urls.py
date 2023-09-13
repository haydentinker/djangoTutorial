from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path('item/<int:id>',views.v1,name="v1"),
    path('list/<int:id>',views.v2,name="v2")
]