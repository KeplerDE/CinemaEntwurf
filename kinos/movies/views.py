from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
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
        if form.is_valid():
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form = form.save(commit=False)
            form.movie_id = pk
            form.save()
        return redirect("/")
