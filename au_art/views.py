from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from au_art.models import Article, Author
# Create your views here.


class InitialView(View):

    def get(self, *args, **kwargs):
        return render(
            self.request,
            'homepage.html',
            {'articles': Article.objects.all()}
        )

        # response = ''
        # for art in Article.objects.all():
        #     response += f"{art.id}, {art.title}, {art.author}\n"
        # return HttpResponse(response.encode('utf-8'))


def homepage(request):
    return render(request, "homepage.html", {
        "articles": Article.objects.all()
    })


def user(request):
    return render(request, "user.html")


def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, "article.html", {
        "title": article.title,
        "article": article.article,
        "author": article.author,
        "created_on": article.created_on
    })


# def join(request, article_id):
#     if request.method == "POST":
#         art = Article.objects.get(pk=article_id)
#         title = Article.objects.get(pk=int(request.POST["member"]))
#         # member.task.add(task)
#         return HttpResponseRedirect(reverse("article", args = (article_id,)))