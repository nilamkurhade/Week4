
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Registration
from . serializers import RegistrationSerializer


# Create your views here.


class RegistrationList(APIView):
    def get(self, request):
        register1 = Registration.objects.all()
        serializer = RegistrationSerializer(register1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


