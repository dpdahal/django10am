from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    re_path(r'^news/(?P<criteria>[0-9]+)/$', views.education),
    path('users', include([
        path('', views.users),
        path('/<int:id>', views.user_detail),
    ]

    ))

]
