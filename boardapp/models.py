from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)

    # 画像用フィールド
    #  - upload_to='' とするとsettingsで指定されたデフォルトのディレクトリ直下に画像が保存される
    images = models.ImageField(upload_to='')

    like = models.IntegerField()
    read = models.IntegerField()
    read_list = models.CharField(max_length=200)