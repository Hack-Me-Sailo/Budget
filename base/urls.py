from django.urls import path
from base import views
urlpatterns = [
    path('home/',views.Home,name='homee'),
    path('Create-New-Budget',views.create_budget,name='add-title'),
     path('items/<str:name>/<int:pk>/', views.Items, name='items'),
    path('remove-item/<int:pk>/', views.remove_item, name='delete'),
    path('add-Item/',views.add_item,name='add'),
    path('edit-Item/<int:pk>',views.edit_item,name='edit'),
]
