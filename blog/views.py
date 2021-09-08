from django.shortcuts import render

posts = [
    {
        'author': 'erias',
        'title': 'Blog Post 1',
        'content': 'First post content just a dummy post to test it',
        'date_posted': 'September 8, 2021 22:00'
    },
    {
        'author': 'erias',
        'title': 'Blog Post 2',
        'content': 'Second post content just a dummy',
        'date_posted': 'September 8, 2021 22:00'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
