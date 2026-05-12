from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        # print("=== DEBUG START ===")
        # print("DATA:", request.data)
        # print("HEADERS:", request.headers)
        # print("USER:", request.user)
        # print("=== DEBUG END ===")
        data = request.data
        # print(data)

        serializer = LoginSerializer(data = data)
        

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            # print(serializer.validated_data)
            # print(user)

            return Response({
                    "message": "Login successful",
                    "email": user.email
                }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

        

