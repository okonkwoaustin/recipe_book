from django.db import models

# Create your models here.
class Recipe(models.Model):
    TYPE_MAIN_DISH = "M"
    TYPE_APPETIZER = "A"
    TYPE_DESSERT = "D"

    DISH_TYPE = [
        (TYPE_MAIN_DISH, "Main Dish"),
        (TYPE_APPETIZER, "Appetizer"),
        (TYPE_DESSERT, "Dessert"),        
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    servings = models.IntegerField()
    type = models.CharField(max_length=1, choices=DISH_TYPE, default=TYPE_MAIN_DISH)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]