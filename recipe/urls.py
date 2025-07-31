from django.urls import path

from . import views

urlpatterns = [
    path("", views.recipe, name="index"),
    path("create_recipe/", views.create_recipe, name="create_recipe"),
    path("success", views.success, name="success"),
    path("recipes/<int:recipe_id>/", views.recipe_detail, name="recipe-detail"),
    path("recipes/<int:pk>/edit/", views.update_recipe, name="update-recipe"),
    path("recipes/<int:pk>/delete/", views.delete_recipe, name="delete-recipe"),
    path("my_recipes/", views.my_recipes, name="my-recipes")
]
