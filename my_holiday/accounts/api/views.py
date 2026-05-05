from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


class LoginView(APIView):

    def post(self, request):
        data = request.data

        serializer = LoginSerializer(data = data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            return Response({
                    "message": "Login successful",
                    "email": user.email
                }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

        

