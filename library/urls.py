from django.urls import path
from library.views import landing_view, book_view

urlpatterns = [
    path('', landing_view, name='library'),
    path('books/', book_view, name='books'),
]