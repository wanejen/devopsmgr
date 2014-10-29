from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.
def test(request):
#    t = Template('<h1>hello, {{uname}}')
#    c = Context({'uname': 'alen'})
    return HttpResponse("Hello, world")
