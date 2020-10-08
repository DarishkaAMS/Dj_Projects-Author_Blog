from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from au_art.models import Article
# Create your views here.


class InitialView(View):

    def get(self, *args, **kwargs):
        # return render(
        #     self.request,
        #     'homepage.html',
        #     {'articles': Article.objects.all()}
        # )

        response = ''
        for art in Article.objects.all():
            response += f"{art.id}, {art.title}, {art.author}\n"
        return HttpResponse(response.encode('utf-8'))



