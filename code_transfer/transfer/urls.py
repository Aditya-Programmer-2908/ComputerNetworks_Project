from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('retrieve/', views.retrieve_file, name='retrieve_file'),
    path('sender/', views.sender, name='sender'),
    #path('paste_clipboard/', views.paste_clipboard, name='paste_clipboard'),
    path('retrieve_file/', views.retrieve_file, name='retrieve_file'),
    path('retrieve_clipboard/', views.retrieve_clipboard, name='retrieve_clipboard'),
    path('receiver_options/', views.receiver_options, name='receiver_options'),
    path('upload_clipboard/',views.upload_clipboard,name="upload_clipboard"),
]
