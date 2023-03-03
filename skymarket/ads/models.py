# from django.conf import settings
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.db import models

from users.models import User


class Ad(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    title = models.CharField(max_length=200, default='')
    price = models.FloatField(default=0, validators=[MinValueValidator(0)])
    description = models.TextField(blank=True, null=True, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ads")
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ["-created_at"]


class Comment(models.Model):
    text = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]
