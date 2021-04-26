
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Category, Post
from .utils import update_views
from django.contrib.auth.forms import UserCreationForm 

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm

##cooking
from .models import Recipe #NEED TO ADD THIS TO MODEL
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    
    context = {'form':form}
    return render(request,'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')################################ NEED TO CHANGE TO WHATEVER IS THE MY ACCOUNT PAGE
        else:
            messages.info(request, 'Username OR Password is incorrect')


    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    forums = Category.objects.all()
    context = {
        "forums":forums,
    }
    return render(request, "forums.html", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post":post
    }
    update_views(request, post)

    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)

    context = {
        "posts":posts,
        "forum": category,
    }

    return render(request, "posts.html", context)

def homeTwo(request):
    total_recipes = Recipe.objects.all().count()
    context = {
        "title":"Homepage",
        "total_recipes":total_recipes,
    }  
        
    return render(request, "home.html", context)

def search(request):
    recipes = Recipe.objects.all()

    if "search" in request.GET:
        query = request.GET.get("search")
        queryset = recipes.filter(Q(title__icontains=query))

    if request.GET.get("pop"):
        results = queryset.filter(Q(topic__title__icontains="pop"))
        topic = "pop"
    elif request.GET.get("rock"):
        results = queryset.filter(Q(topic__title__icontains="rock"))
        topic="rock"
    elif request.GET.get("ambient"):
        results = queryset.filter(Q(topic__title__icontains="ambient"))
        topic="ambient"
    elif request.GET.get("hip hop"):
        results = queryset.filter(Q(topic__title__icontains="hip hop"))
        topic="hip hop"

    total = results.count()

    #paginate results
    paginator = Paginator(results, 3)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "topic":topic,
        "page":page,
        "total":total,
        "query":query,
        "results":results,
    }
    return render(request, "search.html", context)

def detailTwo(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        "recipe":recipe,
    }
    return render(request, "detailTwo.html", context)