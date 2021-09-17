import json 

from django.http        import JsonResponse
from django.views       import View

from movies.models      import Actor, Movie, Actor_Movie

# Create your views here.
class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"],
            date_of_birth = data["date_of_birth"]
        )
        return JsonResponse({"MESSAGE":"CREATED"}, status=201)
    
    def get(self,request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            movies = actor.actor_movie_set.all()
            movie_list = []
            for movie in movies :
                movie_list.append(movie.movie.title)
            results.append({
                "actor_first_name" : actor.first_name,
                "actor_last_name" : actor.last_name,
                "actor_movie" : movie_list
            })
        return JsonResponse({'resutls':results}, status=200)


class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title = data["title"],
            release_date = data["release_date"],
            running_time = data["running_time"]
        )
        return JsonResponse({"MESSAGE":"CREATED"}, status=201)
    
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actors = movie.actor_movie_set.all()
            actor_list = []
            for actor in actors:
                actor_list.append(actor.actor.first_name)
            results.append({
                "movie_title" : movie.title,
                "movie_running_time" : movie.running_time,
                "actors" : actor_list
            })
        return JsonResponse({'resutls':results}, status=200)

class Actor_MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor_Movie.objects.create(
            actor = Actor.objects.get(id = data["actor_id"]),
            movie = Movie.objects.get(id = data["movie_id"])
        )
        return JsonResponse({"MESSAGE":"CREATED"})