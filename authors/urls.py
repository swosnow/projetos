from django.urls import path
from . import views

app_name = 'authors'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('login/create/', views.login_create, name='login_create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/recipe/new_recipe/', views.create_recipe, name='new_recipe'),
    path('dashboard/recipe/<int:id/delete/', views.dashboard_recipe_delete, name='dashboard_recipe-delete'),
    path('dashboard/recipe/<int:id/edit/',  views.DashboardRecipe.as_view(), name='dashboard_recipe-edit'),
    
]