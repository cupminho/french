from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=200)

    def __str__(self):
        return self.file_name

class Sentence(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    sentence_text = models.TextField(null=True)
    tagging_text = models.TextField(null=True)

    def __str__(self):
        return self.sentence_text

class Tagging(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    pos = models.CharField(max_length=20)

    def __str__(self):
        return self.word

class UploadFileModel(models.Model):
    file = models.FileField(null=True)
