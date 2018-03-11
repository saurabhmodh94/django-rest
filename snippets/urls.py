from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls))
]
