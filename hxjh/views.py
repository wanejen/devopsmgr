from django.shortcuts import render_to_response
from hxjh.models import Serverlist

def search(request):
    errors = []
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            errors.append('Enter a search term: ')
        elif len(query)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Serverlist.objects.filter(name__icontains=query)
            return render_to_response('results.html', locals())

    return render_to_response('test.html', {'errors': errors})

def index(request):
    return render_to_response('index.html')