from django.shortcuts import render, redirect
from .models import Movie, Director, Actor

# Create your views here.
def index(request):
    
    context={
        # goal is to get every movie
        "all_movies": Movie.objects.all(),
        "all_directors": Director.objects.all(),
    }
    return render(request, "index.html", context)


def create_director(request):
    # make a new director
    new_director = Director.objects.create(name= request.POST['director_name'])

    return redirect('/')

def create_movie(request):
    new_movie = Movie.objects.create(
        title= request.POST['movie_name'], 
        year= request.POST['year'], 
        directed_by_id=request.POST['director']
        # previous line is the same thing as > directed_by= Director.objects.get(id=request.POST['director'])
        )

    return redirect('/')

def movie_profile(request, movie_id):
    all_actors= Actor.objects.all()
    this_movie = Movie.objects.get(id= movie_id)

    context={
        "movie": this_movie,
        "other_actors": Actor.objects.exclude(movies_acted_in = this_movie),
        # "other_actors": not in this_movie.actors.all(),
        "all_actors": all_actors
    }
    return render(request, "profile.html", context)

def create_actor(request):
    new_actor= Actor.objects.create(name= request.POST['actor_name'])
    return redirect('/')

def edit_movie(request, movie_id):
    
    context = {
        'movie':Movie.objects.filter(id= movie_id)[0]
    }
    return render(request, 'edit.html', context)

def update_movie(request,movie_id):
    this_movie=Movie.objects.filter(id=movie_id)[0]
    if request.method != 'POST':
        return redirect("/")
    this_movie.title=request.POST['title']
    this_movie.year=request.POST['year']
    this_movie.save()
    return redirect(f"/movie/{movie_id}")


# Note: we are going to fix this delete lecture
def delete(request, movie_id):
    this_movie=Movie.objects.filter(id=movie_id)[0]
    this_movie.delete()
    return redirect("/")

# For a challenge, see if you can write the view that will add the actor/actress to the movie
def add_actor(request):
    pass