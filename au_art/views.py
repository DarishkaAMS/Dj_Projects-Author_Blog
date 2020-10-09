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

# def article(request, user_id):
#     article = Article.objects.get(pk=user_id)
#     return render(request, "article.html", {
#         "title": title,
#         "article": article
#     })

