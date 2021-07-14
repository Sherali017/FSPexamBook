from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class BookModel(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=100)
    cover = models.ImageField()
    is_booked = models.BooleanField(default=True)
    booked_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, )
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title


class Meta:
    verbose_name = 'book'
    verbose_name_plural = 'books'
