from rest_framework import serializers
from .models import SummarizeSpokenText, ReOrderParagraph, ReadingMultipleChoice, PracticeHistory

class SSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = SummarizeSpokenText
        fields = '__all__'

class ROSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReOrderParagraph
        fields = '__all__'

class RMMCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingMultipleChoice
        fields = '__all__'

class PracticeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeHistory
        fields = '__all__'
