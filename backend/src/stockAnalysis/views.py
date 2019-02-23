from django.shortcuts import render
from .serializers import stockSerializer, stockPriceSerializer
from .models import Stock, StockPrice
from rest_framework import generics

# Create your views here.

class stockAnalysisList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = stockSerializer

class stockAnalysisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = stockSerializer

class stockAnalysisPriceInsert(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = stockPriceSerializer
    queryset = StockPrice.objects.all()


class stockAnalysisPriceList(generics.ListAPIView):
    """
    A final example of filtering the initial queryset would be to determine the initial queryset based on query parameters in the url.
    We can override .get_queryset() to deal with URLs such as http://example.com/api/purchases?username=denvercoder9, 
    and filter the queryset only if the username parameter is included in the URL

    
    def get_queryset(self):
        
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        
        queryset = Purchase.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset
    """
    serializer_class = stockPriceSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = StockPrice.objects.all()
        company = self.request.query_params.get('sym', None)
        #print("hihi ", company)
        if(company is not None):
            queryset = queryset.filter(sym=company)
        return queryset

    
        
        


class stockAnalysisPriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = stockPriceSerializer
