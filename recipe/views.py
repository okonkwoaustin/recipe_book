from django.shortcuts import render, redirect
from . models import Recipe
from . forms import RecipeForm

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
        form = RecipeForm(data=request.POST)
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
    context = {
        "recipe": recipe
    }
    template = "recipes/recipe_detail.html"
    return render(request, template, context)
