from django.urls import path
from.import views


urlpatterns = [
    path('bv/', views.bookView, name='book_url'),
    path('bs/', views.showbookView, name='showbook_url'),
    path('db/<int:id>/', views.deletebookView, name='deletebook_url'),
    path('ub/<int:id>/', views.updatebookView, name='updatebook_url')
]