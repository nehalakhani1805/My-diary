from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.userdiary,name='home'),
    path('userdiary/',views.userdiary,name='userdiary'),
    #path('userdiary/',views.EntryListView.as_view(),name='userdiary'),
    path('userdiary/<int:pk>/',views.EntryDetailView.as_view(),name='detail'),
    path('userdiary/<int:pk>/new',views.EntryCreateView.as_view(),name='create'),
    path('userdiary/<int:pk>/update',views.EntryUpdateView.as_view(),name='update'),
    path('userdiary/<int:pk>/delete',views.EntryDeleteView.as_view(),name='delete'),
]