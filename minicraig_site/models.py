from django.db import models
from django.urls import reverse


class Category(models.Model):
    c_name = models.CharField(max_length=75, unique=True)
    c_description = models.CharField(max_length=255)

    def __str__(self):
        return self.c_name

    def get_absolute_url(self):
        return reverse("cat_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    title = models.CharField(max_length=75)
    text = models.TextField(blank=False)
    category = models.ForeignKey(
        Category, null=False, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post_detail", kwargs={"category": self.category.pk, "pk": self.pk}
        )
