from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name =models.CharField(max_length=120)
    email_address = models.EmailField()

    def __str__(self):
        return f" {self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100)
    brief_description = models.CharField(max_length=240)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)

    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True, related_name="author")
    tag = models.ManyToManyField(Tag, related_name="tag")

    def __str__(self):
        return self.title
    