from rest_framework import serializers
from consultasApp.models.querySearch import QuerySearch


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuerySearch
        fields = ['id', 'search', 'amount',
                  'firstSearch', 'lastSearch', 'numberResults']

    def create(self, validated_data):
        queryInstance = QuerySearch.objects.create(
            **validated_data)
        return queryInstance

    def to_representation(self, obj):
        querySearch = QuerySearch.objects.get(id=obj.id)
        return {
            'id': querySearch.id,
            'search': querySearch.search,
            'amount': querySearch.amount,
            'firstSearch': querySearch.firstSearch,
            'lastSearch': querySearch.lastSearch,
            'numberResults': querySearch.numberResults
        }
