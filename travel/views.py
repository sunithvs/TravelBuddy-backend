from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def index(request):
    """
    Home page:
    Contains a register/login form for travelers and travel agents
    Displays a list of upcoming events in Ernakulam
    Displays top 3 destinations
    Displays top 3 blogs
    """
    context = {
        "events": Event.objects.all(),
        "destinations": Destination.objects.all()[0:3],
        "blogs": Blog.objects.all()[0:3],
    }

    return render(request, 'home/index.html', context)


@login_required(login_url='login')
def events(request):
    """
    Events page:
    Displays a list of all events
    """
    context = {
        "title": "Events near you",
        "objects": Event.objects.all(),
        "heading": "Events",
        "subheading": "Events near you",
        "description": "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aspernatur commodi sunt quod veniam voluptas et",
    }

    return render(request, 'home/list.html', context)

@login_required(login_url='login')
def destinations(request):
    """
    Destinations page:
    Displays a list of all destinations
    """
    context = {
        "objects": Destination.objects.all(),
        "heading": "Destinations",
        "subheading": "Destinations near you",
        "description": "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aut temporibus dolor veritatis molestiae enim qui vel ",
        "title": "Destinations near you",
    }
    return render(request, 'home/list.html', context)

@login_required(login_url='login')
def blogs(request):
    """
    Blogs page:
    Displays a list of all blogs
    """
    context = {
        "objects": Blog.objects.all(),
        "heading": "Blogs",
        "subheading": "Go through our blogs",
        "description": "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aut temporibus dolor veritatis molestiae enim qui vel ",
        "title": "Blogs you can read",

    }
    return render(request, 'home/list.html', context)


@login_required(login_url='login')
def blog(request, blog_id):
    """
    Blog page:
    Displays a blog post
    """
    context = {
        "blog": get_object_or_404(Blog, id=blog_id),
    }
    return render(request, 'home/blog.html', context)


# detailed destination page
@login_required(login_url='login')
def destination(request, destination_id):
    """
    Destination page:
    Displays a destination
    """
    des = Destination.objects.get(id=destination_id)
    context = {
        "destination": des,
        "dos": des.get_dos(),
        "donts": des.get_donts(),
        "blogs": Blog.objects.filter(destination=des),
        "hotels": Hotel.objects.filter(destination=des),
        "packages": Package.objects.filter(destinations=des),

    }
    return render(request, 'home/destination.html', context)


# detailed event page
@login_required(login_url='login')
def event(request, event_id):
    """
    Event page:
    Displays an event
    """
    context = {
        "event": Event.objects.get(id=event_id),
    }
    return render(request, 'home/event.html', context)

@login_required(login_url='login')
def search(request):
    """
    Search page:
    Displays search results
    """
    search_query = request.GET.get('q', '')
    # search in title ,description
    context = {
        "destinations": Destination.objects.filter(title__icontains=search_query) | Destination.objects.filter(
            description__icontains=search_query),
        "events": Event.objects.filter(title__icontains=search_query) | Event.objects.filter(
            description__icontains=search_query),
        "blogs": Blog.objects.filter(title__icontains=search_query) | Blog.objects.filter(
            description__icontains=search_query),
        "packages": Package.objects.filter(title__icontains=search_query) | Package.objects.filter(
            description__icontains=search_query),
        "hotels": Hotel.objects.filter(title__icontains=search_query) | Hotel.objects.filter(
            description__icontains=search_query),
        "search_query": search_query, }

    return render(request, 'home/search.html', context)

@login_required(login_url='login')
def hotels(request):
    """
    Hotels page:
    Displays a list of all hotels
    """
    context = {
        "objects": Hotel.objects.all(),
        "heading": "Hotels",
        "subheading": "Hotels near you",
        "description": "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aut temporibus dolor veritatis molestiae enim qui vel ",
        "title": "Hotels near you",
    }
    return render(request, 'home/list.html', context)

@login_required(login_url='login')
def packages(request):
    context = {
        "objects": Package.objects.all(),
        "heading": "Packages",
        "subheading": "Packages near you",
        "description": "aut temporibus dolor veritatis molestiae enim qui vel "
                       "aut temporibus dolor veritatis molestiae enim qui vel ",
        "title": "Packages near you",
    }
    return render(request, 'home/list.html', context)

@login_required(login_url='login')
def package(request, package_id):
    context = {
        "package": Package.objects.get(id=package_id),
    }
    return render(request, 'home/package.html', context)

@login_required(login_url='login')
def hotel(request, hotel_id):
    context = {
        "hotel": Hotel.objects.get(id=hotel_id),
    }
    return render(request, 'home/hotel.html', context)
