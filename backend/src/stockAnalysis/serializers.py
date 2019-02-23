#from rest_framework import serializers
from rest_framework import serializers
from stockAnalysis.models import Stock, StockPrice

#API serializer

class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            'id',
            'symbol',
            'startDate',
            'endDate'
        )
        
        #fields = '__all__'


class stockPriceSerializer(serializers.ModelSerializer):
    class Meta:        
        model = StockPrice
        fields = (
            'id',
            'sym',
            'date',
            'open',
            'high',
            'low',
            'close',
            'volume',
        )
        
        #fields = '__all__'