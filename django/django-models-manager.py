from django.db import models

class BookManager(models.Manager):
    def start_with_a(self):
        return super().get_queryset().filter(title__istartwith='a')


class Book(models.Model):
    title = models.CharField(max_length=200)
    word_count = models.PositiveIntegerField()
    published_on = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    books = BookManager()

    # Book.books.start_with_a()


class Postable(models.Model):
    title = models.CharField(max_length=200)
    published_on = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(Postable):
    word_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title

