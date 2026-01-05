from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Document(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()
    tags = models.ManyToManyField(Tag, related_name="documents", blank = True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        tag_list = " ".join([f"{tag.name}" for tag in self.tags.all()])
        return f"{tag_list} \n {self.title}"
    
class Question(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="questions", null=True, blank=True)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    answer_text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank=True, related_name='questions')

    def __str__(self):
        return self.question_text[:50]