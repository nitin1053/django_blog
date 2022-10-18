from django.shortcuts import render

from django.http import HttpResponse
posts= [
    {
        'author': 'Nitin Jha',
        'title' : 'College freshers',
        'content': 'only code only code !!',
        'date_posted': '18th octomber, 2022',
        'time' : '9AM',
        'location' : 'Pune',

    },
    {
        'author': 'Roonie ',
        'title' : 'Birthday party',
        'content': 'Many many happy return',
        'date_posted': '19th octomber, 2022',
        'time' : '10AM',
        'location' : 'Pune',

    }
    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About page"})

