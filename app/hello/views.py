import re
from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .forms import LogMessageForm
from .models import LogMessage
# Create your views here.


# def home(request):
    # return HttpResponse('Hello Django!')
    # content = {"message_list": LogMessage.objects.all()}
    # return render(request, "hello/home.html", content)

class HomeListView(ListView):
    # model = LogMessage
    context_object_name = "message_list"
    queryset = LogMessage.objects.order_by("-log_date")[:5]
    template_name = "hello/home.html"


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")


def hello_there(request, name):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # match_object = re.match("[a-zA-Z]+", name)

    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"
    
    # content = "Hello there, " + clean_name + "! It's " + formatted_now
    # return HttpResponse(content)
    content = { 'name': name, 'date': datetime.now()}
    return render(request, 'hello/hello_there.html', content)

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})