from django.shortcuts import render

posts = [
    {
        'author': 'Danny C',
        'title': 'ICA blog post 1',
        'content': 'This is the post content for 1',
        'date_posted': 'May 1, 2020',
    },
    {
        'author': 'claudia c',
        'title': 'Renzo post 2',
        'content': 'content about anime',
        'date_posted': 'August 28, 2021',
    }
]


# Create your views here.
def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
