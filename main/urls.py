from django.urls import path
from .views import *

app_name = "main"
urlpatterns =[
    path('', showmain, name="showmain"),
    path('adult/',adult, name="adult"),
    path('teenager/',teenager, name="teenager"),
    path('childhood/',childhood, name="childhood"),
    path('<int:id>/',detail, name="detail"),
    path('new/',new, name="new"),
    path('create/',create, name="create"),
    path('posts/',posts, name="posts"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>',update,name="update"),
    path('delete/<str:id>',delete, name="delete"),
]
