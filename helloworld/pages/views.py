from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_page_view(request):
    context = {
        'home_entries': [
            {'title': 'Hello, world!',
            'body': 'I have created my first template in Django!'
            },
            {
            'title': 'A title',
            'body': 'And a description.'
            }]
    }
    return render(request, 'index.html', context)

def home_page_blog(request):
    content = {
        'blog_entries': [
            { 'list_of_comments' : ['author_name: John Smith',
            'content : This is a Python blog!',
            'creation date and time: 01/01/2020'], 'author_name' : 'John Smith', 
            'creation_date' : [{'day' : 1 , 'month' : 1 , 'year' : 2020}] , 'image' : 'Python'
            },
            { 'list_of_comments' : ['author_name: Victoria Botis',
            'content : This is a travel blog!',
            'creation date and time: 01/05/2020'], 'author_name' : 'Victoria Botis', 
            'creation_date' : [{'day' : 1, 'month' : 5 , 'year' : 2020}] , 'image' : 'Travel'
            },
            {'list_of_comments' : ['author_name: Ted Baker',
            'content : This is a fashion blog!',
            'creation date and time: 01/03/2020'], 'author_name' : 'Ted Baker', 
            'creation_date' : [{'day' : 10, 'month' : 5 , 'year' : 2020}] , 'image' : 'Fashion'
            }
            ]
    }
    return render(request, 'blog.html', content)

def new_page(request):
    return HttpResponse('This is a new page')
