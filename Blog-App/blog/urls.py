from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='posts'),
    path('post/create',views.create_post,name='post-create'),
    path('about/',views.about,name='about'),
    path('post/edit/<int:id>',views.edit_form,name='post-edit'),
    path('post/delete/<int:id>',views.delete_post,name='post-delete')
]