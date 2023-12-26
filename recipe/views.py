from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

def recipe(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        recipes.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
            )
        
        return redirect("recipe")

    queryset = recipes.objects.all()
    if request.GET.get("Search"):
         queryset = queryset.filter(recipe_name__icontains = request.GET.get("Search"))
         
    context = {"recipes" : queryset}
    return render(request, "recipes.html", context)

def delete_recipe(request,id):
        queryset = recipes.objects.get(id = id)
        queryset.delete()
        return redirect("recipe")

def update_recipe(request,id):
    queryset = recipes.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
             queryset.recipe_image = recipe_image

        queryset.save()
        return redirect("recipe")


    context = {"recipes" : queryset}
    return render(request, "update_recipes.html", context)

     