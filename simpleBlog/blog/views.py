from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article

def home(request):
    # Get all articles
    articles = Article.objects.all()
    
    # Paginate - 9 articles per page
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {'page_obj': page_obj})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})