from django.urls import path
from .views import new_conversation



from . import views


app_name = 'conversation'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('', views.inbox, name='inbox'),
    path('message/<int:product_id>/', new_conversation, name='new_conversation'),
   
   
]