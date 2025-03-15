from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index, name='home'),
    path('register/', views.create_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('book-ticket/ <int:pk>', views.book_ticket, name='book_ticket'),
    path('ticket-details/<int:pk>', views.ticket_details, name='ticket-details'),
    path('Payment/<str:pk>', views.transaction, name='payment'),
    path('agency/<str:pk>', views.agency, name='agency'),
    path('tickets/', views.Bus_page, name='tickets'),
    path('receipt/', views.receipt, name='receipt'),
    path('dashboard/', views.dashboard, name='dashboard')
    
]
