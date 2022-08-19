from pyexpat import model
from django.db import models

# Create your models here.

class upload_img(models.Model):
    請輸入員工編號 = models.CharField(max_length=200)
    簽名檔上傳 = models.ImageField(upload_to = "static/upload_img")