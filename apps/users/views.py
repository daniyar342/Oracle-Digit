from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .service import CustomUserService
from api.generics import CustomCreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpView(CustomCreateAPIView):
    serializer_class = RegisterSerializer
    service_class = CustomUserService
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,)
        serializer.is_valid(raise_exception=True)
        user = self.service_class.create(**serializer.validated_data)
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        },status=status.HTTP_201_CREATED)
