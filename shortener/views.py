from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url
import uuid


def index(request):
    return render(request, 'index.html')


def create(request):
    pass
    # if request.method == 'POST':
    #    url = request.POST['link']
    #    uid = str(uuid.uuid4())[:5]
    #    new_url = Url(link=url, uuid=uid)
    #    new_url.save()

    #    return HttpResponse(uid)


def go(request, pk):
    pass
    # url_details = Url.objects.get(uuid=pk)

    # return redirect(url_details.link)
