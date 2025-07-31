from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Recipe
from .forms import RecipeForm

# Create your views here.


def recipe(request):
    """List all the recipes"""
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    template = "recipes/index.html"
    return render(request, template, context)

@login_required
def success(request):
    return render(request, "recipes/success.html")

@login_required
def create_recipe(request):
    """Create a recipe"""
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
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

@login_required
def update_recipe(request, pk):
    """Update view for a recipe"""
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe-detail", recipe_id=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    template = "recipes/update_recipe.html"
    context = {"form": form}
    return render(request, template, context)

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("index")
    template = "recipes/delete_recipe.html"
    context = {"recipe": recipe}
    return render(request, template, context)

@login_required
def my_recipes(request):
    """Display recipes created by the logged-in user, with pagination"""
    recipe_list = Recipe.objects.filter(user=request.user).order_by("-created_at")
    paginator = Paginator(recipe_list, 5)  # Show 5 recipes per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "recipes/my_recipes.html", {"page_obj": page_obj})