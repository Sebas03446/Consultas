from re import search
from rest_framework import status, views
from rest_framework.response import Response
from consultasApp.models.querySearch import QuerySearch
from consultasApp.serializers.querySerializer import QuerySerializer


class QuerySearchView(views.APIView):
    def put(self, request):
        queryS = QuerySearch.objects.get(search=request.data["search"])
        serializer = QuerySerializer(
            queryS, data=request.data)  # Se actualizan los datos
        serializer.is_valid(raise_exception=True)  # Se validan
        serializer.save()  # Se guarda
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        allQuerySearch = QuerySearch.objects.all()
        data = []
        for obj in allQuerySearch:
            querySearch = QuerySerializer().to_representation(obj=obj)
            data.append(querySearch)

        return Response(data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
