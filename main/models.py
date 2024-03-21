from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/imgs/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class News(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(max_length=300)
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    comment = models.TextField()
    status= models.BooleanField(default = True)

    
    def __str__(self):
        return self.comment

