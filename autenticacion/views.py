from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from .models import *

@api_view(["POST"])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        try:
            user = Loginusuarios.objects.get(username=username)
            
            # Verifica la contraseña
            if check_password(password, user.password):
                return Response(
                    {
                        "code": 200,
                        "status": "success",
                        "message": "Inicio de sesión exitoso",
                        "data": {
                            "user_id": user.id,
                            "username": user.username,
                            "email": user.email,
                            "is_staff": user.is_staff,
                        },
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "code": 400,
                        "status": "error",
                        "message": "Credenciales incorrectas",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Loginusuarios.DoesNotExist:
            return Response(
                {
                    "code": 404,
                    "status": "error",
                    "message": "Usuario no encontrado",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def logout(request):
    request.auth.delete() 
    return Response(
        {"code": 200, "status": "success", "message": "Sesión cerrada correctamente"},
        status=status.HTTP_200_OK,
    )