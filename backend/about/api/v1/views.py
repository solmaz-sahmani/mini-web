from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def about_api_v1(request):
    return Response("this is about page")