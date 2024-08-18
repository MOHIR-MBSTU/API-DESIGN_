from django.db import models

class SummarizeSpokenText(models.Model):
    title = models.CharField(max_length=255)
    answer_time_limit = models.PositiveIntegerField()
    audio_files = models.JSONField()  # Store audio file information

class ReOrderParagraph(models.Model):
    title = models.CharField(max_length=255)
    paragraphs = models.JSONField()  # Store paragraphs in the incorrect order

class ReadingMultipleChoice(models.Model):
    title = models.CharField(max_length=255)
    passage = models.TextField()
    options = models.JSONField()  # Store options in a dictionary format

class PracticeHistory(models.Model):
    user_id = models.IntegerField()
    question_type = models.CharField(max_length=50)
    question_id = models.IntegerField()
    score = models.PositiveIntegerField()
    submission_time = models.DateTimeField(auto_now_add=True)
