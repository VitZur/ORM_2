from django.urls import include,path
from .models import Tag
from django.shortcuts import render
from articles.views import articles_list
from django.conf import settings


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'articles/tag_list.html',{'tags':tags})

urlpatterns = [
    path('', articles_list, name='articles'),
    path('tags/', tag_list,name='tag_list'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns =[
        path('__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
