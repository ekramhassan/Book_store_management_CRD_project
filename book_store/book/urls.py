from django.urls import path
from book.views import home,  store_book,Show_book,edit_book,delete_book


urlpatterns = [
    path('',home),
    path('store_book/', store_book,name='storebook'),
    path('show_book/', Show_book,name='Show_book'),
    path('edit_book/<int:id>/', edit_book,name='edit_book'),
     path('delete_book/<int:id>/', delete_book,name='delete_book'),
]