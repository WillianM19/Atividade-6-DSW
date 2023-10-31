from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createDisc', views.createDisc, name='createDisc'),
    path('editDisc/<int:id>', views.editDisc, name='editDisc'),
    path('deleteDisc/<int:id>', views.deleteDisc, name='deleteDisc'),
    path('showDisc/<int:id>', views.showDisc, name='showDisc'),
]
