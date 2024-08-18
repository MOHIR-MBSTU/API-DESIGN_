from rest_framework import viewsets
from .models import SummarizeSpokenText, ReOrderParagraph, ReadingMultipleChoice, PracticeHistory
from .serializers import SSTSerializer, ROSerializer, RMMCQSerializer, PracticeHistorySerializer

class SSTViewSet(viewsets.ModelViewSet):
    queryset = SummarizeSpokenText.objects.all()
    serializer_class = SSTSerializer

class ROViewSet(viewsets.ModelViewSet):
    queryset = ReOrderParagraph.objects.all()
    serializer_class = ROSerializer

class RMMCQViewSet(viewsets.ModelViewSet):
    queryset = ReadingMultipleChoice.objects.all()
    serializer_class = RMMCQSerializer

class PracticeHistoryViewSet(viewsets.ModelViewSet):
    queryset = PracticeHistory.objects.all()
    serializer_class = PracticeHistorySerializer
