from django.db import models


class FileModel(models.Model):
  uploader = models.CharField(max_length=20)
  file_name = models.FileField(upload_to='documents')

  def __str__(self):
    return self.uploader
