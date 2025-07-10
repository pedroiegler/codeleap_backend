from rest_framework import generics
from .models import Career
from .serializers import CareerSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CareerListCreateView(generics.ListCreateAPIView):
    queryset = Career.objects.all().order_by('-created_datetime')
    serializer_class = CareerSerializer

    @swagger_auto_schema(
        operation_description="Retorna a lista de todos os posts criados",
        responses={200: CareerSerializer(many=True)},
        tags=["Careers"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria um novo post. Os campos obrigatórios são: username, title e content.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["username", "title", "content"],
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, example="pedro"),
                "title": openapi.Schema(type=openapi.TYPE_STRING, example="Meu primeiro post"),
                "content": openapi.Schema(type=openapi.TYPE_STRING, example="Aqui está o conteúdo do meu post.")
            }
        ),
        responses={
            201: CareerSerializer(),
            400: "Dados inválidos"
        },
        tags=["Careers"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CareerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    http_method_names = ['get', 'patch', 'delete']

    @swagger_auto_schema(
        operation_description="Retorna um post específico com base no ID.",
        responses={
            200: CareerSerializer(),
            404: "Post não encontrado"
        },
        tags=["Careers"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza parcialmente um post (apenas título e conteúdo).",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, example="Título atualizado"),
                "content": openapi.Schema(type=openapi.TYPE_STRING, example="Conteúdo atualizado"),
            }
        ),
        responses={
            200: CareerSerializer(),
            400: "Requisição inválida",
            404: "Post não encontrado"
        },
        tags=["Careers"]
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Remove um post com base no ID.",
        responses={
            204: "Post deletado com sucesso",
            404: "Post não encontrado"
        },
        tags=["Careers"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)