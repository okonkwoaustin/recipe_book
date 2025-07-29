from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

# Create your views here.


def recipe(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    template = "recipes/index.html"
    return render(request, template, context)


def success(request):
    return render(request, "recipes/success.html")


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect("success")
    else:
        form = RecipeForm()
        template = "recipes/create_recipe.html"
        context = {"form": form}
        return render(request, template, context)


def recipe_detail(request, recipe_id):
    """Detail view for a recipe"""
    recipe = Recipe.objects.get(id=recipe_id)
    context = {"recipe": recipe}
    template = "recipes/recipe_detail.html"
    return render(request, template, context)


def update_recipe(request, pk):
    """Update view for a recipe"""
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe-detail", recipe_id=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
        template = "recipes/update_recipe.html"
        context = {"form": form}
    return render(request, template, context)


def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("index")
    template = "recipes/delete_recipe.html"
    context = {"recipe": recipe}
    return render(request, template, context)
