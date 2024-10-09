from django.urls import path
from .views import *


urlpatterns = [
    path('',ProductViewSet.as_view({'get':'list'})),
    path('<int:id>/',ProductViewSet.as_view({'get':'retrieve'})),
    path('create/',ProductViewSet.as_view({'post':'create'})),
    path('update/<int:id>/',ProductViewSet.as_view({'put':'update'})),
    path('delete/<int:id>/',ProductViewSet.as_view({'delete':'destroy'})),
    
    #category 
    path('category/',CategoryViewSet.as_view({'get':'list'})),
    path('category/<int:id>/',CategoryViewSet.as_view({'get':'retrieve'})),
    path('category/create/',CategoryViewSet.as_view({'post':'create'})),
    path('category/update/<int:id>/',CategoryViewSet.as_view({'put':'update'})),
    path('category/delete/<int:id>/',CategoryViewSet.as_view({'delete':'destroy'})),
]

