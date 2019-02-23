from django.urls import path
from . import views
from .views import stockAnalysisDetail, stockAnalysisList, stockAnalysisPriceList, stockAnalysisPriceInsert
urlpatterns = [
    path('', stockAnalysisList.as_view() ),
    path('<pk>', stockAnalysisDetail.as_view() ),
    path('price/', stockAnalysisPriceList.as_view() ),
    path('<pk>/insert', stockAnalysisPriceInsert.as_view())
]