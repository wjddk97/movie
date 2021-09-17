from django.urls        import path
from movies.views       import ActorView, MovieView, Actor_MovieView

urlpatterns = [
    path("actor/",ActorView.as_view()),
    path("movie/",MovieView.as_view()),
    path("actor_movie/",Actor_MovieView.as_view()),
]