from django.urls import path



from . import views

app_name = 'conversation'

urlpatterns = [
    path('message/<int:product_pk>/', views.new_conversation, name='message'),
   
]