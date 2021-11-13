import os
from re import search
from django.http import response
from rest_framework import status, views
from rest_framework.response import Response
from consultasApp.models.querySearch import QuerySearch
from consultasApp.serializers.querySerializer import QuerySerializer


class QueryFileView(views.APIView):
    def get(self, request, pk):
        serializer = {

        }
        try:
            querySearch = QuerySearch.objects.get(search=pk)
            serializer = QuerySerializer().to_representation(querySearch)
        except:
            print("An exception occurred")

        return Response(data=serializer, status=status.HTTP_200_OK)
