from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=256)

    def __str__(self):
        return self.category_name


class News(models.Model):
    news_headline = models.CharField(max_length=256)
    content = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.news_headline
