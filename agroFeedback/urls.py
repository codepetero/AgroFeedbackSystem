from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_feedback/', views.create_feedback, name='create_feedback'),
    path('update_profile', views.updateProfile, name='update_profile'),
    path('feedback-history/<id>', views.feedback_history, name='history'),
    path('delete_history/<id>', views.delete_history, name='delete_history'),
    path('edit_history/<id>', views.edit_history, name='edit_history'),
    path('search/',views.search, name='search'),
    path('feedback_reply/', views.feedback_reply, name='feedback_reply'),
    path('contact_us/', views.contact_us, name='contact_us'),
]