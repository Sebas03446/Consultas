from rest_framework import status, views
from rest_framework.response import Response
from consultasApp.models.querySearch import QuerySearch
from consultasApp.serializers.querySerializer import QuerySerializer


class DoctorView(views.APIView):
    def get(self, request):
        allQuerySearch = QuerySearch.objects.all()
        data = []
        for obj in allQuerySearch:
            querySearch = QuerySearch().to_representation(obj=obj)
            data.append(querySearch)

        return Response(data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
