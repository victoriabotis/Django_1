from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('new_page/', views.new_page, name = "page1"),
    path('blog/',views.home_page_blog, name="blog")
]