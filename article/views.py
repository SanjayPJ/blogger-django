from django.shortcuts import render, redirect
from article.models import Article
from article.forms import ArticleForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "article/article.html", {
        "articles" : articles
    })
def detail(request, slug):
    # return HttpResponse(slug)
    articles = Article.objects.get(slug=slug)
    return render(request, "article/detail.html", {
        "articles" : articles
    })
def create(request):
    if request.method == "POST":
        create_form = ArticleForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect("index")
    else:
        create_form = ArticleForm()
        return render(request, "article/create.html", {
            "create_form" : create_form
        })
def delete(request, slug):
    Article.objects.filter(slug=slug).delete()
    return redirect("index")
    # return HttpResponse(slug)