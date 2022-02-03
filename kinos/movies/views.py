from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from .models import Movie, Actor, Category
from .forms import ReviewForm


class MoviesView(ListView):
    """List of Films"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    #template_name = "movies/movie_list.html"



class MovieDetailView(DetailView):
    """Beschreibung of Films"""
    model = Movie
    slug_field = "url"



class AddReview(View):
    """Bewertungen"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())



class ActorView(DetailView):
    """Вывод информации о актере"""
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"