from django.shortcuts import render

posts = [
        {
            'author':'Mike',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': '18.11.2025'
        },
        {
            'author':'Jone Doe',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': '19.11.2025'
        }
]

def home(request):
    context = {
          'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
        return render(request, 'blog/about.html', {'title': 'About'})

