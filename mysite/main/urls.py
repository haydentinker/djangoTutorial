from django.urls import path
from . import views

urlpatterns=[
    path("<int:id>", views.home, name="home"),
    path('item/<int:id>',views.v1,name="v1"),
    path('list/<int:id>',views.v2,name="v2"),
    path('viewlist/<int:id>',views.viewList,name="viewList"),
    path('create/',views.create,name="create"),
    path('view/',views.view,name='view')
]