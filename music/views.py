from django.http import HttpResponse
from music.models import Album
def index(request):
    all_albums= Album.objects.all()
    html=''
    for album in all_albums:
        url=str(album.id)+'/'
        html+='<a href="'+ url +'">'+ album.album_title + '</a><br>'
    return HttpResponse(html) 
def details(request, album_id):
    return HttpResponse("<h2>details for album id: "+ str(album_id)+" </h2>")   
    