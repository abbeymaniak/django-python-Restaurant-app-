from django.shortcuts import render
from meals.models import Meals , Category
from blog.models import Post
from aboutus.models import Why_Choose_us

# Create your views here.

def home(request):
    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    why_chooose_us = Why_Choose_us.objects.all()
    


    context = {
        'meals' : meals,
        'categories' : categories,
        'meal_list' : meal_list,
        'posts' : posts,
        'latest_post': latest_post,
        'why_choose_us' : why_chooose_us,
    }

    return render(request, 'home/index.html', context)