from django.urls import path
from . import views


app_name = 'food'
'''
this is done in namespacing so u dont have to
worry about muliple apps having same name for paths
'''

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('item/', views.item, name='item'),
    path('<int:pk>/',views.FoodDetail.as_view(), name='detail'),
    # path('add/',views.create_item, name='create_item'),
    path('add/',views.CreateItem.as_view(), name='create_item'),
    #edit item
    path('update/<int:id>', views.update_item, name='update_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item')
]