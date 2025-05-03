from django.urls import path
from . import views

app_name = "monsite"

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('clients/', views.clients, name='clients'),
    path('blog/', views.blog, name='blog'),
    path('offre/<str:offre>/', views.offer_detail, name='offer_detail'),
    path('contact/<str:offre>/', views.contact_form, name='contact_form'),
    path('messages/', views.messages_list, name='messages_list'),
    path('download_program/', views.download_program, name='download_program'),
]