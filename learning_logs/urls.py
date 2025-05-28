from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all topics
    path('topics/', views.topics, name='topics'),
    # Show a single topic and all its entries
    path('topics/<int:topic_id>/', views.topic, name='topic'),

]
