from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

#data = {'movies':['movie1','movie2']}
'''data = {
    'movies': [{'id': 1,'title' : 'MIB',
'year' :2022

},{'id': 2,'title' : 'star wars',
'year' :2001

},{'id': 3,'title' : 'avengers',
'year' :'2010'

}]}#only dict=>'key':'value'''

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html',{'movies': data})


def home(request):
    return HttpResponse("Home Page")

def detail(request,id):
    data = Movie.objects.get(pk = id)
    return render(request, 'movies/detail.html',{'movie': data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title = title,year=year)
        print(movie)
        movie.save()
        return HttpResponseRedirect('/movies')
    
    return render(request,'movies/add.html')

def delete(request,id):
    #Movie.objects.get(pk=id).delete()
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    
    movie.delete()
    return HttpResponseRedirect('/movies')
