from django.shortcuts import render

from . models import Recipe

# Create your views here.
def recipe(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    template = "recipes/index.html"
    return render(request, template, context)