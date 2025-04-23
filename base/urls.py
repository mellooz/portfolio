from django.urls import path
from . import views

app_name='base'

urlpatterns = [
	path('', views.home , name='home'),
    path('contact/', views.contact , name='contact'),

    # projects urls

#   - ai-Workflow
    path('ai-Workflow/', views.aiWorkflow , name='ai-Workflow'),
#   - learn-hub
    path('learn-hub/', views.learnhub , name='learn-hub'),
#   - job-boards
    path('job-boards/', views.jobboards , name='job-boards'),
#   - cars-marketplace
    path('cars-marketplace/', views.carsmarketplace , name='cars-marketplace'),
#   - chat-app
    path('chat-app/', views.chatapp , name='chat-app'),
#   - e-commerce
    path('e-commerce/', views.ecommerce , name='e-commerce'),
#   - mario 
    path('mario/', views.mario , name='mario'),
#   - networks
    path('networks/', views.networks , name='networks'),
]