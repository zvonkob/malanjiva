from django.shortcuts import render
from . models import Post

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     },
#     {
#         'author': 'Frančiška Šivic',
#         'title': 'Druga svetovna vojna',
#         'content': 'Pričevanje',
#         'date_posted': 'August 29, 2018'
#     }
# ]

def home(request):
    # context = {
    #     'posts': posts
    # }
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog1/home.html', context)


def about(request):
    return render(request, 'blog1/about.html', {'title': 'About'})
