from django.contrib import admin
from django.urls import path
from myapp1 import views

urlpatterns = [
    path ('contacts/',views.contacts,name='contacts'),
    path ('add_newmember/',views.add_newmember,name= 'add_newmember'),
    path ('sample1/',views.sample1,name='sample1'),
    path('all_member/',views.all_member,name='all_member'),
    path('all_member/detail/<int:id>', views.detail,name ='detail'),
    path('all_member/detail/update/<int:id>/',views.update,name='update'),
    path('all_member/detail/delete/<int:id>/',views.delete,name='delete')
    ]
