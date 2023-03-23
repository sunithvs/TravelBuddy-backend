from django.shortcuts import render
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


# detailed blog page
def blog(request, blog_id):
    """
    Blog page:
    Displays a blog post
    """
    context = {
        "blog": Blog.objects.get(id=blog_id),
    }
    return render(request, 'home/blog.html', context)


# detailed destination page
def destination(request, destination_id):
    """
    Destination page:
    Displays a destination
    """
    context = {
        "destination": Destination.objects.get(id=destination_id),
    }
    return render(request, 'home/destination.html', context)


# detailed event page
def event(request, event_id):
    """
    Event page:
    Displays an event
    """
    context = {
        "event": Event.objects.get(id=event_id),
    }
    return render(request, 'home/event.html', context)
