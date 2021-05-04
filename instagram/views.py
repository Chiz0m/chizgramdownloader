from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InstagramSerializer
from .models import Instagram
import requests

# Create your views here.
@api_view(['POST'])
def saveDownloadIg(request):
    serializer = InstagramSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        url = serializer.data['url']
        querystring = {"igurl":url}
        headers = {
        'x-rapidapi-key': "6400ff6b24msh0777960a581cf0ap19f8c6jsn307329deaa78",
        'x-rapidapi-host': "instagram-facebook-media-downloader.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return Response(response)
    else:
        return Response(serializer.errors)