"""
travel/urls.py
"""
from django.urls import path, include
from .views import index, events, destinations, blogs, blog, destination, event, search,hotel, hotels, package, packages

urlpatterns = [
    path('', index, name='index'),
    path('events/', events, name='events'),
    path('destinations/', destinations, name='destinations'),
    path('blogs/', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog, name='blog'),
    path("destinations/<int:destination_id>/", destination, name="destination"),
    path("events/<int:event_id>/", event, name="event"),
    path("search", search, name="search"),
    path("hotels", hotels, name="hotels"),
    path("packages/", packages, name="packages"),
    path("packages/<int:package_id>/", package, name="package"),


]
