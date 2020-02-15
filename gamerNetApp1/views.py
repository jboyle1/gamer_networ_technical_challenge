from django.shortcuts import render
from gamerNetApp1.models import Article


# Create your views here.

def index(request):
    Article_list = Article.objects.order_by('title')
    Article_dict = { 'Articles': Article_list}
    return render(request, 'gamerNetApp1/index.html', context=Article_dict)