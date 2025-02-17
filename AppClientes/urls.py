from django.urls import path
from . import views

app_name = 'AppClientes'

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='list'),
    path('cliente/detalle/<int:pk>/', views.ClienteDetalle.as_view(), name='detalle'),
        # <int:pk> es importante
    path('cliente/update/<int:pk>/', views.ClienteUpdateView.as_view(), name='update'),
     
    path('cliente/eliminar/<int:pk>/', views.ClienteDeleteView.as_view(), name='delete'),
    path('cliente/create/', views.ClienteCreateView.as_view(), name='create'), 
]


