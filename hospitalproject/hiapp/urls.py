from . import views
from django.urls import path, include
app_name = 'hiapp'
urlpatterns = [
    path('AddBBrand/', views.addbrand, name='addbrand'),
path('add_brand', views.add_brand, name='add_brand'),
     path('delete_brand/<int:brandid>/', views.delete_brand, name='delete_brand'),
    path('edit_brand/<int:brandid>/', views.edit_brand, name='edit_brand'),
    path('update_brand/<int:brandid>/', views.update_brand, name='update_brand'),
    path('AddCategory/', views.addcategory, name='addcategory'),
    path('add_category', views.add_category, name='add_category'),
    path('delete_category/<int:categoryid>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:categoryid>/', views.edit_category, name='edit_category'),
    path('update_category/<int:categoryid>/', views.update_category, name='update_category'),
    path('AddItem/', views.additem, name='additem'),
    path('add_item', views.add_item, name='add_item'),
    path('delete_item/<int:itemid>/', views.delete_item, name='delete_item'),
    path('edit_item/<int:itemid>/', views.edit_item, name='edit_item'),
    path('update_item/<int:itemid>/', views.update_item, name='update_item'),
                ]