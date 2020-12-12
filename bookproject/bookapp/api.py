from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
class myschool(APIView):
    def get(self,request):
        model = Users.object.all()
        serializers = Usersserializer(model,many=True)
        return Response(serializers.data)
